#!/usr/bin/env python
# coding=utf-8

# @Author              : Uncle Bean
# @Date                : 2020-01-13 17:37:46
# @LastEditors: Uncle Bean
# @LastEditTime: 2020-01-13 22:53:12
# @FilePath            : \src\text\text_main.py
# @Description         : 

from text.scrolled_text import EScrolledText


class TextMain(EScrolledText):

    def __init__(self, master=None, cnf={}, **kw):
        
        super().__init__(master=master, cnf=cnf, **kw)