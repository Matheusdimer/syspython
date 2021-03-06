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
        Msg.resize(435, 159)
        Msg.setStyleSheet("")
        self.gridLayout = QtWidgets.QGridLayout(Msg)
        self.gridLayout.setObjectName("gridLayout")
        self.btn_no = QtWidgets.QPushButton(Msg)
        self.btn_no.setStyleSheet("QPushButton{\n"
"    background: #c73a41;\n"
"    border-radius: 5px;\n"
"    color: white;\n"
"    font-size: 12px;\n"
"    height: 30px;\n"
"    width: 70px;\n"
"}\n"
"QPushButton:hover{\n"
"    background: #bf565b;\n"
"}")
        self.btn_no.setObjectName("btn_no")
        self.gridLayout.addWidget(self.btn_no, 1, 3, 1, 1)
        self.btn_yes = QtWidgets.QPushButton(Msg)
        self.btn_yes.setStyleSheet("QPushButton{\n"
"    background: #3dbf5c;\n"
"    border-radius: 5px;\n"
"    color: white;\n"
"    font-size: 12px;\n"
"    height: 30px;\n"
"    width: 70px;\n"
"}\n"
"QPushButton:hover{\n"
"    background: #91dba8;\n"
"}")
        self.btn_yes.setObjectName("btn_yes")
        self.gridLayout.addWidget(self.btn_yes, 1, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(Msg)
        self.label.setStyleSheet("font-size: 14px;\n"
"text-align: center;\n"
"")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 4)
        spacerItem1 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 2, 1, 1)

        self.retranslateUi(Msg)
        QtCore.QMetaObject.connectSlotsByName(Msg)

    def retranslateUi(self, Msg):
        _translate = QtCore.QCoreApplication.translate
        Msg.setWindowTitle(_translate("Msg", "Aviso"))
        self.btn_no.setText(_translate("Msg", "Não"))
        self.btn_yes.setText(_translate("Msg", "Sim"))
        self.label.setText(_translate("Msg", "TextLabel"))
