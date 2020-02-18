#!python
# coding=utf-8

# @Author              : Uncle Bean
# @Date                : 2020-02-18 09:16:23
# @LastEditors: Uncle Bean
# @LastEditTime: 2020-02-18 12:19:45
# @FilePath            : \src\utils\remote\ssh.py
# @Description         : 

import logging
import paramiko


logging.basicConfig(level=logging.INFO, format='%(asctime)s[%(levelname)s]: %(message)s')


class SSH(object):
    def __init__(self, 
            host, 
            port, 
            username, 
            password=None, 
            pkey=None,
            auto_connect=True
            ):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.pkey = pkey
        self.transport = paramiko.Transport((
            self.host, 
            self.port
        ))
        self.stdin = None
        self.stdout = None
        self.stderr = None
        self.sftp = None
        self.ssh = None
        if auto_connect: self.transport_connect()

    def transport_connect(self):
        if self.pkey:
            pkey = paramiko.RSAKey.from_private_key_file(self.pkey)
            self.transport.connect(
                username=self.username, 
                pkey=pkey
                )
        else:
            self.transport.connect(
                username=self.username, 
                password=self.password
                )
    
    def close(self):
        self.transport.close()

    def get_sftp(self):
        self.sftp = paramiko.SFTPClient.from_transport(self.transport)

    def download_file(self, source_file, target_file):
        if not self.sftp: self.get_sftp()
        self.sftp.get(source_file, target_file)

    def get_ssh(self):
        self.ssh = paramiko.SSHClient()
        self.ssh._transport = self.transport

    def exec_command(self, cmd):
        if not self.ssh: self.get_ssh()
        self.stdin, self.stdout, self.stderr = self.ssh.exec_command(cmd)
