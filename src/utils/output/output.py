#!/usr/bin/env python
# coding=utf-8

# @Author              : Uncle Bean
# @Date                : 2020-01-20 13:45:00
# @LastEditors: Uncle Bean
# @LastEditTime: 2020-02-18 13:36:13
# @FilePath            : \src\utils\output\output.py
# @Description         : 

import pyperclip
import win32clipboard as clip
from tkinter import messagebox


class Output(object):
    @staticmethod
    def copy(text):
        pyperclip.copy(text)
    
    @staticmethod
    def paste():
        clip.OpenClipboard(0)
        text = clip.GetClipboardData(clip.CF_UNICODETEXT)
        clip.CloseClipboard()
        return text
        
    @staticmethod
    def msg_box_info(*values, **kw):
        """信息输出

        :param *values: 信息内容
        :param sep: 信息分隔符
        :param end: 信息结束符
        :param with_time: 信息是否自动添加时间，如with_time=" - "，则输出"{time} - {content}"
        """
        sep = kw["sep"] if "sep" in kw else " "
        end = kw["end"] if "end" in kw else "\n"
        title = kw["title"] if "title" in kw else "INFO"
        content = sep.join(map(lambda x: str(x), values))
        if "with_time" in kw:
            time_cur = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
            content = time_cur + kw["with_time"] + content
        messagebox.showinfo(
            title=title,
            message=content+end
        )

    @staticmethod
    def msg_box_err(*values, **kw):
        """错误输出

        :param *values: 信息内容
        :param sep: 信息分隔符
        :param end: 信息结束符
        :param with_time: 信息是否自动添加时间，如with_time=" - "，则输出"{time} - {content}"
        """
        sep = kw["sep"] if "sep" in kw else " "
        end = kw["end"] if "end" in kw else "\n"
        title = kw["title"] if "title" in kw else "ERROR"
        content = sep.join(map(lambda x: str(x), values))
        if "with_time" in kw:
            time_cur = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
            content = time_cur + kw["with_time"] + content
        messagebox.showerror(
            title=title,
            message=content+end
        )


if __name__ == "__main__":
    Output.msg_box_err("test")