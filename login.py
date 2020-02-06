#!/usr/bin/env python2
# encoding: utf-8
# @Auther     :   yjz
# @File       :   login.py
# @Time       :   2020/2/3 12:54
# @Version    :   0.1
# @Function  :   登录杭电oj


from login_window import *
from login.loginHdu import loginHdu
from login.main_window import *
from PyQt5.QtWidgets import QLineEdit
from main import Main_Window
import requests
import sys
import os

filename = './user.txt'


# 登录窗口类
class Login_Window(QtWidgets.QMainWindow, Ui_LoginMainWindow):

    def __init__(self):
        super(Login_Window, self).__init__()
        self.setupUi(self)

        # 槽信号与事件连接
        self.loginButton.clicked.connect(self.login_button_func)
        self.session = requests.session()
        self.passEdit.setEchoMode(QLineEdit.Password)
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                d = f.readlines()
                username = d[0].strip()
                password = d[1].strip()
                self.userEdit.setText(username)
                self.passEdit.setText(password)
        self.rememPass.setCheckState(True)

    def login_button_func(self):
        '''

        :return: None
        '''
        if self.rememPass.isChecked():
            account = self.userEdit.text()
            password = self.passEdit.text()
            with open(filename, 'w') as f:
                f.write(account + '\n' + password + '\n')
        else:
            os.remove(filename)
        main_window.user = self.userEdit.text()
        self.session = loginHdu(self.session, self.userEdit.text(), self.passEdit.text())
        main_window.session = self.session
        main_window.show()
        self.close()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)  # QApplication相当于main函数，也就是整个程序（很多文件）的主入口函数。对于GUI程序必须至少有一个这样的实例来让程序运行。
    window = Login_Window()  # 生成一个实例（对象）
    main_window = Main_Window()
    window.show()  # 有了实例，就得让它显示。这里的show()是QWidget的方法，用来显示窗口。
    sys.exit(app.exec_())  # 调用sys库的exit退出方法，条件是app.exec_()也就是整个窗口关闭。
