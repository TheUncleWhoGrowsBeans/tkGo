#!/usr/bin/env python
# coding=utf-8

# @Author              : Uncle Bean
# @Date                : 2020-01-14 14:30:58
# @LastEditors: Uncle Bean
# @LastEditTime: 2020-01-14 16:21:49
# @FilePath            : \src\assembly\clipboard\clipboard.py
# @Description         : 

import time
import win32clipboard as clip
from traceback import print_exc


class Clipboard(object):
    
    DATA_TYPE_FILE = "FILE"
    DATA_TYPE_TEXT = "TEXT"
    DATA_TYPE_ERROR = "ERROR"

    def __init__(self, num=10, max=99999, listen_invl=0.5, stdout=None):
        self.num = num
        self.max = max
        self.listen_invl = listen_invl
        self.stdout = stdout
        self.data = list()
        self.allow_listen = True
    
    def print(self, content):
        if self.stdout:
            cur_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
            self.stdout(cur_time, self.__class__.__name__, str(content), sep=" -> ")

    def open(self):
        clip.OpenClipboard(0)
    
    def close(self):
        clip.CloseClipboard()

    def get_data(self):
        data_type = data_content = None
        self.open()
        try:
            data_content = [file for file in clip.GetClipboardData(clip.CF_HDROP)]
            data_type = self.DATA_TYPE_FILE
        except TypeError:
            data_content = clip.GetClipboardData(clip.CF_UNICODETEXT).split("\r\n")
            data_type = self.DATA_TYPE_TEXT
        except Exception as e:
            data_content = [str(e)]
            data_type = self.DATA_TYPE_ERROR
            print_exc()
        finally:
            self.close()
        return (data_type, data_content)
    
    def listen(self):
        while self.allow_listen:
            data = self.get_data()
            if len(data[1]) > self.max:
                pass
            elif len(self.data) == 0 or str(data) != str(self.data[-1]):
                self.print(data)
                self.data.append(data)
                if len(self.data) > self.num:
                    del self.data[0]
            time.sleep(self.listen_invl)


if __name__ == "__main__":
    clipboard = Clipboard(stdout=print)
    clipboard.listen()