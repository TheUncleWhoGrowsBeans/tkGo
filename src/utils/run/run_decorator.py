#!/usr/bin/env python
# coding=utf-8

# @Author              : Uncle Bean
# @Date                : 2020-01-14 09:28:45
# @LastEditors: Uncle Bean
# @LastEditTime: 2020-01-14 10:18:04
# @FilePath            : \src\utils\run\run_decorator.py
# @Description         : 

from functools import wraps
from threading import Thread


class ThreadRun(object):
    def __init__(self):
        pass

    def __call__(self, f):
        @wraps(f)
        def wrapped_f(*args, **kw):
            t = Thread(
                target=f,
                args=args,
                kwargs=kw
            )
            t.start()

        return wrapped_f
        