#!/usr/bin/env python2
# encoding: utf-8
# @Auther     :   yjz
# @File       :   pro_window.py
# @Time       :   2020/2/4 14:50
# @Version    :   0.1
# @Function  :   问题界面

from view.proWindow import *


# 主窗口类
class Pro_Window(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self):
        super(Pro_Window, self).__init__()
        self.setupUi(self)
