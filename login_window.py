# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login_window.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_LoginMainWindow(object):
    def setupUi(self, LoginMainWindow):
        LoginMainWindow.setObjectName("LoginMainWindow")
        LoginMainWindow.resize(800, 600)
        self.mainWindow = QtWidgets.QWidget(LoginMainWindow)
        self.mainWindow.setObjectName("mainWindow")
        self.loginButton = QtWidgets.QPushButton(self.mainWindow)
        self.loginButton.setGeometry(QtCore.QRect(370, 330, 93, 28))
        self.loginButton.setObjectName("loginButton")
        self.userLabel = QtWidgets.QLabel(self.mainWindow)
        self.userLabel.setGeometry(QtCore.QRect(490, 190, 72, 15))
        self.userLabel.setObjectName("userLabel")
        self.passLabel = QtWidgets.QLabel(self.mainWindow)
        self.passLabel.setGeometry(QtCore.QRect(490, 270, 72, 15))
        self.passLabel.setObjectName("passLabel")
        self.rememPass = QtWidgets.QCheckBox(self.mainWindow)
        self.rememPass.setGeometry(QtCore.QRect(240, 330, 91, 20))
        self.rememPass.setObjectName("rememPass")
        self.userEdit = QtWidgets.QLineEdit(self.mainWindow)
        self.userEdit.setGeometry(QtCore.QRect(240, 180, 241, 31))
        self.userEdit.setObjectName("userEdit")
        self.passEdit = QtWidgets.QLineEdit(self.mainWindow)
        self.passEdit.setGeometry(QtCore.QRect(242, 260, 241, 31))
        self.passEdit.setObjectName("passEdit")
        LoginMainWindow.setCentralWidget(self.mainWindow)
        self.menubar = QtWidgets.QMenuBar(LoginMainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        LoginMainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(LoginMainWindow)
        self.statusbar.setObjectName("statusbar")
        LoginMainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(LoginMainWindow)
        QtCore.QMetaObject.connectSlotsByName(LoginMainWindow)

    def retranslateUi(self, LoginMainWindow):
        _translate = QtCore.QCoreApplication.translate
        LoginMainWindow.setWindowTitle(_translate("LoginMainWindow", "MainWindow"))
        self.loginButton.setText(_translate("LoginMainWindow", "登录"))
        self.userLabel.setText(_translate("LoginMainWindow", "用户名"))
        self.passLabel.setText(_translate("LoginMainWindow", "密码"))
        self.rememPass.setText(_translate("LoginMainWindow", "记住密码"))

