#!/usr/bin/env python
# coding=utf-8

# @Author              : Uncle Bean
# @Date                : 2020-01-20 13:52:53
# @LastEditors: Uncle Bean
# @LastEditTime: 2020-01-21 09:59:57
# @FilePath            : \src\toplevel\toplevel_file_find_text.py
# @Description         : 

import tkinter as tk
from tkinter import filedialog, Label, Entry, StringVar
from toplevel.toplevel import EToplevel
from button.button import EButton
from utils.file.file import File


class ToplevelFileFindText(EToplevel):
    """一个顶级窗口（类似弹窗），用于一键查找文件内容
    """
    FIND_START_DESC = "开始查找"
    FIND_END_DESC = "结束查找"

    def __init__(self, master=None, cnf={}, **kw):
        super().__init__(master, cnf, **kw)
        
        self.dir_to_find = None  # 待查找目录
        self.button_ask_dir = self.create_button_ask_dir()  # 创建按钮（点击后弹出文件夹选择框）
        self.button_ask_dir.grid(row=0, column=0, sticky=tk.NSEW)

        self.dir = StringVar()
        self.dir.set("")
        self.label_dir = Label(self, textvariable=self.dir)  # 创建标签，用于显示所选文件夹路径
        self.label_dir.grid(row=0, column=1, sticky=tk.W)

        self.label_file_name_pattern = Label(self, text="文件名称匹配")  # 创建"文件名称匹配"标签
        self.label_file_name_pattern.grid(row=1, column=0, sticky=tk.NSEW)

        self.file_name_pattern = StringVar()
        self.file_name_pattern.set("*.py")
        self.entry_file_name_pattern = Entry(self, textvariable=self.file_name_pattern)  # 创建"文件名称匹配"输入框
        self.entry_file_name_pattern.grid(row=1, column=1, sticky=tk.NSEW)
        
        self.label_file_content_pattern = Label(self, text="文件内容匹配")  # 创建"文件内容匹配"标签
        self.label_file_content_pattern.grid(row=2, column=0, sticky=tk.NSEW)

        self.file_content_pattern = StringVar()
        self.file_content_pattern.set("import")
        self.entry_file_content_pattern = Entry(self, textvariable=self.file_content_pattern)  # 创建"文件内容匹配"输入框
        self.entry_file_content_pattern.grid(row=2, column=1, sticky=tk.NSEW)

        self.button_find_start = self.create_button_find_start()  # 创建一键查找按钮
        self.button_find_start.grid(row=3, column=0, sticky=tk.NSEW)

        self.button_find_end = self.create_button_find_end()  # 创建查找终止按钮
        self.button_find_end.grid(row=4, column=0, sticky=tk.NSEW)

        self.file_tool = File()  # 实例化文件查找工具

    def create_button_find_start(self):
        button_find_start = EButton(
            self, 
            text=self.FIND_START_DESC, 
            command=lambda: self.find_start(button=button_find_start)
            )
        return button_find_start

    @EButton.thread_run
    def find_start(self, button):
        if not self.dir_to_find:
            self.msg_box_err("请选择文件夹")
            return

        if self.file_name_pattern.get() == "" \
            or self.file_content_pattern.get() == "":
            self.msg_box_err("请输入匹配信息！")
            return

        self.stdout(self.FIND_START_DESC)
        self.file_tool.find_text(
            dir=self.dir_to_find,
            file_name_pattern=self.file_name_pattern.get(),
            file_content_pattern=self.file_content_pattern.get(),
            stdout=self.stdout,
            stderr=self.stderr
            )
        self.stdout(self.FIND_END_DESC, "共找到{}个文件".format(
            len(self.file_tool.find_info)
        ))

    def create_button_find_end(self):
        button_find_end = EButton(
            self, 
            text=self.FIND_END_DESC, 
            command=lambda: self.find_end(button=button_find_end)
            )
        return button_find_end
    
    @EButton.thread_run
    def find_end(self, button):
        self.file_tool.find_text_stop()
        
    def create_button_ask_dir(self):
        button_ask_dir = EButton(
            self, 
            text="选择文件夹", 
            command=lambda: self.ask_dir(button=button_ask_dir)
            )
        return button_ask_dir

    @EButton.thread_run
    def ask_dir(self, button):
        self.dir_to_find = filedialog.askdirectory()
        if self.dir_to_find:
            self.stdout(self.dir_to_find)
            self.dir.set(self.dir_to_find)