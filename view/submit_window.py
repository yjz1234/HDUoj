#!/usr/bin/env python2
# encoding: utf-8
# @Auther     :   yjz
# @File       :   submit_window.py
# @Time       :   2020/2/4 15:31
# @Version    :   0.1
# @Function  :   提交代码
from view.submitWindow import *

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Host': 'acm.hdu.edu.cn',
    'Origin': 'http://acm.hdu.edu.cn',
    'Referer': 'http://acm.hdu.edu.cn/listproblem.php?vol=1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
}


# 提交窗口
class Sub_Window(QtWidgets.QDialog, Ui_submitDialog):
    def __init__(self):
        super(Sub_Window, self).__init__()
        self.setupUi(self)
        self.session = None
        self.pid = None
