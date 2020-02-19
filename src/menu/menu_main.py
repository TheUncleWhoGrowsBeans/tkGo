#!/usr/bin/env python
# coding=utf-8

# @Author              : Uncle Bean
# @Date                : 2020-01-13 16:48:25
# @LastEditors: Uncle Bean
# @LastEditTime: 2020-02-18 13:29:21
# @FilePath            : \src\menu\menu_main.py
# @Description         : 

from menu.menu import EMenu
from menu.menu_go import MenuGo
from menu.menu_trans import MenuTrans
from menu.menu_file import MenuFile
from menu.menu_impala import MenuImpala


class MenuMain(EMenu):
    def __init__(self, master=None, cnf={}, **kw):
        super().__init__(master=master, cnf=cnf, **kw)
        master.config(menu=self)
        
        self.menu_go = MenuGo(master=self, cnf=cnf, **kw)
        self.menu_trans = MenuTrans(master=self, cnf=cnf, **kw)
        self.menu_file = MenuFile(master=self, cnf=cnf, **kw)
        self.menu_impala = MenuImpala(master=self, cnf=cnf, **kw)