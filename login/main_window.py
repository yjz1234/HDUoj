# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Num1 = QtWidgets.QPushButton(self.centralwidget)
        self.Num1.setObjectName("Num1")
        self.horizontalLayout.addWidget(self.Num1)
        self.Num2 = QtWidgets.QPushButton(self.centralwidget)
        self.Num2.setObjectName("Num2")
        self.horizontalLayout.addWidget(self.Num2)
        self.Num3 = QtWidgets.QPushButton(self.centralwidget)
        self.Num3.setObjectName("Num3")
        self.horizontalLayout.addWidget(self.Num3)
        self.Num4 = QtWidgets.QPushButton(self.centralwidget)
        self.Num4.setObjectName("Num4")
        self.horizontalLayout.addWidget(self.Num4)
        self.Num5 = QtWidgets.QPushButton(self.centralwidget)
        self.Num5.setObjectName("Num5")
        self.horizontalLayout.addWidget(self.Num5)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.textNum = QtWidgets.QTextBrowser(self.centralwidget)
        self.textNum.setObjectName("textNum")
        self.gridLayout.addWidget(self.textNum, 0, 1, 1, 1)
        self.Jump = QtWidgets.QPushButton(self.centralwidget)
        self.Jump.setObjectName("Jump")
        self.gridLayout.addWidget(self.Jump, 0, 2, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.gridLayout.addWidget(self.tableWidget, 1, 0, 1, 3)
        self.gridLayout.setColumnStretch(0, 10)
        self.gridLayout.setColumnStretch(1, 1)
        self.gridLayout.setRowStretch(0, 2)
        self.gridLayout.setRowStretch(1, 80)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setAutoFillBackground(False)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Num1.setText(_translate("MainWindow", "1"))
        self.Num2.setText(_translate("MainWindow", "2"))
        self.Num3.setText(_translate("MainWindow", "3"))
        self.Num4.setText(_translate("MainWindow", "4"))
        self.Num5.setText(_translate("MainWindow", "5"))
        self.Jump.setText(_translate("MainWindow", "跳转"))

