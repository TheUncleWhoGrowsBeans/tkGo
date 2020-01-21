#!/usr/bin/env python
# coding=utf-8

# @Author              : Uncle Bean
# @Date                : 2020-01-13 16:19:32
# @LastEditors: Uncle Bean
# @LastEditTime: 2020-01-20 14:52:41
# @FilePath            : \src\menu\menu.py
# @Description         : 

from tkinter import messagebox, Menu, NORMAL, DISABLED
from functools import wraps
from threading import Thread
from traceback import print_exc
from utils.output.output import Output


class EMenu(Menu):
    def __init__(self, *args, **kw):
        self.stdout = kw["stdout"] if "stdout" in kw else self.msg_box_info
        self.stderr = kw["stderr"] if "stderr" in kw else self.msg_box_err
        self.conf = kw["conf"] if "conf" in kw else None
        for key in ["stdout", "stderr", "conf"]:
            if key in kw:
                del kw[key]
        super().__init__(*args, **kw)
    
    def msg_box_info(self, *values, **kw):
        return Output.msg_box_info(*values, **kw)
    
    def msg_box_err(self, *values, **kw):
        return Output.msg_box_err(*values, **kw)
        
    def thread_run(label_name):
        def run_decorator(f):
            def wrapped_f(self, *args, **kw):
                def call():
                    self.entryconfig(label_name, state=DISABLED)
                    try:
                        f(self, *args, **kw)
                    except Exception as e:
                        print_exc()
                        self.msg_box_err(str(e))
                    self.entryconfig(label_name, state=NORMAL)
                t = Thread(target=call)
                t.start()
            return wrapped_f
        return run_decorator
