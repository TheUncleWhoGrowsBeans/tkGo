#!/usr/bin/env python
# coding=utf-8

# @Author              : Uncle Bean
# @Date                : 2020-01-13 21:49:28
# @LastEditors: Uncle Bean
# @LastEditTime: 2020-01-14 16:16:42
# @FilePath            : \src\text\scrolled_text.py
# @Description         : 

import time
from tkinter import INSERT
from tkinter.scrolledtext import ScrolledText


class EScrolledText(ScrolledText):
    
    def __init__(self, master=None, cnf={}, **kw):
        
        super().__init__(master=master, cnf=cnf, **kw)

    def stdout(self, *values, **kw):
        """信息输出

        :param *values: 信息内容
        :param sep: 信息分隔符
        :param end: 信息结束符
        :param start: 信息输出位置
        :param with_time: 信息是否自动添加时间，如with_time=" - "，则输出"{time} - {content}"
        """
        sep = kw["sep"] if "sep" in kw else " "
        end = kw["end"] if "end" in kw else "\n"
        start = kw["start"] if "start" in kw else "1.0"
        content = sep.join(map(lambda x: str(x), values))
        if "with_time" in kw:
            time_cur = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
            content = time_cur + kw["with_time"] + content
        self.insert(start, content + end)
        self.mark_set(INSERT, start)
        self.see(start)