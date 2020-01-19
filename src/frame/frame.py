#!/usr/bin/env python
# coding=utf-8

# @Author              : Uncle Bean
# @Date                : 2020-01-19 13:59:13
# @LastEditors: Uncle Bean
# @LastEditTime: 2020-01-19 14:03:32
# @FilePath            : \src\frame\frame.py
# @Description         : 

from tkinter import Frame


class EFrame(Frame):
    def __init__(self, master, cnf={}, **kw):
        self.stdout = kw["stdout"] if "stdout" in kw else None
        self.stderr = kw["stderr"] if "stderr" in kw else None
        self.conf = kw["conf"] if "conf" in kw else None
        for key in ["stdout", "stderr", "conf"]:
            if key in kw:
                del kw[key]
        super().__init__(master=master, cnf=cnf, **kw)

