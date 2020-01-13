#!/usr/bin/env python
# coding=utf-8

# @Author              : Uncle Bean
# @Date                : 2020-01-13 17:29:18
# @LastEditors: Uncle Bean
# @LastEditTime: 2020-01-13 22:52:41
# @FilePath            : \src\frame\frame_main.py
# @Description         : 

from tkinter import Frame
from tkinter import NSEW
from frame.frame_text_main import FrameTextMain
from frame.frame_button_main import FrameButtonMain


class FrameMain(Frame):

    FRAME_TEXT_MAIN_NAME = "Text Main"

    def __init__(self, master=None, cnf={}, **kw):

        super().__init__(master=master, cnf=cnf, **kw)

        self.frame_button_main = FrameButtonMain(master=self, cnf=cnf, **kw)
        self.frame_button_main.grid(row=0, column=0, sticky=NSEW)
        
        self.frame_text_main = FrameTextMain(master=self, text=self.FRAME_TEXT_MAIN_NAME)
        self.frame_text_main.grid(row=1, column=0, sticky=NSEW)

        