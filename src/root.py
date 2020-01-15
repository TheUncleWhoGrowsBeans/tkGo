#!/usr/bin/env python
# coding=utf-8

# @Author              : Uncle Bean
# @Date                : 2020-01-13 16:25:38
# @LastEditors: Uncle Bean
# @LastEditTime: 2020-01-15 11:08:36
# @FilePath            : \src\root.py
# @Description         : 

import os
import sys
import tkinter as tk
from tkinter import Tk
from tkinter import Menu
from menu.menu_main import MenuMain
from frame.frame_main import FrameMain
from listener.listener_main import ListenerMain


class APP(Tk):

    LISTEN_INVL = 0.5  # 监听频率（监听间隔）
    
    def __init__(self):
        
        super().__init__()

        sys.path.append(os.path.dirname(os.path.dirname(__file__)))
        from resources.conf import Conf
        Conf.check_dir_and_mkdir()  # 检查APP相关目录是否存在，若不存在则创建
        self.title(Conf.APP_NAME)
        self.geometry('%dx%d' % (Conf.APP_WIDTH, Conf.APP_HEIGHT))
        self.iconbitmap(Conf.PATH_ICON)
        
        self.frame_main = FrameMain(master=self)
        self.frame_main.grid(row=0, column=0, sticky=tk.NSEW)
        self.stdout = self.frame_main.frame_text_main.text_main.stdout

        self.menu_main = MenuMain(  # 主菜单
            master=self, 
            tearoff=0,
            stdout=self.stdout
        )

        self.ListenerMain = ListenerMain(  # 监听器
            listen_invl=self.LISTEN_INVL,
            stdout=self.stdout,
            dir_clip_img=Conf.DIR["CLIP_IMG"]  # 传入图片目录则代表开启监听剪贴板的图片并持久化
        )  
        self.ListenerMain.listen()  # 开启监听
        
        
if __name__ == "__main__":
    app = APP()
    app.mainloop()
