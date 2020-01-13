#!/usr/bin/env python
# coding=utf-8

# @Author              : Uncle Bean
# @Date                : 2020-01-13 16:19:32
# @LastEditors: Uncle Bean
# @LastEditTime: 2020-01-13 22:53:02
# @FilePath            : \src\menu\menu.py
# @Description         : 

from tkinter import Menu
from threading import Thread


class EMenu(Menu):
    def __init__(self, *args, **kw):
        self.stdout = kw["stdout"] if "stdout" in kw else print
        self.stderr = kw["stderr"] if "stderr" in kw else print
        for key in ["stdout", "stderr"]:
            if key in kw:
                del kw[key]
        super().__init__(*args, **kw)

    def run(label_name):
        def run_decorator(f):
            def wrapped_f(self, *args, **kw):
                def call():
                    self.entryconfig(label_name, state=DISABLED)
                    f(self, *args, **kw)
                    self.entryconfig(label_name, state=NORMAL)
                t = Thread(target=call)
                t.start()
            return wrapped_f
        return run_decorator




