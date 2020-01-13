#!/usr/bin/env python
# coding=utf-8

# @Author              : Uncle Bean
# @Date                : 2020-01-13 17:50:58
# @LastEditors: Uncle Bean
# @LastEditTime: 2020-01-13 22:52:23
# @FilePath            : \src\frame\frame_button_main.py
# @Description         : 

from tkinter import Frame, Button
from tkinter import NSEW


class FrameButtonMain(Frame):

    def __init__(self, master=None, cnf={}, **kw):
        
        super().__init__(master=master, cnf=cnf, **kw)
        
        self.button_test = Button(master=self, text="TEST")
        self.button_test.grid(row=0, column=0, sticky=NSEW)