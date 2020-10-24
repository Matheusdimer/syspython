from src.ui.main import Ui_MainWindow
from src.ui.cadastro import Ui_MainWindow2
from PyQt5 import QtWidgets, QtCore, QtGui
from src.banco import Banco
from src.ui.msg import Ui_Form
import sys

class mainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.banco = Banco("./src/database/dados.db")
        self.btn_cad.clicked.connect(self.openCad)
        self.btn_edit.clicked.connect(self.edit)
        self.btn_delete.clicked.connect(self.delete)
        self.table.horizontalHeader().setStyleSheet(
        """
        QHeaderView::section {
            background-color: #2e85db; 
            font: 14px arial; 
            font-weight: 600; 
            color: white; 
            border: none; 
            border-right: 1px solid #949494
        }
        """
        )
        self.table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)

        self.filter = "CODIGO"
        self.toolFilter.setText("Filtro: Código")

        codigo = QtWidgets.QAction(text="Código", parent=self.toolFilter)
        codigo.triggered.connect(self.setFilterCod)
        self.toolFilter.addAction(codigo)
        
        desc = QtWidgets.QAction(text="Descrição", parent=self.toolFilter)
        desc.triggered.connect(self.setFilterDesc)
        self.toolFilter.addAction(desc)

        tipo = QtWidgets.QAction(text="Tipo", parent=self.toolFilter)
        tipo.triggered.connect(self.setFilterTipo)
        self.toolFilter.addAction(tipo)

        self.table.setHorizontalHeaderLabels(["Código", "Descrição", "Valor Unitário", "Tipo"])

        self.btn_search.clicked.connect(self.search)
        self.btn_refresh.clicked.connect(self.dados)

        self.table.verticalHeader().setVisible(False)
        self.dados()
        self.resizeColumns()

    def resizeColumns(self):
        self.table.setColumnWidth(0, self.width() * (10/100))
        self.table.setColumnWidth(1, self.width() * (40/100))
        self.table.setColumnWidth(2, self.width() * (20/100))
        self.table.setColumnWidth(3, self.width() * (30/100) - 37)

    def resizeEvent(self, QResizeEvent):
        self.resizeColumns()

    def dados(self, coluna="", busca=""):
        self.result = self.banco.consulta("Produtos", pesquisa=busca, campo=coluna)
        self.row = len(self.result)
        if self.row > 0:
            self.collumn = len(self.result[0])
            self.table.setRowCount(0)
            self.table.setColumnCount(self.collumn)
            self.table.setHorizontalHeaderLabels(["Código", "Descrição", "Valor Unitário", "Tipo"])
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
        else:
            self.table.setRowCount(0)
            self.msgInfo("Pesquisa sem resultados.")


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
            self.ui.linecod.text(),
            self.ui.linedesc.text(),
            self.ui.linevalor.text(),
            self.ui.linetipo.text()
        ]
        self.data[2] = self.data[2].replace(",", ".")
        if self.banco.cadastro("Produtos", self.data):
            #self.labelinfo.setText(f"Produto {self.dados[0]:0>2}: {self.dados[1]} cadastrado com sucesso!")
            self.msgInfo(f"Produto cadastrado com sucesso!")
        else:
            #self.labelinfo.setText("Erro ao cadastrar produto, verifique os campos.")
            self.msgInfo("Erro ao cadastrar produto, verifique os campos.")

    def search(self):
        self.lineBusca = self.lineSearch.text()
        self.dados(busca=self.lineBusca, coluna=self.filter)

    def edit(self):
        indexes = self.table.selectedIndexes()
        for index in sorted(indexes):
            data = index.data()
            print(data)

    def delete(self):
        indexes = self.table.selectedIndexes()
        codigo = indexes[0].data()
        if self.banco.delete("Produtos", codigo):
            self.msgInfo(f"Produto {codigo} deletado com sucesso!")
            self.dados()
        else:
            self.msgInfo("Erro ao tentar deletar registro.")

    def setFilterTipo(self):
        self.toolFilter.setText("Filtro: Tipo")
        self.filter = "TIPO"

    def setFilterDesc(self):
        self.toolFilter.setText("Filtro: Descrição")
        self.filter = "DESCRICAO"

    def setFilterCod(self):
        self.toolFilter.setText("Filtro: Código")
        self.filter = "CODIGO"


    def msgInfo(self, text):
        self.aviso = QtWidgets.QWidget()
        self.interface = Ui_Form()
        self.interface.setupUi(self.aviso)
        self.aviso.show()
        self.interface.label.setAlignment(QtCore.Qt.AlignCenter)
        self.interface.label.setText(text)
        self.interface.bntExit.clicked.connect(self.aviso.close)
