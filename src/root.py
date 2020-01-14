#!/usr/bin/env python
# coding=utf-8

# @Author              : Uncle Bean
# @Date                : 2020-01-13 16:25:38
# @LastEditors: Uncle Bean
# @LastEditTime: 2020-01-14 16:03:21
# @FilePath            : \src\root.py
# @Description         : 

import os
import tkinter as tk
from tkinter import Tk
from tkinter import Menu
from menu.menu_main import MenuMain
from frame.frame_main import FrameMain
from listener.listener_main import ListenerMain


class APP(Tk):

    LISTEN_INVL = 0.5  # 监听频率（监听间隔）
    
    def __init__(self, title="tkGo", width=800, height=600):
        super().__init__()
        self.title(title)
        self.geometry('%dx%d' % (width, height))

        icon_path = os.path.join(
            os.path.dirname(__file__),
            r"..\resources\tkGo.ico"
        )
        self.iconbitmap(icon_path)
        
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
            stdout=self.stdout
        )  
        self.ListenerMain.listen()  # 开启监听
        
        
if __name__ == "__main__":
    app = APP()
    app.mainloop()
