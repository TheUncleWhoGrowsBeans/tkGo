#!/usr/bin/env python
# coding=utf-8

# @Author              : Uncle Bean
# @Date                : 2020-01-13 16:19:32
# @LastEditors: Uncle Bean
# @LastEditTime: 2020-01-14 10:09:43
# @FilePath            : \src\menu\menu.py
# @Description         : 

from tkinter import Menu
from tkinter import DISABLED, NORMAL
from threading import Thread
from functools import wraps


class EMenu(Menu):
    def __init__(self, *args, **kw):
        self.stdout = kw["stdout"] if "stdout" in kw else print
        self.stderr = kw["stderr"] if "stderr" in kw else print
        for key in ["stdout", "stderr"]:
            if key in kw:
                del kw[key]
        super().__init__(*args, **kw)

    def thread_run(label_name):
        def run_decorator(f):
            @wraps(f)
            def wrapped_f(self, *args, **kw):
                def call():
                    self.entryconfig(label_name, state=DISABLED)  # 设置菜单选项禁用
                    f(self, *args, **kw)
                    self.entryconfig(label_name, state=NORMAL)  # 设置菜单选项启用
                t = Thread(target=call)
                t.start()
            return wrapped_f
        return run_decorator




