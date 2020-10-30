# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cadastro.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow2(object):

    def setupUi(self, MainWindow):
        self.css = "height: 25px; border: 1.2px solid #404040; background-color: white; border-radius: 5px; font: arial; font-size: 14px;"
        self.csslabel = "color: #333333; font-size: 14px; font: arial; font-weight: 400"
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(350, 180)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.linecod = QtWidgets.QLineEdit(self.centralwidget)
        self.linecod.setObjectName("linecod")
        self.gridLayout.addWidget(self.linecod, 0, 1, 1, 1)
        self.linedesc = QtWidgets.QLineEdit(self.centralwidget)
        self.linedesc.setObjectName("linedesc")
        self.gridLayout.addWidget(self.linedesc, 1, 1, 1, 1)
        self.linevalor = QtWidgets.QLineEdit(self.centralwidget)
        self.linevalor.setObjectName("linevalor")
        self.gridLayout.addWidget(self.linevalor, 3, 1, 1, 1)
        self.linetipo = QtWidgets.QLineEdit(self.centralwidget)
        self.linetipo.setObjectName("linetipo")
        self.gridLayout.addWidget(self.linetipo, 4, 1, 1, 1)
        self.linecod.setStyleSheet(self.css)
        self.linedesc.setStyleSheet(self.css)
        self.linetipo.setStyleSheet(self.css)
        self.linevalor.setStyleSheet(self.css)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)
        self.label.setStyleSheet(self.csslabel)
        self.label_2.setStyleSheet(self.csslabel)
        self.label_3.setStyleSheet(self.csslabel)
        self.label_4.setStyleSheet(self.csslabel)
        self.btn_confirm = QtWidgets.QPushButton(self.centralwidget)
        self.btn_confirm.setObjectName("btn_confirm")
        self.gridLayout.addWidget(self.btn_confirm, 5, 1, 1, 1)
        self.btn_cancel = QtWidgets.QPushButton(self.centralwidget)
        self.btn_cancel.setObjectName("btn_cancel")
        self.gridLayout.addWidget(self.btn_cancel, 5, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.btn_confirm.setStyleSheet("""
            QPushButton {
                background: #408552; 
                color: #fff; 
                font: Times New Roman; 
                font-size: 14px; 
                font-weight: 700; 
                border-radius: 5px; 
                height: 30px;
            }

            QPushButton:hover {
                background: #4d945f;
            }
            """
        )

        self.btn_cancel.setStyleSheet("""
            QPushButton {
                background: #d16969; 
                color: #fff; 
                font: Times New Roman; 
                font-size: 14px; 
                font-weight: 700; 
                border-radius: 5px; 
                height: 30px;
            }

            QPushButton:hover {
                background: #cf8686;
            }
            """
        )
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Código"))
        self.label_2.setText(_translate("MainWindow", "Descrição"))
        self.label_3.setText(_translate("MainWindow", "Valor Unitário R$"))
        self.label_4.setText(_translate("MainWindow", "Tipo"))
        self.btn_confirm.setText(_translate("MainWindow", "Cadastrar Produto"))
        self.btn_cancel.setText(_translate("MainWindow", "Cancelar"))
