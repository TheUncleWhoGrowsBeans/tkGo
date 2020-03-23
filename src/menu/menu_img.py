#!python
# coding=utf-8

# @Author              : Uncle Bean
# @Date                : 2020-03-23 12:12:16
# @LastEditors: Uncle Bean
# @LastEditTime: 2020-03-23 14:09:33
# @FilePath            : \src\menu\menu_img.py
# @Description         : 

import os
from menu.menu import EMenu
from utils.img.ocr import OCR
from utils.clipboard.clipboard import Clipboard


class MenuImg(EMenu):

    LABEL_NAME = "Img"
    LABEL_IMG_TO_EXCEL = "IMG to Excel"
    
    def __init__(self, master=None, cnf={}, **kw):
        super().__init__(master=master, cnf=cnf, **kw)
        # 添加主菜单
        master.add_cascade(label=self.LABEL_NAME, menu=self)
        # 添加子菜单-图片表格数据转Excel
        self.add_command(  
            label=self.LABEL_IMG_TO_EXCEL, 
            command=self.img_to_excel
            )
    
    @EMenu.thread_run(LABEL_IMG_TO_EXCEL)
    def img_to_excel(self):
        # 获取图片文件路径
        data_type, data_content = Clipboard.get_data()
        if data_type != Clipboard.DATA_TYPE_FILE:
            self.msg_box_err("请先复制图片文件", title="错误")
            return

        # 使用ocr进行转换
        ocr = OCR()
        for file in data_content:
            path_excel = ocr.img_to_excel(
                image_path=file,
                secret_id=self.conf.api.TC_OCR_SECRET_ID,
                secret_key=self.conf.api.TC_OCR_SECRET_KEY
                )
            self.msg_box_info("转换成功：\n" + path_excel)
