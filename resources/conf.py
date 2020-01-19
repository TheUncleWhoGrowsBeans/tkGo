#!/usr/bin/env python
# coding=utf-8

# @Author              : Uncle Bean
# @Date                : 2020-01-14 21:50:32
# @LastEditors: Uncle Bean
# @LastEditTime: 2020-01-19 14:09:30
# @FilePath            : \resources\conf.py
# @Description         : 

import os


class Conf(object):
    
    APP_NAME = "tkGo"
    APP_WIDTH = 1440
    APP_HEIGHT = 900
    PATH_ICON = os.path.join(os.path.dirname(__file__), "tkGo.ico")

    TEXT_OUTPUT_HEIGHT = 15

    DIR = dict()
    DIR["ROOT"] = os.path.dirname(os.path.dirname(__file__))  # 项目根目录
    DIR["DATA"] = os.path.join(DIR["ROOT"], "data")  # 数据目录
    DIR["IMG"] = os.path.join(DIR["ROOT"], "img")  # 数据目录
    DIR["TMP"] = os.path.join(DIR["ROOT"], "tmp")  # 临时目录
    DIR["CLIP"] = os.path.join(DIR["DATA"], "clip")  # 剪贴板数据目录
    DIR["CLIP_IMG"] = os.path.join(DIR["CLIP"], "img")  # 剪贴板图片目录

    @classmethod
    def check_and_mkdir(cls, path=None, dir=None, max_num_cycles=100):
        """检查目录是否存在，若不存在则创建
        """
        dir_name_list = list()
        dir_name = dir if dir else os.path.dirname(path)
        cycle_times = 0
        while not os.path.exists(dir_name):
            dir_name_list.append(dir_name)
            dir_name = os.path.dirname(dir_name)
            cycle_times += 1
            if cycle_times >= max_num_cycles:
                raise RuntimeError('CheckDirError -> {}'.format(path))
        while len(dir_name_list) > 0:
            dir_name_to_make = dir_name_list.pop()
            os.makedirs(dir_name_to_make)
            print("已创建文件夹：%s" % dir_name_to_make)

    @classmethod
    def check_dir_and_mkdir(cls):
        for key, value in cls.DIR.items():
            print(key, value, sep=" -> ")
            cls.check_and_mkdir(dir=value)


if __name__ == "__main__":
    Conf.check_dir_and_mkdir()