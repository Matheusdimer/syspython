from ui.main import Ui_MainWindow
from ui.cadastro import Ui_MainWindow2
from PyQt5 import QtWidgets, QtCore
from banco import Banco
from ui.msg import Ui_Form
import sys

class mainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.btn_cad.clicked.connect(self.openCad)
        self.btn_cad.setStyleSheet("""
            QPushButton {
                background: #61AB6D; 
                color: #fff; 
                font: Times New Roman; 
                font-size: 14px; 
                font-weight: 700; 
                border-radius: 5px; 
                height: 30px;
            }

            QPushButton:hover {
                background: #72bd6c;
            }
            """
        )
        self.table.setStyleSheet(
            """
                QTableView {
                    background: white;
                    color: #292929;
                    font-size: 16px;
                    font: arial;
                    font-weight: 400;
                }
            """
        )
        self.btn_refresh.setStyleSheet(
            """
            QPushButton {
                background: #3C8FBC; 
                color: #fff; 
                font: Times New Roman; 
                font-size: 14px; 
                font-weight: 700; 
                border-radius: 5px; 
                height: 30px
            }

            QPushButton:hover {
                background: #81b2eb;
            }
            """
        )
        self.dados()
        
    def openCad(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow2()
        self.ui.setupUi(self.window)
        self.window.show()
        self.ui.btn_cancel.clicked.connect(self.window.close)
        self.window.setWindowTitle("Cadastro de novo Produto")
        self.ui.btn_confirm.clicked.connect(self.insert)

        self.ui.btn_confirm.setStyleSheet("""
            QPushButton {
                background: #61AB6D; 
                color: #fff; 
                font: Times New Roman; 
                font-size: 14px; 
                font-weight: 700; 
                border-radius: 5px; 
                height: 30px;
            }

            QPushButton:hover {
                background: #72bd6c;
            }
            """
        )

        self.ui.btn_cancel.setStyleSheet("""
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

    def insert(self):
        self.data = [
            self.linecod.text(),
            self.linedesc.text(),
            self.linevalor.text(),
            self.linetipo.text()
        ]
        self.data[2] = self.data[2].replace(",", ".")
        insere = Banco("./src/database/dados.db")
        if insere.cadastro("Produtos", self.data):
            #self.labelinfo.setText(f"Produto {self.dados[0]:0>2}: {self.dados[1]} cadastrado com sucesso!")
            self.msgInfo(f"Produto cadastrado com sucesso!")
        else:
            #self.labelinfo.setText("Erro ao cadastrar produto, verifique os campos.")
            self.msgInfo("Erro ao cadastrar produto, verifique os campos.")

    def msgInfo(self, text):
        self.aviso = QtWidgets.QWidget()
        self.interface = Ui_Form()
        self.interface.setupUi(self.aviso)
        self.aviso.show()
        self.interface.label.setAlignment(QtCore.Qt.AlignCenter)
        self.interface.label.setText(text)
        self.interface.bntExit.clicked.connect(self.aviso.close)

    def dados(self):
        banco = Banco("./src/database/dados.db")
        self.result = banco.consulta("Produtos")
        self.collumn = len(self.result[0])
        self.row = len(self.result)
        self.table.setRowCount(0)
        self.table.setColumnCount(self.collumn)
        self.table.setHorizontalHeaderLabels(["Código", "Descrição", "Valor Unitário", "Tipo"])
        self.table.setColumnWidth(0, 60)
        self.table.setColumnWidth(1, 380)
        self.table.setColumnWidth(2, 120)
        for row_number, row_data in enumerate(self.result):
            self.table.insertRow(row_number)
            for collumn_number, data in enumerate(row_data):
                
                if collumn_number == 2:
                    valor = (f"R$ {data:.2f}")
                    self.item = QtWidgets.QTableWidgetItem(str(valor).replace(".", ","))
                elif collumn_number == 0:
                    valor = (f"{data:0>4}")
                    self.item = QtWidgets.QTableWidgetItem(str(valor))
                else:
                    self.item = QtWidgets.QTableWidgetItem(str(data))
                if collumn_number == 0 or collumn_number == 2:
                    self.item.setTextAlignment(QtCore.Qt.AlignRight)
                else:
                    self.item.setTextAlignment(QtCore.Qt.AlignLeft)
                self.table.setItem(row_number, collumn_number, self.item)

