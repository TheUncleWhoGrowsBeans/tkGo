#!/usr/bin/env python
# coding=utf-8

# @Author              : Uncle Bean
# @Date                : 2020-01-20 14:42:39
# @LastEditors: Uncle Bean
# @LastEditTime: 2020-01-20 15:36:45
# @FilePath            : \src\menu\menu_file.py
# @Description         : 

from menu.menu import EMenu
from toplevel.toplevel_file_find_text import ToplevelFileFindText


class MenuFile(EMenu):

    LABEL_FILE = "File"
    LABEL_FIND_TEXT = "Find text"

    def __init__(self, master=None, cnf={}, **kw):
        super().__init__(master=master, cnf=cnf, **kw)
        master.add_cascade(label=self.LABEL_FILE, menu=self)
        self.add_command(label=self.LABEL_FIND_TEXT, command=self.find_text)

    @EMenu.thread_run(LABEL_FIND_TEXT)
    def find_text(self):
        self.toplevel_file_find_text = ToplevelFileFindText(
            title="查找包含指定内容的文件",
            conf=self.conf,
            stdout=self.stdout,
            stderr=self.stderr
            )