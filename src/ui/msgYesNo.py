# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'msgYesNo.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Msg(object):
    def setupUi(self, Msg):
        Msg.setObjectName("Msg")
        Msg.setFixedSize(527, 185)
        self.btn_no = QtWidgets.QPushButton(Msg)
        self.btn_no.setGeometry(QtCore.QRect(400, 130, 90, 28))
        self.btn_no.setStyleSheet("QPushButton{\n"
"    background: #c73a41;\n"
"    border-radius: 5px;\n"
"    color: white;\n"
"    font-size: 12px;\n"
"}\n"
"QPushButton:hover{\n"
"    background: #bf565b;\n"
"}")
        self.btn_no.setObjectName("btn_no")
        self.btn_yes = QtWidgets.QPushButton(Msg)
        self.btn_yes.setGeometry(QtCore.QRect(290, 130, 90, 28))
        self.btn_yes.setStyleSheet("QPushButton{\n"
"    background: #3dbf5c;\n"
"    border-radius: 5px;\n"
"    color: white;\n"
"    font-size: 12px;\n"
"}\n"
"QPushButton:hover{\n"
"    background: #91dba8;\n"
"}")
        self.btn_yes.setObjectName("btn_yes")
        self.label = QtWidgets.QLabel(Msg)
        self.label.setGeometry(QtCore.QRect(50, 60, 431, 41))
        self.label.setStyleSheet("font-size: 14px;\n"
"text-align: center;\n"
"")
        self.label.setObjectName("label")

        self.retranslateUi(Msg)
        QtCore.QMetaObject.connectSlotsByName(Msg)

    def retranslateUi(self, Msg):
        _translate = QtCore.QCoreApplication.translate
        Msg.setWindowTitle(_translate("Msg", "Aviso"))
        self.btn_no.setText(_translate("Msg", "Não"))
        self.btn_yes.setText(_translate("Msg", "Sim"))
        self.label.setText(_translate("Msg", "TextLabel"))