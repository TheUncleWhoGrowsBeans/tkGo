#!/usr/bin/env python
# coding=utf-8

# @Author              : Uncle Bean
# @Date                : 2020-01-13 17:35:10
# @LastEditors: Uncle Bean
# @LastEditTime: 2020-01-19 14:06:53
# @FilePath            : \src\frame\frame_text_main.py
# @Description         : 

from tkinter import NSEW
from frame.label_frame import ELabelFrame
from text.text_main import TextMain


class FrameTextMain(ELabelFrame):

    def __init__(self, master=None, **kw):
        
        super().__init__(master=master, **kw)

        self.columnconfigure(0, weight=1)
        
        self.rowconfigure(0, weight=600)
        self.text_main = TextMain(master=self)
        self.text_main.grid(row=0, column=0, sticky=NSEW)
