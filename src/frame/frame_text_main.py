#!/usr/bin/env python
# coding=utf-8

# @Author              : Uncle Bean
# @Date                : 2020-01-13 17:35:10
# @LastEditors: Uncle Bean
# @LastEditTime: 2020-01-13 17:58:10
# @FilePath            : \src\frame\frame_text_main.py
# @Description         : 

from tkinter import NSEW
from tkinter.ttk import LabelFrame
from text.text_main import TextMain


class FrameTextMain(LabelFrame):

    def __init__(self, master=None, **kw):
        
        super().__init__(master=master, **kw)

        self.text_main = TextMain(master=self, width=110, height=35)
        self.text_main.grid(row=0, column=0, sticky=NSEW)
