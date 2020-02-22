#!python
# coding=utf-8

# @Author              : Uncle Bean
# @Date                : 2020-02-18 09:16:23
# @LastEditors: Uncle Bean
# @LastEditTime: 2020-02-21 23:16:41
# @FilePath            : \src\utils\remote\ssh.py
# @Description         : 

import logging
import paramiko
import traceback


logging.basicConfig(level=logging.INFO, format='%(asctime)s[%(levelname)s]: %(message)s')


class SSH(object):
    def __init__(self, 
            host, 
            port, 
            username, 
            password=None, 
            pkey=None,
            auto_connect=True,
            stdout=print,
            stderr=print
            ):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.pkey = pkey
        self.transport = None
        self.stdout = stdout
        self.stderr = stderr
        
        self.cmd_stdin = None
        self.cmd_stdout = None
        self.cmd_stderr = None
        self.sftp = None
        self.ssh = None
        if auto_connect: self.transport_connect()

    def transport_connect(self):
        try:
            self.transport = paramiko.Transport((
                self.host, 
                self.port
            ))
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
        except Exception as e:
            traceback.print_exc()
            self.stderr(str(e))
    
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
        self.cmd_stdin, self.cmd_stdout, self.cmd_stderr = self.ssh.exec_command(cmd)
        return self.cmd_stdout.channel.recv_exit_status()
    
    def output(self, stdout=print, stderr=print):
        for line in self.cmd_stdout.readlines():
            stdout(line)
        for line in self.cmd_stderr.readlines():
            stderr(line)
