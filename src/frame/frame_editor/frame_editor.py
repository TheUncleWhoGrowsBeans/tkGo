#!python
# coding=utf-8

# @Author              : Uncle Bean
# @Date                : 2020-02-03 23:05:51
# @LastEditors: Uncle Bean
# @LastEditTime: 2020-02-05 19:32:23
# @FilePath            : \src\frame\frame_editor\frame_editor.py
# @Description         : 

import tkinter as tk
from tkinter import ttk
from tkinter import NSEW, HORIZONTAL
from frame.frame import EFrame
from frame.frame_editor.frame_treeview import FrameTreeview
from frame.frame_editor.frame_text import FrameText


class FrameEditor(EFrame):

    def __init__(self, master=None, cnf={}, **kw):
        
        super().__init__(master=master, cnf=cnf, **kw)
        
        self.rowconfigure(0, weight=1000)  # 设置行权重
        self.columnconfigure(0, weight=3)  # 设置列权重
        
        self.paned_win_h = ttk.Panedwindow(self, orient=HORIZONTAL)  # 添加水平方向（HORIZONTAL）的推拉窗组件
        self.paned_win_h.grid(row=0, column=0, sticky=NSEW)  # 设置GRID布局，放置在第2行第1列
        
        self.frame_treeview = FrameTreeview(  # 创建放置 treeview 的Frame
            master=self.paned_win_h,  # master为上面创建的垂直推拉窗  
            cnf=cnf, **kw  # 传入其他参数
            )  
        self.paned_win_h.add(self.frame_treeview, weight=1)  # 往推拉窗中添加 frame_treeview 组件，并设置权重

        self.frame_text = FrameText(  # 创建放置 text 的Frame
            master=self.paned_win_h  # master为上面创建的垂直推拉窗  
            )
        self.paned_win_h.add(self.frame_text, weight=2)  # 往推拉窗中添加 frame_text 组件，并设置权重