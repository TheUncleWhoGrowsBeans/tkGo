#!/usr/bin/env python
# coding=utf-8

# @Author              : Uncle Bean
# @Date                : 2020-01-17 16:57:55
# @LastEditors: Uncle Bean
# @LastEditTime: 2020-01-18 20:48:00
# @FilePath            : \src\menu\menu_trans.py
# @Description         : 

import os
from menu.menu import EMenu
from assembly.excel.excel import Excel
from utils.clip.clip import Clip


class MenuTrans(EMenu):

    LABEL_TRANS = "Trans"
    LABEL_IMG_TO_EXCEL = "IMG to Excel"
    
    def __init__(self, master=None, cnf={}, **kw):
        super().__init__(master=master, cnf=cnf, **kw)

        master.add_cascade(label=self.LABEL_TRANS, menu=self)
        self.add_command(label=self.LABEL_IMG_TO_EXCEL, command=self.img_to_excel)

    @EMenu.thread_run(LABEL_IMG_TO_EXCEL)
    def img_to_excel(self):
        data_type, data_content = Clip.get_data()
        if data_type != Clip.DATA_TYPE_FILE:
            self.stderr("请先复制Excel文件", title="错误")
            return
            
        error_info = list()
        for file in data_content:
            excel = Excel(
                path=file, 
                img_dir=self.conf.DIR["IMG"], 
                img_dispersed=True, 
                stdout=self.stdout
                )
            excel.download_img_of_wb()
            if len(excel.img_download_failed) > 0:
                error_info.append((file, excel.img_download_failed, "download_failed"))
            excel.add_img_of_wb()
            if len(excel.img_add_failed) > 0:
                error_info.append((file, excel.img_add_failed, "add_failed"))
        
        self.stdout("Finish")
        if len(error_info) > 0:
            for error in error_info:
                self.stdout(error[0], error[2])
                for key, value in error[1].items():
                    self.stdout(key, value)