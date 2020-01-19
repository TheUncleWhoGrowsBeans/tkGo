#!/usr/bin/env python
# coding=utf-8

# @Author              : Uncle Bean
# @Date                : 2020-01-18 23:06:25
# @LastEditors: Uncle Bean
# @LastEditTime: 2020-01-19 16:52:14
# @FilePath            : \src\frame\frame_output.py
# @Description         : 

from tkinter import NSEW, HORIZONTAL
from tkinter import ttk
from text.scrolled_text import EScrolledText
from frame.frame import EFrame


class FrameOutput(EFrame):

    TEXT_STDOUT_NAME = "OUTPUT - stdout"
    TEXT_STDERR_NAME = "OUTPUT - stderr"

    def __init__(self, master=None, **kw):
        
        super().__init__(master=master, **kw)  # Frame初始化
        
        self.rowconfigure(0, weight=1)  # 设置行权重
        self.columnconfigure(0, weight=1)  # 设置列权重
        
        # 添加水平方向（HORIZONTAL）的推拉窗组件
        self.paned_win_h = ttk.Panedwindow(self, orient=HORIZONTAL)  
        # 采用GRID布局，推拉窗放置在第1行第1列，如果有其他组件，可放置在其他行或者其他列
        self.paned_win_h.grid(row=0, column=0, sticky=NSEW)  
        
        self.text_stdout = EScrolledText(  # 创建text组件
            master=self.paned_win_h,  # master为上面创建的水平推拉窗  
            height=self.conf.TEXT_OUTPUT_HEIGHT,  # 设置text组件的高度
            )
        self.text_stdout.stdout(self.TEXT_STDOUT_NAME)  # 在text组件中输出初始化信息
        self.paned_win_h.add(self.text_stdout, weight=2)  # 往推拉窗中添加text组件，并设置权重

        self.text_stderr = EScrolledText(  # 创建text组件
            master=self.paned_win_h,  # master为上面创建的水平推拉窗   
            height=self.conf.TEXT_OUTPUT_HEIGHT  # 设置text组件的高度
            )
        self.text_stderr.stdout(self.TEXT_STDERR_NAME)  # 在text组件中输出初始化信息
        self.paned_win_h.add(self.text_stderr, weight=1)  # 往推拉窗中添加text组件，并设置权重