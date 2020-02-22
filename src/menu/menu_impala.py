#!python
# coding=utf-8

# @Author              : Uncle Bean
# @Date                : 2020-02-18 13:22:47
# @LastEditors: Uncle Bean
# @LastEditTime: 2020-02-21 23:17:18
# @FilePath            : \src\menu\menu_impala.py
# @Description         : 

import os
from datetime import datetime
from menu.menu import EMenu
from utils.db.impala import Impala
from utils.remote.ssh import SSH


class MenuImpala(EMenu):

    LABEL_NAME = "Impala"
    LABEL_NAME_INVALIDATE_METADATA = "Invalidate Metadata"
    LABEL_NAME_COUNT_BY_DATADATE = "Count By Datadate"
    LABEL_NAME_SHELL_EXPORT = "Shell Export"

    DESC_SSH_CMD_FAILED = "执行错误"
    DESC_SSH_DOWNLOAD_SUCCESSED = "下载成功"
    
    def __init__(self, master=None, cnf={}, **kw):
        super().__init__(master=master, cnf=cnf, **kw)
        
        self.impala = Impala(
            host = self.conf.impala.HOST,
            port = self.conf.impala.PORT,
            database = self.conf.impala.DATABASE,
            user = self.conf.impala.USER
        )

        self.ssh = SSH(
            host=self.conf.ssh.SERVER_INFO["s1"]["ip"],
            port=self.conf.ssh.SERVER_INFO["s1"]["port"],
            username=self.conf.ssh.SERVER_INFO["s1"]["user_name"],
            pkey=self.conf.ssh.SERVER_INFO["s1"]["private_key"],
            auto_connect=False,
            stdout=self.stdout,
            stderr=self.msg_box_err
        )

        master.add_cascade(label=self.LABEL_NAME, menu=self)

        self.add_command(
            label=self.LABEL_NAME_INVALIDATE_METADATA, 
            command=self.invalidate_metadata
            )
        self.add_command(
            label=self.LABEL_NAME_COUNT_BY_DATADATE, 
            command=self.count_by_datadate
            )
        self.add_command(
            label=self.LABEL_NAME_SHELL_EXPORT, 
            command=self.shell_export
            )

    @EMenu.thread_run(LABEL_NAME_SHELL_EXPORT)
    def shell_export(self):
        sql = self.paste()
        table_name = self.impala.get_table_name(sql)[0]

        data_dir = "/tmp"
        tmp_name = "{}{}_{}".format(
            self.conf.ssh.FILE_PREFIX,
            table_name,
            datetime.now().strftime('%Y%m%d_%H%M%S')
        )
        file_name = tmp_name + ".csv"
        zip_name = tmp_name + ".zip"
        file_path = data_dir + "/" + file_name
        zip_path = data_dir + "/" + zip_name

        cmd = "impala-shell -i {host}:{port} -q \"{sql}\" -B --output_delimiter=\",\" --print_header -o {file_path}".format(
            file_path=file_path,
            host=self.conf.impala.HOST_SHELL,
            port=self.conf.impala.PORT_SHELL,
            sql=sql.replace("\"", "\\\"")
        )
        self.stdout(cmd)
        self.ssh.transport_connect()
        result = self.ssh.exec_command(cmd)
        self.ssh.output(stdout=self.stdout, stderr=self.stderr)
        if result != 0:
            self.msg_box_err("{}:\n{}".format(self.DESC_SSH_CMD_FAILED, cmd))
            return

        cmd = "cd {data_dir};zip {zip_name} {file_name}".format(
            data_dir=data_dir,
            file_name=file_name,
            zip_name=zip_name
            )
        result = self.ssh.exec_command(cmd)
        self.ssh.output(stdout=self.stdout, stderr=self.stderr)

        cmd_rm = "rm " + file_path
        result_rm = self.ssh.exec_command(cmd_rm)
        
        if result != 0:
            self.msg_box_err("{}:\n{}".format(self.ERR_SSH_CMD, cmd))
            return
        
        target_file = os.path.join(
            os.path.expanduser("~"),
            'Desktop',
            zip_name
        )
        self.ssh.download_file(
            source_file=zip_path,
            target_file=target_file
        )
        cmd_rm = "rm " + zip_path
        result_rm = self.ssh.exec_command(cmd_rm)
        
        self.ssh.close()
        self.msg_box_info(self.DESC_SSH_DOWNLOAD_SUCCESSED + ":\n" + target_file)

    @EMenu.thread_run(LABEL_NAME_COUNT_BY_DATADATE)
    def count_by_datadate(self):
        table_name = self.get_table_name_from_clip()
        self.invalidate_table(table_name, auto_close=False)
        
        sql = "select data_date,count(1) from {} group by data_date order by data_date desc".format(
            table_name
            )
        self.stdout(sql, with_time=" - ")
        result = self.impala.execute(sql)
        result = "\n".join([str(row) for row in result])
        self.stdout("{} -> {}".format(sql, result), with_time=" - ")
        self.msg_box_info(result)
        
    @EMenu.thread_run(LABEL_NAME_INVALIDATE_METADATA)
    def invalidate_metadata(self):
        self.invalidate_table(self.get_table_name_from_clip())

    def invalidate_table(self, table_name, auto_close=True):
        sql = "invalidate metadata {}".format(table_name)
        self.stdout(sql, with_time=" - ")
        result = self.impala.execute(sql=sql, auto_close=auto_close)
        self.stdout("{} -> {}".format(sql, result), with_time=" - ")

    def get_table_name_from_clip(self):
        table_name = self.paste()
        if len(table_name.split(".")) == 1: 
            table_name = table_name.split("_")[0] + "." + table_name
        return table_name
