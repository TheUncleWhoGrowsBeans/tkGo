#!/usr/bin/env python
# coding=utf-8

# @Author              : Uncle Bean
# @Date                : 2020-01-13 16:48:25
# @LastEditors: Uncle Bean
# @LastEditTime: 2020-03-23 13:35:36
# @FilePath            : \src\menu\menu_main.py
# @Description         : 

from menu.menu import EMenu
from menu.menu_go import MenuGo
from menu.menu_excel import MenuExcel
from menu.menu_file import MenuFile
from menu.menu_impala import MenuImpala
from menu.menu_img import MenuImg


class MenuMain(EMenu):
    def __init__(self, master=None, cnf={}, **kw):
        super().__init__(master=master, cnf=cnf, **kw)
        master.config(menu=self)
        
        self.menu_go = MenuGo(master=self, cnf=cnf, **kw)
        self.menu_excel = MenuExcel(master=self, cnf=cnf, **kw)
        self.menu_file = MenuFile(master=self, cnf=cnf, **kw)
        self.menu_impala = MenuImpala(master=self, cnf=cnf, **kw)
        self.menu_img = MenuImg(master=self, cnf=cnf, **kw)