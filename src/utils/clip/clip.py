#!/usr/bin/env python
# coding=utf-8

# @Author              : Uncle Bean
# @Date                : 2020-01-17 17:21:50
# @LastEditors: Uncle Bean
# @LastEditTime: 2020-01-17 17:26:37
# @FilePath            : \src\utils\clip\clip.py
# @Description         : 

import win32clipboard as clip


class Clip(object):
    
    DATA_TYPE_FILE = "FILE"
    DATA_TYPE_TEXT = "TEXT"
    DATA_TYPE_IMG = "IMG"
    DATA_TYPE_OTHR = "OTHR"
    IMG_NAME_PRFX = "clip_img_"
    IMG_NAME_SFX = ".png"
    
    @classmethod
    def open(cls):
        clip.OpenClipboard(0)

    @classmethod
    def close(cls):
        clip.CloseClipboard()

    @classmethod
    def get_data(cls, dir_img=None):
        data_type = data_content = None
        cls.open()  # 打开剪贴板
        if clip.IsClipboardFormatAvailable(clip.CF_HDROP):  # 如果是文件格式
            data_content = [file for file in clip.GetClipboardData(clip.CF_HDROP)]
            cls.close()
            data_type = cls.DATA_TYPE_FILE
        elif clip.IsClipboardFormatAvailable(clip.CF_DIB):  # 如果是图片格式
            if dir_img:  # 如果设置了图片目录，则将剪贴板的图片内容保存到该目录
                data = clip.GetClipboardData(clip.CF_DIB)
                cls.close()
                cls.last_img_path = data_content = cls.save_img(data)  # 保存图片
            else:
                cls.close()
            data_type = cls.DATA_TYPE_IMG
        elif clip.IsClipboardFormatAvailable(clip.CF_UNICODETEXT):  # 如果是文本格式
            data_content = clip.GetClipboardData(clip.CF_UNICODETEXT).split("\r\n")
            cls.close()
            data_type = cls.DATA_TYPE_TEXT
        else:
            cls.close()
            data_type = cls.DATA_TYPE_OTHR
        
        return (data_type, data_content)


if __name__ == "__main__":
    print(Clip.get_data())