# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'msg.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setWindowModality(QtCore.Qt.NonModal)
        #Form.resize(391, 140)
        Form.setFixedSize(391,150)
        self.bntExit = QtWidgets.QPushButton(Form)
        self.bntExit.setGeometry(QtCore.QRect(150, 100, 90, 30))
        self.bntExit.setCheckable(False)
        self.bntExit.setAutoDefault(False)
        self.bntExit.setDefault(True)
        self.bntExit.setFlat(False)
        self.bntExit.setObjectName("bntExit")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 20, 331, 71))
        self.label.setStyleSheet("font: 10pt \"Arial\"; text-align: center;")
        self.label.setObjectName("label")
        self.label.setStyleSheet("font-size: 14px; font: arial; font-weight: 300")
        self.bntExit.setStyleSheet("""
            QPushButton {
                background: #4b6cdb; 
                color: #fff; 
                font: Times New Roman; 
                font-size: 14px; 
                font-weight: 700; 
                border-radius: 5px; 
                height: 30px;
            }

            QPushButton:hover {
                background: #6480de;
            }
            """
        )

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Aviso"))
        self.bntExit.setText(_translate("Form", "Fechar"))
        self.label.setText(_translate("Form", ""))