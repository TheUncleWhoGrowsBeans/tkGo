#!/usr/bin/env python
# coding=utf-8

# @Author              : Uncle Bean
# @Date                : 2020-01-13 16:19:32
# @LastEditors: Uncle Bean
# @LastEditTime: 2020-01-15 16:01:12
# @FilePath            : \src\menu\menu.py
# @Description         : 

from tkinter import messagebox, Menu, NORMAL, DISABLED
from functools import wraps
from threading import Thread
from traceback import print_exc


class EMenu(Menu):
    def __init__(self, *args, **kw):
        self.stdout = kw["stdout"] if "stdout" in kw else self.msg_box_info
        self.stderr = kw["stderr"] if "stderr" in kw else self.msg_box_err
        for key in ["stdout", "stderr"]:
            if key in kw:
                del kw[key]
        super().__init__(*args, **kw)
    
    def msg_box_info(self, *values, **kw):
        """信息输出

        :param *values: 信息内容
        :param sep: 信息分隔符
        :param end: 信息结束符
        :param with_time: 信息是否自动添加时间，如with_time=" - "，则输出"{time} - {content}"
        """
        sep = kw["sep"] if "sep" in kw else " "
        end = kw["end"] if "end" in kw else "\n"
        content = sep.join(map(lambda x: str(x), values))
        if "with_time" in kw:
            time_cur = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
            content = time_cur + kw["with_time"] + content
        messagebox.showinfo(
            title="stdout",
            message=content+end
        )

    def msg_box_err(self, *values, **kw):
        """错误输出

        :param *values: 信息内容
        :param sep: 信息分隔符
        :param end: 信息结束符
        :param with_time: 信息是否自动添加时间，如with_time=" - "，则输出"{time} - {content}"
        """
        sep = kw["sep"] if "sep" in kw else " "
        end = kw["end"] if "end" in kw else "\n"
        content = sep.join(map(lambda x: str(x), values))
        if "with_time" in kw:
            time_cur = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
            content = time_cur + kw["with_time"] + content
        messagebox.showerror(
            title="stderr",
            message=content+end
        )

    def thread_run(label_name):
        def run_decorator(f):
            def wrapped_f(self, *args, **kw):
                def call():
                    self.entryconfig(label_name, state=DISABLED)
                    try:
                        f(self, *args, **kw)
                    except Exception as e:
                        print_exc()
                        self.stderr(e)
                    self.entryconfig(label_name, state=NORMAL)
                t = Thread(target=call)
                t.start()
            return wrapped_f
        return run_decorator
