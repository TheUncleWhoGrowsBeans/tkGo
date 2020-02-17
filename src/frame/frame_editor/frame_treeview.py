#!python
# coding=utf-8

# @Author              : Uncle Bean
# @Date                : 2020-02-03 23:18:31
# @LastEditors: Uncle Bean
# @LastEditTime: 2020-02-05 23:16:20
# @FilePath            : \src\frame\frame_editor\treeview_dir.py
# @Description         : 

import os
import tkinter as tk
from tkinter import ttk
from tkinter import NSEW
from PIL import Image, ImageTk
from frame.frame import EFrame


class FrameTreeview(EFrame):

    def __init__(self, master=None, text=None, **kw):
        
        super().__init__(master=master, **kw)
        
        self.rowconfigure(0, weight=1)  # 设置列权重
        self.columnconfigure(0, weight=1)  # 设置列权重
        
        self.text = text

        self.tree = TreeviewDir(
            self, 
            selectmode='browse', 
            show='tree', 
            padding=[0, 0, 0, 0],
            text_show=self.text,
            conf=self.conf,
            stdout=self.stdout,
            stderr=self.stderr
        )
        self.tree.grid(row=0, column=0, sticky=NSEW)
        self.tree.column('#0', width=150)

        self.vbar = ttk.Scrollbar(
            self, 
            orient=tk.VERTICAL, 
            command=self.tree.yview
        )
        self.vbar.grid(row=0, column=1, sticky=tk.NSEW)
        self.tree.configure(yscrollcommand=self.vbar.set)


class TreeviewDir(ttk.Treeview):
    def __init__(self, master, selectmode, show, padding, text_show, conf, stdout, stderr):
        super().__init__(master=master, selectmode=selectmode, show=show, padding=padding)
        self.conf = conf
        self.stdout = stdout
        self.stderr = stderr

        self.tree_data = {}
        self.tree_img = {}
        
        self.insert_top_node()  # 插入顶部节点
        self.insert_default_node()  # 插入默认节点
        self.insert_bottom_node()  # 插入底部节点
    
    def stdout_with_time(self, *args, **kw):
        kw["with_time"] = " - "
        self.stdout(*args, **kw)
    
    def stderr_with_time(self, *args, **kw):
        kw["with_time"] = " - "
        self.stderr(*args, **kw)

    def insert_default_node(self):
        """插入默认节点
        """
        if self.conf.treeview.DIR_ROOT:
            self.refresh_dir(self.conf.treeview.DIR_ROOT)
        else:
            for i in range(65, 91):
                vol = chr(i) + ':/'
                if os.path.isdir(vol):
                    self.refresh_dir(vol)

    def insert_top_node(self):
        """插入顶部节点
        """
        for dir_path in self.conf.treeview.DIR_TOP:
            if os.path.exists(dir_path):
                self.refresh_dir(dir_path)
            else:
                self.stderr_with_time("not os.path.exists -> " % dir_path)

    def insert_bottom_node(self):
        """插入底部节点
        """
        for dir_path in self.conf.treeview.DIR_BOTTOM:
            if os.path.exists(dir_path):
                self.refresh_dir(dir_path)
            else:
                self.stderr_with_time("not os.path.exists -> " % dir_path)

    def delete_child_node(self, dir_par):
        """删除子节点
        """
        for item in self.get_children(dir_par):
            self.stdout_with_time("delete_child_node -> %s" % item)
            self.delete(item)
    
    def refresh_dir(self, dir_to_refresh, empty=False):
        """刷新目录节点
        """
        if empty: self.delete_child_node(dir_to_refresh)
                
        if os.path.isdir(dir_to_refresh):
            if dir_to_refresh not in self.tree_data.keys():
                self.tree_data[dir_to_refresh] = TreeviewData(
                    tree=self,
                    text=self.get_basename(dir_to_refresh),
                    iid=dir_to_refresh,
                    img=self.get_tree_img(dir_to_refresh)
                )
                self.stdout_with_time(
                    "insert -> %s" % self.tree_data[dir_to_refresh].iid
                )
            try:
                for f in os.listdir(dir_to_refresh):
                    if f.upper() == "$RECYCLE.BIN":
                        continue

                    if f.upper() == self.conf.treeview.FILE_NAME_DIR_README.upper():
                        continue

                    f_path = os.path.join(dir_to_refresh, f)
                    if empty and f_path in self.tree_data.keys():
                        del self.tree_data[f_path]

                    if f_path not in self.tree_data.keys():
                        self.tree_data[f_path] = TreeviewData(
                            tree=self,
                            parent=dir_to_refresh,
                            text=f,
                            iid=f_path,
                            img=self.get_tree_img(f_path)
                        )
            except PermissionError:
                self.delete(dir_to_refresh)
                self.tree_data[dir_to_refresh].img = self.get_tree_img("lock")
                self.tree_data[dir_to_refresh].insert(self)
                self.stderr_with_time("lock -> %s" % self.item(dir_to_refresh)["text"])
    
    @staticmethod
    def get_basename(path):
        basename = os.path.basename(path)
        return basename if basename else path
        
    def get_tree_img(self, path):
        file_type = os.path.splitext(path)[1].lower()
        if path == "lock":
            file_type = path
        elif os.path.isdir(path):
            file_type = "dir"
        elif os.path.islink(path):
            file_type = "link"
        elif file_type not in self.conf.treeview.ICONS.keys():
            file_type = "default"

        if file_type not in self.tree_img.keys():
            self.tree_img[file_type] = ImageTk.PhotoImage(
                Image.open(
                    self.conf.treeview.ICONS[file_type]
                ).resize((16, 16), Image.ANTIALIAS)
            )
            
        return self.tree_img[file_type]


class TreeviewData(object):
    def __init__(self, tree, parent="", index=tk.END, iid=None, text=None, value=None, img=None):
        self.tree = tree
        self.parent = parent
        self.index = index
        self.iid = text if iid is None else iid
        self.text = text
        self.value = iid if value is None else value
        self.img = img
        self.insert()
        
    def insert(self):
        self.tree.insert(
            self.parent,
            self.index,
            self.iid,
            text=self.text,
            values=self.value,
            image=self.img
        )
