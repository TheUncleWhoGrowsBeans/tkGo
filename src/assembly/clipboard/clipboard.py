#!/usr/bin/env python
# coding=utf-8

# @Author              : Uncle Bean
# @Date                : 2020-01-14 14:30:58
# @LastEditors: Uncle Bean
# @LastEditTime: 2020-01-15 11:50:10
# @FilePath            : \src\assembly\clipboard\clipboard.py
# @Description         : 

import os
import time
import win32clipboard as clip
from traceback import print_exc
import ctypes
from ctypes.wintypes import WORD, DWORD, LONG


class BMPFileHeader(ctypes.Structure):  # BMP文件头结构体
    _pack_   = 1                     
    _fields_ = [
        ('bfType', WORD),
        ('bfSize', DWORD),
        ('bfReserved1', WORD),
        ('bfReserved2', WORD),
        ('bfOffBits', DWORD)
    ]

BMPFileHeaderSize = ctypes.sizeof(BMPFileHeader)

class BMPApinfogHeader(ctypes.Structure):  # 位图信息头结构体
    _pack_   = 1
    _fields_ = [
        ('biSize', DWORD),
        ('biWidth', LONG),
        ('biHeight', LONG),
        ('biPLanes', WORD),
        ('biBitCount', WORD),
        ('biCompression', DWORD),
        ('biSizeImage', DWORD),
        ('biXpelsPerMeter', LONG),
        ('biYpelsPerMeter', LONG),
        ('biClrUsed', DWORD),
        ('biClrImportant', DWORD)
    ]
    
BMPApinfogHeaderSize = ctypes.sizeof(BMPApinfogHeader)

ColorTableSize = 0

class Clipboard(object):
    
    DATA_TYPE_FILE = "FILE"
    DATA_TYPE_TEXT = "TEXT"
    DATA_TYPE_IMG = "IMG"
    DATA_TYPE_OTHR = "OTHR"
    IMG_NAME_PRFX = "clip_img_"
    IMG_NAME_SFX = ".png"

    def __init__(self, num=10, max=99999, listen_invl=0.5, stdout=None, dir_img=None):
        self.num = num
        self.max = max
        self.listen_invl = listen_invl
        self.stdout = stdout
        self.data = list()
        self.allow_listen = True
        self.pause_listen = False
        self.dir_img = dir_img
        self.last_img_hex_digest = ""
        self.last_img_path = None

        self.last_clip_sn = 0
    
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
        self.open()  # 打开剪贴板
        if clip.IsClipboardFormatAvailable(clip.CF_HDROP):  # 如果是文件格式
            data_content = [file for file in clip.GetClipboardData(clip.CF_HDROP)]
            self.close()
            data_type = self.DATA_TYPE_FILE
        elif clip.IsClipboardFormatAvailable(clip.CF_DIB):  # 如果是图片格式
            if self.dir_img:  # 如果设置了图片目录，则将剪贴板的图片内容保存到该目录
                data = clip.GetClipboardData(clip.CF_DIB)
                self.close()
                self.last_img_path = data_content = self.save_img(data)  # 保存图片
            else:
                self.close()
            data_type = self.DATA_TYPE_IMG
        elif clip.IsClipboardFormatAvailable(clip.CF_UNICODETEXT):  # 如果是文本格式
            data_content = clip.GetClipboardData(clip.CF_UNICODETEXT).split("\r\n")
            self.close()
            data_type = self.DATA_TYPE_TEXT
        else:
            self.close()
            data_type = self.DATA_TYPE_OTHR
        
        return (data_type, data_content)
    
    def save_img(self, data):
        cur_time = time.strftime('%Y%m%d_%H%M%S', time.localtime(time.time()))  # 当前时间
        img_dir = os.path.join(self.dir_img,cur_time.split("_")[0])  # 分日期存储图片
        if not os.path.exists(img_dir): os.mkdir(img_dir)
        imt_name = "{}{}{}".format(self.IMG_NAME_PRFX, cur_time, self.IMG_NAME_SFX)  # 图片名字
        imt_path = os.path.join(img_dir, imt_name)  # 图片具体路径

        bmp_file_header = BMPFileHeader()  # 创建文件头
        ctypes.memset(ctypes.pointer(bmp_file_header), 0, BMPFileHeaderSize)
        bmp_file_header.bfType = ord('B') | (ord('M') << 8)
        bmp_file_header.bfSize = BMPFileHeaderSize + len(data)
        bmp_file_header.bfOffBits = BMPFileHeaderSize + BMPApinfogHeaderSize + ColorTableSize
        
        with open(imt_path, 'wb') as bmp_file:  # 写入图片内容
            bmp_file.write(bmp_file_header)
            bmp_file.write(data)

        return imt_path

    def listen(self):
        while self.allow_listen:  # 是否允许监听，可通过 allow_listen 控制是否开启监听
            if not self.pause_listen:  # 是否暂停监听，可通过 pause_listen 控制是否暂停监听
                clip_sn = clip.GetClipboardSequenceNumber()  # 获取剪贴板序列号
                if clip_sn != self.last_clip_sn:  # 如果序列号和上次不一样，则代表剪贴板内容发生了变化
                    
                    try:
                        data = self.get_data()  # 获取剪贴板内容
                        if data[1] and len(data[1]) > self.max:  # 如果剪贴板内容太长，则直接跳过
                            pass
                        else:
                            self.print(data)  # 输出剪贴板内容
                            self.data.append(data)  # 将剪贴板内容存入列表
                            if len(self.data) > self.num:  # 如果列表中储存的内容超过限定个数，则删除最早的
                                del self.data[0]
                        self.last_clip_sn = clip_sn  # 记录剪贴板序列号
                    except Exception as e:  # 如果发生异常，则打印异常信息
                        print_exc()
                        self.print(e)

                time.sleep(self.listen_invl)  # 休眠指定时间，一般设为0.5秒就可以了


if __name__ == "__main__":
    clipboard = Clipboard(stdout=print)
    clipboard.listen()