# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'statusWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_statusDialog(object):
    def setupUi(self, statusDialog):
        statusDialog.setObjectName("statusDialog")
        statusDialog.resize(505, 441)
        self.gridLayout = QtWidgets.QGridLayout(statusDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.tableWidget = QtWidgets.QTableWidget(statusDialog)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.gridLayout.addWidget(self.tableWidget, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(statusDialog)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(statusDialog)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 2, 0, 1, 1)

        self.retranslateUi(statusDialog)
        QtCore.QMetaObject.connectSlotsByName(statusDialog)

    def retranslateUi(self, statusDialog):
        _translate = QtCore.QCoreApplication.translate
        statusDialog.setWindowTitle(_translate("statusDialog", "Dialog"))
        self.label.setText(_translate("statusDialog", "提交状态"))
        self.pushButton.setText(_translate("statusDialog", "刷新"))

