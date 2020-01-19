#!/usr/bin/env python
# coding=utf-8

# @Author              : Uncle Bean
# @Date                : 2020-01-13 16:25:38
# @LastEditors: Uncle Bean
# @LastEditTime: 2020-01-19 14:31:06
# @FilePath            : \src\root.py
# @Description         : 

import os
import sys
import time
import tkinter as tk
from tkinter import Tk
from tkinter import Menu
from menu.menu_main import MenuMain
from frame.frame_main import FrameMain
from listener.listener_main import ListenerMain


class APP(Tk):

    LISTEN_INVL = 0.5  # 监听频率（监听间隔）
    
    def __init__(self):
        self.output("tkGo")

        super().__init__()
        self.output("super init")

        sys.path.append(os.path.dirname(os.path.dirname(__file__)))
        from resources.conf import Conf
        Conf.check_dir_and_mkdir()  # 检查APP相关目录是否存在，若不存在则创建
        self.title(Conf.APP_NAME)
        self.geometry('%dx%d' % (Conf.APP_WIDTH, Conf.APP_HEIGHT))
        self.iconbitmap(Conf.PATH_ICON)
        self.output("basic init")
        
        self.columnconfigure(0, weight=1)
        
        self.rowconfigure(0, weight=1)
        self.frame_main = FrameMain(master=self, conf=Conf)
        self.frame_main.grid(row=0, column=0, sticky=tk.NSEW)
        self.stdout = self.frame_main.frame_output.text_stdout.stdout
        self.stderr = self.frame_main.frame_output.text_stderr.stdout
        self.output("frame_main init")

        self.menu_main = MenuMain(  # 主菜单
            master=self, 
            tearoff=0,
            stdout=self.stdout,
            stderr=self.stderr,
            conf=Conf
        )
        self.output("menu_main init")
        
        self.listener_main = ListenerMain(  # 监听器
            listen_invl=self.LISTEN_INVL,
            stdout=self.stdout,
            stderr=self.stderr,
            conf=Conf
        )  
        self.listener_main.listen()  # 开启监听
        self.output("listener_main init")
    
    def output(self, content):
        cur_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        print(cur_time, content, sep=" -> ")
        
        
if __name__ == "__main__":
    app = APP()
    app.mainloop()
