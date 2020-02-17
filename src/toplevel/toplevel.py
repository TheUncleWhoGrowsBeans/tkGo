#!/usr/bin/env python
# coding=utf-8

# @Author              : Uncle Bean
# @Date                : 2020-01-20 13:41:19
# @LastEditors: Uncle Bean
# @LastEditTime: 2020-02-17 22:23:49
# @FilePath            : \src\toplevel\toplevel.py
# @Description         : 

from tkinter import Toplevel
from utils.output.output import Output


class EToplevel(Toplevel, Output):
    def __init__(self, master=None, cnf={}, **kw):
        self.stdout = kw.pop("stdout") if "stdout" in kw else None
        self.stderr = kw.pop("stderr") if "stderr" in kw else None
        self.conf = kw.pop("conf") if "conf" in kw else None
        self.title_name = kw.pop("title") if "title" in kw else None
        super().__init__(master, cnf, **kw)

        if self.title_name: self.title(self.title_name)
        if self.conf: self.iconbitmap(self.conf.PATH_ICON)

        # 置顶
        self.attributes("-toolwindow", 1)  
        self.wm_attributes("-topmost", 1)