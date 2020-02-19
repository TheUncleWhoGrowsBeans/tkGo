#!python
# coding=utf-8

# @Author              : Uncle Bean
# @Date                : 2020-02-18 15:50:09
# @LastEditors: Uncle Bean
# @LastEditTime: 2020-02-18 16:27:21
# @FilePath            : \src\utils\db\sql.py
# @Description         : 

import re


class SQL(object):
    @staticmethod
    def get_table_name(sql):
        pattern = re.compile(r"(?:from|update|delete|table)[\s]+([._a-z0-9]+)", re.I)
        table_name = pattern.findall(sql)
        if len(table_name) == 0:
            table_name = ["null"]
        return table_name

