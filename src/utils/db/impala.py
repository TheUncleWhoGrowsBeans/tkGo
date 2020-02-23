#!python
# coding=utf-8

# @Author              : Uncle Bean
# @Date                : 2020-02-18 13:27:56
# @LastEditors: Uncle Bean
# @LastEditTime: 2020-02-23 20:17:36
# @FilePath            : \src\utils\db\impala.py
# @Description         : 

from impala.dbapi import connect
from impala.error import ProgrammingError
from utils.db.sql import SQL

class Impala(SQL):

    DESC_EXEC_SUCCESS = "执行成功"

    def __init__(self, host, port, database, user, password=None):
        """Impala工具类
        :param host: IP
        :param port: 端口
        :param database: 数据库名
        :param user: 用户名
        :param password: 密码
        """
        self.host = host
        self.port = port
        self.database = database
        self.user = user
        self.password = password
        self.connect = None
        self.cursor = None
        
    def get_connect(self, timeout=600):
        """获取连接
        :param timeout: 超时时间
        """
        self.connect = connect(
            host=self.host,  # IP 
            port=self.port,  # 端口
            timeout=timeout,  # 超时时间
            database=self.database  # 数据库名
            )

    def get_cursor(self, dictify=False):
        """获取游标
        """
        self.cursor = self.connect.cursor(
            user=self.user,  # 用户名
            dictify=dictify
            )

    def close(self):
        """关闭连接
        """
        self.cursor.close()
        self.connect.close()
        self.cursor = None
        self.connect = None

    def execute(self, sql, dictify=False, auto_close=True):
        """执行sql
        :param auto_close: 执行结束是否自动关闭连接
        """
        if not self.connect: self.get_connect()
        self.get_cursor(dictify=dictify)
        self.cursor.execute(sql)
        try:
            result = self.cursor.fetchall()
        except ProgrammingError:
            result = self.DESC_EXEC_SUCCESS
        if auto_close: self.close()
        return result
