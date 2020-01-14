#!/usr/bin/env python
# coding=utf-8

# @Author              : Uncle Bean
# @Date                : 2020-01-14 15:54:44
# @LastEditors: Uncle Bean
# @LastEditTime: 2020-01-14 16:06:40
# @FilePath            : \src\listener\listener_main.py
# @Description         : 

from threading import Thread
from assembly.clipboard.clipboard import Clipboard


class ListenerMain(object):
    def __init__(self, listen_invl=0.5, stdout=print):
        self.__threads = list()

        self.clipboard = Clipboard(listen_invl=listen_invl, stdout=stdout)  # 剪贴板监听器
        self.__threads.append(Thread(target=self.clipboard.listen))

    def listen(self):
        for thread in self.__threads:
            thread.setDaemon(True)
            thread.start()