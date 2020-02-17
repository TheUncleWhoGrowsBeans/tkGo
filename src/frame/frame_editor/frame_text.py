#!python
# coding=utf-8

# @Author              : Uncle Bean
# @Date                : 2020-02-03 23:26:34
# @LastEditors: Uncle Bean
# @LastEditTime: 2020-02-05 19:37:20
# @FilePath            : \src\frame\frame_editor\frame_text.py
# @Description         : 

from tkinter import NSEW
from frame.label_frame import ELabelFrame
from text.scrolled_text import EScrolledText


class FrameText(ELabelFrame):

    TITLE_INIT = "未选择"

    def __init__(self, master=None, **kw):
        
        super().__init__(master=master, **kw)

        self["text"] = self.TITLE_INIT
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        self.text = EScrolledText(master=self)
        self.text.grid(row=0, column=0, sticky=NSEW)