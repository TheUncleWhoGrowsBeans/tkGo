#!/usr/bin/env python
# coding=utf-8

# @Author              : Uncle Bean
# @Date                : 2020-01-13 17:29:18
# @LastEditors: Uncle Bean
# @LastEditTime: 2020-02-05 21:13:44
# @FilePath            : \src\frame\frame_main.py
# @Description         : 

import tkinter as tk
from tkinter import ttk
from tkinter import NSEW, VERTICAL
from frame.frame import EFrame
from frame.frame_text_main import FrameTextMain
from frame.frame_editor.frame_editor import FrameEditor
from frame.frame_button_main import FrameButtonMain
from frame.frame_output import FrameOutput


class FrameMain(EFrame):

    def __init__(self, master=None, cnf={}, **kw):

        super().__init__(master=master, cnf=cnf, **kw)  # Frame初始化

        self.columnconfigure(0, weight=1)  # 设置列权重

        self.frame_button_main = FrameButtonMain(master=self, cnf=cnf, **kw)  # 创建放置按钮的Frame
        self.frame_button_main.grid(row=0, column=0, sticky=NSEW)  # 设置GRID布局，放置在第1行第1列
        
        self.rowconfigure(1, weight=1)  # 设置行权重
        self.paned_win_v = ttk.Panedwindow(self, orient=VERTICAL)  # 添加垂直方向（VERTICAL）的推拉窗组件
        self.paned_win_v.grid(row=1, column=0, sticky=NSEW)  # 设置GRID布局，放置在第2行第1列
        
        self.frame_output = FrameOutput(  # 创建放置output的Frame
            master=self.paned_win_v,  # master为上面创建的垂直推拉窗  
            cnf=cnf, **kw  # 传入其他参数
            )  
        self.paned_win_v.add(self.frame_output, weight=1)  # 往推拉窗中添加frame_output组件，并设置权重

        self.frame_editor = FrameEditor(  # 创建放置text_main的Frame
            master=self.paned_win_v,  # master为上面创建的垂直推拉窗  
            cnf=cnf, 
            stdout=self.frame_output.text_stdout.stdout,
            stderr=self.frame_output.text_stderr.stdout,
            **kw  # 传入其他参数
            )
        self.paned_win_v.add(self.frame_editor, weight=1000)  # 往推拉窗中添加frame_editor组件，并设置权重
