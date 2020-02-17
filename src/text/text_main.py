#!/usr/bin/env python
# coding=utf-8

# @Author              : Uncle Bean
# @Date                : 2020-01-13 17:37:46
# @LastEditors: Uncle Bean
# @LastEditTime: 2020-02-03 23:39:43
# @FilePath            : \src\text\text_main.py
# @Description         : 

from tkinter import NSEW
from text.scrolled_text import EScrolledText


class TextMain(EScrolledText):

    def __init__(self, master=None, cnf={}, **kw):
        
        super().__init__(master=master, cnf=cnf, **kw)

        self.text = EScrolledText(master=self)
        self.text.grid(row=0, column=0, sticky=NSEW)