#!/usr/bin/env python
# coding=utf-8

# @Author              : Uncle Bean
# @Date                : 2020-01-13 16:56:59
# @LastEditors: Uncle Bean
# @LastEditTime: 2020-01-14 10:09:17
# @FilePath            : \src\menu\menu_go.py
# @Description         : 

import time
from menu.menu import EMenu
from utils.run.run_decorator import ThreadRun
from threading import Thread


class MenuGo(EMenu):

    LABEL_GO = "Go"
    LABEL_START = "开始"
    LABEL_END = "终止"
    
    def __init__(self, master=None, cnf={}, **kw):
        super().__init__(master=master, cnf=cnf, **kw)
        self.go = None
        master.add_cascade(label=self.LABEL_GO, menu=self)
        self.add_command(label=self.LABEL_START, command=self.start)
        self.add_command(label=self.LABEL_END, command=self.end)

    @EMenu.thread_run(LABEL_START)
    def start(self):
        self.go = True
        while self.go:
            self.stdout("biu biu biu!", with_time=" - ")
            time.sleep(1)
    
    def end(self):
        self.go = False
        self.stdout("zi zi zi!", with_time=" - ")