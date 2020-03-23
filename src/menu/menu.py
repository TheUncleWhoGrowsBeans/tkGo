#!/usr/bin/env python
# coding=utf-8

# @Author              : Uncle Bean
# @Date                : 2020-01-13 16:19:32
# @LastEditors: Uncle Bean
# @LastEditTime: 2020-02-24 18:53:46
# @FilePath            : \src\menu\menu.py
# @Description         : 

from tkinter import messagebox, Menu, NORMAL, DISABLED
from functools import wraps
from threading import Thread
from traceback import print_exc
from utils.output.output import Output


class EMenu(Menu, Output):
    def __init__(self, *args, **kw):
        self.stdout = kw.pop("stdout") if "stdout" in kw else None
        self.stderr = kw.pop("stderr") if "stderr" in kw else None
        self.conf = kw.pop("conf") if "conf" in kw else None
        kw["tearoff"] = kw.get("tearoff", 0)
        super().__init__(*args, **kw)
    
    @staticmethod
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
