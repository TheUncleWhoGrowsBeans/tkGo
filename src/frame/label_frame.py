#!/usr/bin/env python
# coding=utf-8

# @Author              : Uncle Bean
# @Date                : 2020-01-19 14:05:32
# @LastEditors: Uncle Bean
# @LastEditTime: 2020-01-19 14:08:17
# @FilePath            : \src\frame\label_frame.py
# @Description         : 

from tkinter.ttk import LabelFrame


class ELabelFrame(LabelFrame):
    def __init__(self, master, **kw):
        self.stdout = kw["stdout"] if "stdout" in kw else None
        self.stderr = kw["stderr"] if "stderr" in kw else None
        self.conf = kw["conf"] if "conf" in kw else None
        for key in ["stdout", "stderr", "conf"]:
            if key in kw:
                del kw[key]
        super().__init__(master=master, **kw)
