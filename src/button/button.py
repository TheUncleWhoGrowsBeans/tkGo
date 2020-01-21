#!/usr/bin/env python
# coding=utf-8

# @Author              : Uncle Bean
# @Date                : 2020-01-20 15:49:17
# @LastEditors: Uncle Bean
# @LastEditTime: 2020-01-21 14:39:27
# @FilePath            : \src\button\button.py
# @Description         : 

from threading import Thread
from traceback import print_exc
from tkinter import Button, NORMAL, DISABLED
from utils.output.output import Output


class EButton(Button):
    def __init__(self, master=None, cnf={}, **kw):
        self.stdout = kw["stdout"] if "stdout" in kw else self.msg_box_info
        self.stderr = kw["stderr"] if "stderr" in kw else self.msg_box_err
        self.conf = kw["conf"] if "conf" in kw else None
        for key in ["stdout", "stderr", "conf"]:
            if key in kw:
                del kw[key]
        super().__init__(master, cnf, **kw)

    def msg_box_info(self, *values, **kw):
        return Output.msg_box_info(*values, **kw)
    
    def msg_box_err(self, *values, **kw):
        return Output.msg_box_err(*values, **kw)
        
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
        