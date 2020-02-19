#!python
# coding=utf-8

# @Author              : Uncle Bean
# @Date                : 2020-02-19 16:39:19
# @LastEditors: Uncle Bean
# @LastEditTime: 2020-02-19 20:19:09
# @FilePath            : \resources\conf_ssh_template.py
# @Description         : 

class ConfSSH(object):
    FILE_PREFIX = "bean_"
    SERVER_INFO = {
        "server1": {
            "name": "server1",
            "ip": "172.1.1.1",
            "port": 22,
            "user_name": "root",
            "password": "1234456"        
        }
    }