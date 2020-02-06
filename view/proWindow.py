# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'proWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(819, 665)
        self.outLabel = QtWidgets.QLabel(Dialog)
        self.outLabel.setGeometry(QtCore.QRect(20, 550, 111, 16))
        self.outLabel.setObjectName("outLabel")
        self.outputBrowser = QtWidgets.QTextBrowser(Dialog)
        self.outputBrowser.setGeometry(QtCore.QRect(10, 290, 801, 91))
        self.outputBrowser.setObjectName("outputBrowser")
        self.inputLabel = QtWidgets.QLabel(Dialog)
        self.inputLabel.setGeometry(QtCore.QRect(20, 150, 72, 15))
        self.inputLabel.setObjectName("inputLabel")
        self.sampleLabel = QtWidgets.QLabel(Dialog)
        self.sampleLabel.setGeometry(QtCore.QRect(20, 410, 101, 16))
        self.sampleLabel.setObjectName("sampleLabel")
        self.sampleInputBrowser = QtWidgets.QTextBrowser(Dialog)
        self.sampleInputBrowser.setGeometry(QtCore.QRect(10, 430, 801, 91))
        self.sampleInputBrowser.setObjectName("sampleInputBrowser")
        self.outputLabel = QtWidgets.QLabel(Dialog)
        self.outputLabel.setGeometry(QtCore.QRect(20, 270, 72, 15))
        self.outputLabel.setObjectName("outputLabel")
        self.descripBrowser = QtWidgets.QTextBrowser(Dialog)
        self.descripBrowser.setGeometry(QtCore.QRect(10, 40, 801, 81))
        self.descripBrowser.setObjectName("descripBrowser")
        self.descriptionLabel = QtWidgets.QLabel(Dialog)
        self.descriptionLabel.setGeometry(QtCore.QRect(20, 20, 91, 16))
        self.descriptionLabel.setObjectName("descriptionLabel")
        self.sampleOutputBrowser = QtWidgets.QTextBrowser(Dialog)
        self.sampleOutputBrowser.setGeometry(QtCore.QRect(10, 570, 801, 91))
        self.sampleOutputBrowser.setObjectName("sampleOutputBrowser")
        self.inputBrowser = QtWidgets.QTextBrowser(Dialog)
        self.inputBrowser.setGeometry(QtCore.QRect(10, 170, 801, 71))
        self.inputBrowser.setObjectName("inputBrowser")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.outLabel.setText(_translate("Dialog", "Sample Output"))
        self.inputLabel.setText(_translate("Dialog", "Input"))
        self.sampleLabel.setText(_translate("Dialog", "Sample Input"))
        self.outputLabel.setText(_translate("Dialog", "Output"))
        self.descriptionLabel.setText(_translate("Dialog", "Description"))

