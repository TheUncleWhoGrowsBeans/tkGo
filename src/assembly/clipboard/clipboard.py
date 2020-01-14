#!/usr/bin/env python
# coding=utf-8

# @Author              : Uncle Bean
# @Date                : 2020-01-14 14:30:58
# @LastEditors: Uncle Bean
# @LastEditTime: 2020-01-14 14:50:28
# @FilePath            : \src\assembly\clipboard\clipboard.py
# @Description         : 

import win32clipboard as clip
from traceback import print_exc


class Clipboard(object):
    def __init__(self, num=10):
        self.data = list()
    
    def test(self):
        clip.OpenClipboard(0)
        try:
            file_path = [file for file in clip.GetClipboardData(clip.CF_HDROP)]
            print(file_path)
        except TypeError:
            text = clip.GetClipboardData(clip.CF_UNICODETEXT)
            print(text)
        except Exception:
            print_exc()
        clip.CloseClipboard(0)


if __name__ == "__main__":
    clipboard = Clipboard()
    clipboard.test()