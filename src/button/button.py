#!/usr/bin/env python
# coding=utf-8

# @Author              : Uncle Bean
# @Date                : 2020-01-20 15:49:17
# @LastEditors: Uncle Bean
# @LastEditTime: 2020-02-17 22:20:30
# @FilePath            : \src\button\button.py
# @Description         : 

import tkinter as tk
from threading import Thread
from traceback import print_exc
from tkinter import Button, NORMAL, DISABLED
from utils.output.output import Output


class EButton(Button, Output):
    def __init__(self, master=None, cnf={}, **kw):
        if "thread_command" in kw:
            kw["command"] = self.thread_command(kw.pop("thread_command"))
            
        # self.stdout = kw["stdout"] if "stdout" in kw else self.msg_box_info
        # self.stderr = kw["stderr"] if "stderr" in kw else self.msg_box_err
        # self.conf = kw["conf"] if "conf" in kw else None
        for key in ["stdout", "stderr", "conf"]:
            if key in kw:
                del kw[key]
        super().__init__(master, cnf, **kw)

    def thread_run(f):
        def wrapped_f(self, *args, **kw):
            def call():
                kw["button"].config(state=DISABLED)
                try:
                    f(self, *args, **kw)
                except Exception as e:
                    print_exc()
                    self.msg_box_err(str(e))
                kw["button"].config(state=NORMAL)
            t = Thread(target=call)
            t.start()
        return wrapped_f

    def thread_command(self, f):
        def wrapped_f(*args, **kw):
            def call():
                self.config(state=tk.DISABLED)
                try:
                    f(*args, **kw)
                except Exception as e:
                    print_exc()
                    self.msg_box_err(str(e))
                self.config(state=tk.NORMAL)
            t = Thread(target=call)
            t.start()
        return wrapped_f
        