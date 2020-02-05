#!/usr/bin/env python
# coding=utf-8

# @Author              : Uncle Bean
# @Date                : 2020-01-20 13:41:19
# @LastEditors: Uncle Bean
# @LastEditTime: 2020-02-05 10:21:56
# @FilePath            : \src\toplevel\toplevel.py
# @Description         : 

from tkinter import Toplevel
from utils.output.output import Output


class EToplevel(Toplevel, Output):
    def __init__(self, master=None, cnf={}, **kw):
        self.stdout = kw["stdout"] if "stdout" in kw else self.msg_box_info
        self.stderr = kw["stderr"] if "stderr" in kw else self.msg_box_err
        self.conf = kw["conf"] if "conf" in kw else None
        self.title_name = kw["title"] if "title" in kw else None
        for key in ["stdout", "stderr", "conf", "title"]:
            if key in kw:
                del kw[key]

        super().__init__(master, cnf, **kw)

        if self.title_name: self.title(self.title_name)
        if self.conf: self.iconbitmap(self.conf.PATH_ICON)

        # 置顶
        self.attributes("-toolwindow", 1)  
        self.wm_attributes("-topmost", 1)