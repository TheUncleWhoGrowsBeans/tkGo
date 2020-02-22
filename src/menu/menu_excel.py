#!/usr/bin/env python
# coding=utf-8

# @Author              : Uncle Bean
# @Date                : 2020-01-17 16:57:55
# @LastEditors: Uncle Bean
# @LastEditTime: 2020-02-22 22:08:08
# @FilePath            : \src\menu\menu_excel.py
# @Description         : 

import os
from menu.menu import EMenu
from utils.file.excel.excel import Excel
from utils.clipboard.clipboard import Clipboard


class MenuExcel(EMenu):

    LABEL_NAME = "Excel"
    LABEL_START_IMG_TO_EXCEL = "Start IMG to Excel"
    LABEL_STOP_IMG_TO_EXCEL = "Stop IMG to Excel"
    
    def __init__(self, master=None, cnf={}, **kw):

        super().__init__(master=master, cnf=cnf, **kw)

        self.excel = None

        master.add_cascade(label=self.LABEL_NAME, menu=self)
        self.add_command(
            label=self.LABEL_START_IMG_TO_EXCEL, 
            command=self.start_img_to_excel
            )
        self.add_command(
            label=self.LABEL_STOP_IMG_TO_EXCEL, 
            command=self.stop_img_to_excel
            )

        

    @EMenu.thread_run(LABEL_START_IMG_TO_EXCEL)
    def start_img_to_excel(self):
        data_type, data_content = Clipboard.get_data()
        if data_type != Clipboard.DATA_TYPE_FILE:
            self.msg_box_err("请先复制Excel文件", title="错误")
            return
            
        error_info = list()
        for file in data_content:
            self.excel = Excel(
                path=file, 
                img_dir=self.conf.DIR["IMG"], 
                img_dispersed=True, 
                stdout=self.stdout
                )
            self.excel.start_download_of_wb(thread_num=4)
            if len(self.excel.img_download_failed) > 0:
                error_info.append((file, self.excel.img_download_failed, "图片下载失败"))
            if not self.excel.img_download_stop:
                self.excel.add_img_of_wb()
                if len(self.excel.img_add_failed) > 0:
                    error_info.append((file, self.excel.img_add_failed, "图片嵌入失败"))
        
        if len(error_info) > 0:
            for error in error_info:
                self.stderr(error[0], error[2])
                for key, value in error[1].items():
                    self.stderr(" -> ", key, value)
        
        self.msg_box_info("IMG to Excel Finish")
    
    @EMenu.thread_run(LABEL_STOP_IMG_TO_EXCEL)
    def stop_img_to_excel(self):
        self.excel.img_download_stop = True
