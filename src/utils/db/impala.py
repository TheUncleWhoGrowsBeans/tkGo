#!python
# coding=utf-8

# @Author              : Uncle Bean
# @Date                : 2020-02-18 13:27:56
# @LastEditors: Uncle Bean
# @LastEditTime: 2020-02-18 18:06:31
# @FilePath            : \src\utils\db\impala.py
# @Description         : 

from impala.dbapi import connect
from impala.error import ProgrammingError
from utils.db.sql import SQL

class Impala(SQL):

    DESC_EXEC_SUCCESS = "执行成功"

    def __init__(self, host, port, database, user, password=None):
        self.host = host
        self.port = port
        self.database = database
        self.user = user
        self.password = password
        self.connect = None
        self.cursor = None
        
    def get_connect(self, timeout=600):
        self.connect = connect(
            host=self.host, 
            port=self.port, 
            timeout=timeout, 
            database=self.database
            )

    def get_cursor(self):
        self.cursor = self.connect.cursor(user=self.user)

    def close(self):
        self.cursor.close()
        self.connect.close()

    def execute(self, sql, auto_close=True):
        if not self.connect: self.get_connect()
        if not self.cursor: self.get_cursor()
        self.cursor.execute(sql)
        try:
            result = self.cursor.fetchall()
        except ProgrammingError:
            result = self.DESC_EXEC_SUCCESS
        if auto_close: self.close()
        return result
