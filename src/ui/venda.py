# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'venda.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_form_venda(object):
    def setupUi(self, form_venda):
        form_venda.setObjectName("form_venda")
        form_venda.resize(939, 732)
        self.gridLayout = QtWidgets.QGridLayout(form_venda)
        self.gridLayout.setObjectName("gridLayout")
        self.line = QtWidgets.QFrame(form_venda)
        self.line.setStyleSheet("")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 2, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.btn_finish = QtWidgets.QPushButton(form_venda)
        self.btn_finish.setStyleSheet("QPushButton {\n"
"                background: #408552; \n"
"                color: #fff; \n"
"                font: Times New Roman; \n"
"                font-size: 12px; \n"
"                font-weight: 700; \n"
"                border-radius: 5px; \n"
"                height: 30px;\n"
"                width: 150px;\n"
"            }\n"
"\n"
"            QPushButton:hover {\n"
"                background: #4d945f;\n"
"            }")
        self.btn_finish.setObjectName("btn_finish")
        self.gridLayout_2.addWidget(self.btn_finish, 1, 3, 1, 1)
        self.btn_cancel = QtWidgets.QPushButton(form_venda)
        self.btn_cancel.setStyleSheet("QPushButton {\n"
"                background: #d16969; \n"
"                color: #fff; \n"
"                font: Times New Roman; \n"
"                font-size: 12px; \n"
"                font-weight: 700; \n"
"                border-radius: 5px; \n"
"                height: 30px;\n"
"                width: 122px;\n"
"            }\n"
"\n"
"            QPushButton:hover {\n"
"                background: #cf8686;\n"
"            }")
        self.btn_cancel.setObjectName("btn_cancel")
        self.gridLayout_2.addWidget(self.btn_cancel, 1, 0, 1, 1)
        self.btn_total = QtWidgets.QPushButton(form_venda)
        self.btn_total.setStyleSheet("QPushButton {\n"
"                background: #3C8FBC; \n"
"                color: #fff; \n"
"                font: Times New Roman; \n"
"                font-size: 12px; \n"
"                font-weight: 700; \n"
"                border-radius: 5px; \n"
"                height: 30px;\n"
"                width: 150px;\n"
"            }\n"
"\n"
"            QPushButton:hover {\n"
"                background: #81b2eb;\n"
"            }")
        self.btn_total.setObjectName("btn_total")
        self.gridLayout_2.addWidget(self.btn_total, 1, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 1, 1, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 7, 0, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(form_venda)
        self.tableWidget.setStyleSheet("font: 11pt arial;\n"
"color: #434343;\n"
"font-weight: 450;\n"
"alternate-background-color: rgb(232, 232, 232);\n"
"\n"
"")
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.AnyKeyPressed|QtWidgets.QAbstractItemView.DoubleClicked|QtWidgets.QAbstractItemView.EditKeyPressed|QtWidgets.QAbstractItemView.SelectedClicked)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setRowCount(10)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(166)
        self.tableWidget.verticalHeader().setVisible(False)
        self.gridLayout.addWidget(self.tableWidget, 5, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(form_venda)
        self.label_3.setStyleSheet("font-size: 12pt")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.lineMoney = QtWidgets.QLineEdit(form_venda)
        self.lineMoney.setStyleSheet("QLineEdit {\n"
"                background: white;\n"
"                height: 25px;\n"
"                border: 1px solid #474747;\n"
"                border-radius: 2px;\n"
"                font-size: 14px;\n"
"                font: sans-serif;\n"
"                width: 120px;\n"
"            }\n"
"            QLineEdit:focus {\n"
"                border: 1px solid #23a5c2;\n"
"            }")
        self.lineMoney.setObjectName("lineMoney")
        self.horizontalLayout.addWidget(self.lineMoney)
        self.label_2 = QtWidgets.QLabel(form_venda)
        self.label_2.setStyleSheet("font-size: 12pt")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.lineTroco = QtWidgets.QLineEdit(form_venda)
        self.lineTroco.setStyleSheet("QLineEdit {\n"
"                background: white;\n"
"                height: 25px;\n"
"                border: 1px solid #474747;\n"
"                border-radius: 2px;\n"
"                font-size: 14px;\n"
"                font: sans-serif;\n"
"                width: 120px;\n"
"            }\n"
"            QLineEdit:focus {\n"
"                border: 1px solid #23a5c2;\n"
"            }")
        self.lineTroco.setObjectName("lineTroco")
        self.horizontalLayout.addWidget(self.lineTroco)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.label = QtWidgets.QLabel(form_venda)
        self.label.setStyleSheet("font-size: 12pt\n"
"")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.line_total = QtWidgets.QLineEdit(form_venda)
        self.line_total.setStyleSheet("QLineEdit {\n"
"                background: white;\n"
"                height: 25px;\n"
"                border: 1px solid #474747;\n"
"                border-radius: 2px;\n"
"                font-size: 14px;\n"
"                font: sans-serif;\n"
"                width: 120px;\n"
"            }\n"
"            QLineEdit:focus {\n"
"                border: 1px solid #23a5c2;\n"
"            }")
        self.line_total.setObjectName("line_total")
        self.horizontalLayout.addWidget(self.line_total)
        self.gridLayout.addLayout(self.horizontalLayout, 6, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem2, 1, 0, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.lineNome = QtWidgets.QLineEdit(form_venda)
        self.lineNome.setStyleSheet("QLineEdit {\n"
"                background: white;\n"
"                height: 25px;\n"
"                border: 1px solid #474747;\n"
"                border-radius: 2px;\n"
"                font-size: 14px;\n"
"                font: sans-serif;\n"
"                width: 120px;\n"
"            }\n"
"            QLineEdit:focus {\n"
"                border: 1px solid #23a5c2;\n"
"            }")
        self.lineNome.setObjectName("lineNome")
        self.gridLayout_3.addWidget(self.lineNome, 0, 1, 1, 3)
        spacerItem3 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_3.addItem(spacerItem3, 1, 1, 1, 1)
        self.lineCPF = QtWidgets.QLineEdit(form_venda)
        self.lineCPF.setStyleSheet("QLineEdit {\n"
"                background: white;\n"
"                height: 25px;\n"
"                border: 1px solid #474747;\n"
"                border-radius: 2px;\n"
"                font-size: 14px;\n"
"                font: sans-serif;\n"
"                width: 120px;\n"
"            }\n"
"            QLineEdit:focus {\n"
"                border: 1px solid #23a5c2;\n"
"            }")
        self.lineCPF.setObjectName("lineCPF")
        self.gridLayout_3.addWidget(self.lineCPF, 2, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(form_venda)
        self.label_6.setStyleSheet("font-size: 12pt;\n"
"padding: 0 10px;")
        self.label_6.setObjectName("label_6")
        self.gridLayout_3.addWidget(self.label_6, 2, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(form_venda)
        self.label_5.setStyleSheet("font-size: 12pt;\n"
"padding-right: 10px;")
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 2, 0, 1, 1)
        self.lineData = QtWidgets.QLineEdit(form_venda)
        self.lineData.setStyleSheet("QLineEdit {\n"
"                background: white;\n"
"                height: 25px;\n"
"                border: 1px solid #474747;\n"
"                border-radius: 2px;\n"
"                font-size: 14px;\n"
"                font: sans-serif;\n"
"                width: 120px;\n"
"            }\n"
"            QLineEdit:focus {\n"
"                border: 1px solid #23a5c2;\n"
"            }")
        self.lineData.setObjectName("lineData")
        self.gridLayout_3.addWidget(self.lineData, 2, 3, 1, 1)
        self.label_4 = QtWidgets.QLabel(form_venda)
        self.label_4.setStyleSheet("font-size: 12pt;\n"
"padding-right: 10px;")
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 0, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(form_venda)
        self.label_7.setStyleSheet("QLabel {\n"
"    font-size: 18pt;\n"
"    margin: 0  60px;\n"
"}")
        self.label_7.setObjectName("label_7")
        self.gridLayout_3.addWidget(self.label_7, 0, 4, 3, 1)
        self.gridLayout.addLayout(self.gridLayout_3, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btn_add = QtWidgets.QPushButton(form_venda)
        self.btn_add.setStyleSheet("QPushButton {\n"
"                background: #3C8FBC; \n"
"                color: #fff; \n"
"                font: Times New Roman; \n"
"                font-size: 12px; \n"
"                font-weight: 700; \n"
"                border-radius: 5px; \n"
"                height: 30px;\n"
"                width: 150px;\n"
"                margin: 10px 0;\n"
"            }\n"
"\n"
"            QPushButton:hover {\n"
"                background: #81b2eb;\n"
"            }")
        self.btn_add.setObjectName("btn_add")
        self.horizontalLayout_2.addWidget(self.btn_add)
        self.btn_delete = QtWidgets.QPushButton(form_venda)
        self.btn_delete.setStyleSheet("QPushButton {\n"
"                background: #d16969; \n"
"                color: #fff; \n"
"                font: Times New Roman; \n"
"                font-size: 12px; \n"
"                font-weight: 700; \n"
"                border-radius: 5px; \n"
"                height: 30px;\n"
"                width: 150px;\n"
"            }\n"
"\n"
"            QPushButton:hover {\n"
"                background: #cf8686;\n"
"            }")
        self.btn_delete.setObjectName("btn_delete")
        self.horizontalLayout_2.addWidget(self.btn_delete)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.btn_search = QtWidgets.QPushButton(form_venda)
        self.btn_search.setStyleSheet("QPushButton {\n"
"                background-color: rgb(58, 141, 97);\n"
"                color: #fff; \n"
"                font: Times New Roman; \n"
"                font-size: 12px; \n"
"                font-weight: 700; \n"
"                border-radius: 5px; \n"
"                height: 30px;\n"
"                width: 150px;\n"
"            }\n"
"\n"
"            QPushButton:hover {\n"
"                background: #4d945f;\n"
"            }")
        self.btn_search.setObjectName("btn_search")
        self.horizontalLayout_2.addWidget(self.btn_search)
        self.gridLayout.addLayout(self.horizontalLayout_2, 3, 0, 1, 1)

        self.retranslateUi(form_venda)
        QtCore.QMetaObject.connectSlotsByName(form_venda)

    def retranslateUi(self, form_venda):
        _translate = QtCore.QCoreApplication.translate
        form_venda.setWindowTitle(_translate("form_venda", "Nova venda"))
        self.btn_finish.setText(_translate("form_venda", "Finalizar venda"))
        self.btn_cancel.setText(_translate("form_venda", "Cancelar"))
        self.btn_total.setText(_translate("form_venda", "Totalizar"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("form_venda", "Código"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("form_venda", "Descrição"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("form_venda", "Preço Unit."))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("form_venda", "Quantidade"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("form_venda", "Total"))
        self.label_3.setText(_translate("form_venda", "Dinheiro: R$"))
        self.label_2.setText(_translate("form_venda", "Troco: R$"))
        self.label.setText(_translate("form_venda", "Total: R$"))
        self.label_6.setText(_translate("form_venda", "Data"))
        self.label_5.setText(_translate("form_venda", "CPF"))
        self.label_4.setText(_translate("form_venda", "Nome"))
        self.label_7.setText(_translate("form_venda", "Venda"))
        self.btn_add.setText(_translate("form_venda", "Adicionar produto"))
        self.btn_delete.setText(_translate("form_venda", "Excluir produto"))
        self.btn_search.setText(_translate("form_venda", "Buscar informações"))
