#!/usr/bin/env python
# coding=utf-8

# @Author              : Uncle Bean
# @Date                : 2020-01-20 11:06:51
# @LastEditors: Uncle Bean
# @LastEditTime: 2020-01-21 13:50:53
# @FilePath            : \src\utils\file\file.py
# @Description         : 

import os
import re


class File(object):
    def __init__(self):
        self.stop = False  # 强制结束标记
        self.find_info = dict()  # 用于记录查找到的信息
    
    def find_text_stop(self):
        """强制结束查找
        """
        self.stop = True

    def get_file_data(self, file_path):
        """获取文件内容

        :param file_path: 文件完整路径
        """
        data = None
        
        try:
            f = open(file_path, mode="r", encoding="utf-8")  # 尝试用utf8编码打开
            data = f.read().splitlines()  # 将文件内容读取为按行分隔的列表
            f.close()  # 关闭文件
        except UnicodeDecodeError:
            f = open(file_path, mode="r", encoding="gb18030")  # 尝试用gb18030编码打开
            data = f.read().splitlines()  # 将文件内容读取为按行分隔的列表
            f.close()  # 关闭文件
    
        return data

    def find_text(
        self,
        dir, 
        file_name_pattern="*", 
        file_content_pattern="", 
        stdout=print, 
        stderr=print,
        output_max=613
        ):
        """查找文件内容

        :param dir: 待查找目录
        :param file_name_pattern: 文件名模糊匹配
        :param file_content_pattern: 待查找的文本内容
        :param output_max: 字符串长度超过max值则不打印具体信息
        """
        if file_content_pattern == "": stderr("请输入查找内容！"); return  # 查找内容不能为空
        if file_name_pattern == "": file_name_pattern = "*"  # 文件名匹配为空则查找目录下所有文件
        
        file_name_pattern = r"^{}$".format(file_name_pattern.replace("*", ".*"))  # 转换成正则表达式
        file_content_pattern = r"{}".format(file_content_pattern.replace("*", ".*"))  # 转换成正则表达式

        self.stop = False  #  初始化强制停止标记
        self.find_info = dict()  # 初始化查找信息
        for root, dirs, files in os.walk(dir):  # 遍历文件
            if self.stop:  # 用于控制手动强制停止查找
                break
            for file in files:
                if self.stop:  # 用于控制手动强制停止查找
                    break
                file_path = os.path.abspath(os.path.join(root, file))  # 文件完整路径
                if re.search(file_name_pattern, file, re.I):  # 判断文件名是否满足模糊匹配规则
                    try:
                        data = self.get_file_data(file_path=file_path)  # 获取文件数据
                    except UnicodeDecodeError:
                        stderr(file_path, str(e))  # 输出异常信息（编码问题）
                        continue
                    except PermissionError as e:
                        stderr(file_path, str(e))  # 输出异常信息（权限问题）
                        continue
                    
                    row_id = 0  # 行号
                    
                    for line in data:  # 遍历每一行数据
                        row_id += 1  # 行号
                        if re.search(file_content_pattern, line, re.I):  # 判断是否为要查找的内容
                            self.find_info[file_path] = self.find_info.get(file_path, 0) + 1  # 记录查找到的信息
                            stdout(  # 输出查找到的信息
                                file_path, 
                                "第" + str(row_id) + "行", 
                                line if len(line) <= output_max else "……"
                                )
                    
                    
if __name__ == "__main__":
    find_dir = r"C:\ProgramData"
    file_name_pattern = "*"
    file_content_pattern = "test"
    file = File()
    file.find_text(
        dir=find_dir, 
        file_name_pattern=file_name_pattern, 
        file_content_pattern=file_content_pattern
        )