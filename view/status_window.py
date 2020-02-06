#!/usr/bin/env python2
# encoding: utf-8
#@Auther     :   yjz
#@File       :   status_window.py
#@Time       :   2020/2/5 13:46
#@Version    :   0.1
#@Function  :

from view.statusWindow import *

class statusDialog(QtWidgets.QDialog, Ui_statusDialog):
    def __init__(self):
        super(statusDialog, self).__init__()
        self.setupUi(self)

