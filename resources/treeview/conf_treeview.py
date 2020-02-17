#!python
# coding=utf-8

# @Author              : Uncle Bean
# @Date                : 2020-02-05 19:43:34
# @LastEditors: Uncle Bean
# @LastEditTime: 2020-02-05 23:11:50
# @FilePath            : \resources\conf_treeview.py
# @Description         : 

import os


class ConfTreeview(object):
    DIR_ROOT = ""  # 树节点根目录
    
    DIR_TOP = []
    DIR_BOTTOM = []

    FILE_EXT_README = ".es"  # 备注文件扩展名
    FILE_EXT_README_REV = ".esr"  # 逆序备注文件扩展名
    FILE_NAME_DIR_README = "readme" + FILE_EXT_README  # 文件夹备注文件名称

    DIR_ICON = os.path.abspath(os.path.join(__file__, "../img"))
    ICONS = {
        "default": "square10.bmp",
        "dir": "dir.bmp",
        "link": "link.bmp",
        "lock": "lock.ico",
        ".es": "es.ico",
        ".esr": "es.ico",
        ".exe": "divx.ico",
        ".txt": "1f.bmp",
        
        # office
        ".xls": "excel.ico",
        ".xlsx": "excel.ico",
        ".doc": "word.ico",
        ".docx": "word.ico",
        ".ppt": "ppt.ico",
        ".pptx": "ppt.ico",
        ".csv": "csv.ico",

        # 图片
        ".jpg": "e5.ico",
        ".jpeg": "e5.ico",
        ".png": "e6.ico",
        ".gif": "e4.ico",

        # 压缩包
        ".zip": "winrar.ico",
        ".rar": "winrar.ico",
        ".gz": "winrar.ico",

        # 编程语言
        ".js": "js.ico",
        ".java": "java.ico",
        ".jar": "jar.ico",
        ".php": "php.ico",
        ".py": "python.ico",
        ".bat": "bat.ico",
        ".sh": "sh.ico",
        ".scala": "scala.ico",
        ".sql": "sql.ico",
        ".json": "json.ico",
    }

    def __init__(self):
        # 补齐icon完整路径
        for k, v in self.ICONS.items():
            self.ICONS[k] = os.path.join(self.DIR_ICON, v)


if __name__ == "__main__":
    conf_treeview = ConfTreeview()
    print(conf_treeview.ICONS)