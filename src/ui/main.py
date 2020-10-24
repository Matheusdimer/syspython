# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./src/ui/images/cadastro.svg"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.btn_cad = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_cad.sizePolicy().hasHeightForWidth())
        self.btn_cad.setSizePolicy(sizePolicy)
        self.btn_cad.setMinimumSize(QtCore.QSize(0, 0))
        self.btn_cad.setSizeIncrement(QtCore.QSize(0, 0))
        self.btn_cad.setBaseSize(QtCore.QSize(0, 0))
        self.btn_cad.setStyleSheet("QPushButton {\n"
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
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("./src/ui/images/add.svg"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.btn_cad.setIcon(icon1)
        self.btn_cad.setIconSize(QtCore.QSize(18, 18))
        self.btn_cad.setObjectName("btn_cad")
        self.gridLayout.addWidget(self.btn_cad, 4, 2, 1, 1)
        self.btn_refresh = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_refresh.sizePolicy().hasHeightForWidth())
        self.btn_refresh.setSizePolicy(sizePolicy)
        self.btn_refresh.setSizeIncrement(QtCore.QSize(0, 0))
        self.btn_refresh.setStyleSheet("QPushButton {\n"
"                background: #3C8FBC; \n"
"                color: #fff; \n"
"                font: Times New Roman; \n"
"                font-size: 12px; \n"
"                font-weight: 700; \n"
"                border-radius: 5px; \n"
"                height: 30px;\n"
"                padding: 0 5px;\n"
"            }\n"
"\n"
"            QPushButton:hover {\n"
"                background: #81b2eb;\n"
"            }")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("./src/ui/images/refresh.svg"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.btn_refresh.setIcon(icon2)
        self.btn_refresh.setObjectName("btn_refresh")
        self.gridLayout.addWidget(self.btn_refresh, 5, 2, 1, 1)
        self.btn_edit = QtWidgets.QPushButton(self.centralwidget)
        self.btn_edit.setStyleSheet("QPushButton {\n"
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
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("./src/ui/images/edit.svg"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.btn_edit.setIcon(icon3)
        self.btn_edit.setObjectName("btn_edit")
        self.gridLayout.addWidget(self.btn_edit, 4, 0, 1, 1)
        self.btn_delete = QtWidgets.QPushButton(self.centralwidget)
        self.btn_delete.setStyleSheet("QPushButton {\n"
"                background: #d16969; \n"
"                color: #fff; \n"
"                font: Times New Roman; \n"
"                font-size: 12px; \n"
"                font-weight: 700; \n"
"                border-radius: 5px; \n"
"                height: 30px;\n"
"            }\n"
"\n"
"            QPushButton:hover {\n"
"                background: #cf8686;\n"
"            }")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("./src/ui/images/delete.svg"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.btn_delete.setIcon(icon4)
        self.btn_delete.setObjectName("btn_delete")
        self.gridLayout.addWidget(self.btn_delete, 5, 0, 1, 1)
        self.layoutSearch = QtWidgets.QHBoxLayout()
        self.layoutSearch.setObjectName("layoutSearch")
        self.lineSearch = QtWidgets.QLineEdit(self.centralwidget)
        self.lineSearch.setStyleSheet("QLineEdit {\n"
"                background: white;\n"
"                height: 25px;\n"
"                border: 1px solid #474747;\n"
"                border-radius: 2px;\n"
"                font-size: 14px;\n"
"                font: sans-serif;\n"
"            }\n"
"            QLineEdit:focus {\n"
"                border: 1px solid #23a5c2;\n"
"            }")
        self.lineSearch.setObjectName("lineSearch")
        self.layoutSearch.addWidget(self.lineSearch)
        self.toolFilter = QtWidgets.QToolButton(self.centralwidget)
        self.toolFilter.setStyleSheet("QToolButton {\n"
"                background: #76afcc; \n"
"                color: #fff; \n"
"                font: Times New Roman; \n"
"                font-size: 12px; \n"
"                font-weight: 700; \n"
"                border-radius: 5px; \n"
"                height: 20px;\n"
"                width: 100%;\n"
"                padding: 0 15px;\n"
"            }\n"
"\n"
"            QToolButton:hover {\n"
"                background: #81b2eb;\n"
"            }")
        self.toolFilter.setPopupMode(QtWidgets.QToolButton.MenuButtonPopup)
        self.toolFilter.setObjectName("toolFilter")
        self.layoutSearch.addWidget(self.toolFilter)
        self.btn_search = QtWidgets.QPushButton(self.centralwidget)
        self.btn_search.setStyleSheet("QPushButton {\n"
"                background: #3C8FBC; \n"
"                color: #fff; \n"
"                font: Times New Roman; \n"
"                font-size: 12px; \n"
"                font-weight: 700; \n"
"                border-radius: 5px; \n"
"                height: 25px;\n"
"                padding: 0 10px;\n"
"            }\n"
"\n"
"            QPushButton:hover {\n"
"                background: #81b2eb;\n"
"            }")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("./src/ui/images/search.svg"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.btn_search.setIcon(icon5)
        self.btn_search.setObjectName("btn_search")
        self.layoutSearch.addWidget(self.btn_search)
        self.gridLayout.addLayout(self.layoutSearch, 1, 0, 1, 3)
        self.table = QtWidgets.QTableWidget(self.centralwidget)
        self.table.setStyleSheet("font: 11pt arial;\n"
"color: #434343;\n"
"font-weight: 450;\n"
"alternate-background-color: rgb(232, 232, 232);\n"
"\n"
"")
        self.table.setLineWidth(1)
        self.table.setAlternatingRowColors(True)
        self.table.setGridStyle(QtCore.Qt.SolidLine)
        self.table.setRowCount(5)
        self.table.setColumnCount(5)
        self.table.setObjectName("table")
        self.table.horizontalHeader().setVisible(True)
        self.table.horizontalHeader().setCascadingSectionResizes(False)
        self.table.horizontalHeader().setDefaultSectionSize(150)
        self.table.horizontalHeader().setHighlightSections(True)
        self.table.verticalHeader().setVisible(False)
        self.table.verticalHeader().setMinimumSectionSize(23)
        self.gridLayout.addWidget(self.table, 3, 0, 1, 3)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 4, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Produtos"))
        self.btn_cad.setText(_translate("MainWindow", "Novo produto"))
        self.btn_refresh.setText(_translate("MainWindow", "Atualizar"))
        self.btn_edit.setText(_translate("MainWindow", "Editar"))
        self.btn_delete.setText(_translate("MainWindow", "Excluir"))
        self.toolFilter.setText(_translate("MainWindow", "Filtros"))
        self.btn_search.setText(_translate("MainWindow", "Pesquisar"))
        self.table.setSortingEnabled(False)
