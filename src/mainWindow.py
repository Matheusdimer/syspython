from src.ui.main import Ui_MainWindow
from src.ui.cadastro import Ui_MainWindow2
from PyQt5 import QtWidgets, QtCore, QtGui
from src.banco import Banco
from src.ui.msg import Ui_Form
from src.ui.msgYesNo import Ui_Msg
from src.ui.venda import Ui_form_venda
from src.recibo import gerarRecibo
from datetime import date
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
        self.btn_sale.clicked.connect(self.newSale)

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
                        self.item.setTextAlignment(QtCore.Qt.AlignRight + QtCore.Qt.AlignVCenter)
                    else:
                        self.item.setTextAlignment(QtCore.Qt.AlignLeft + QtCore.Qt.AlignVCenter)
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

    def newSale(self):
        self.rows = 1
        self.saleWindow = QtWidgets.QWidget()
        self.uiSale = Ui_form_venda()
        self.uiSale.setupUi(self.saleWindow)
        self.saleWindow.show()
        self.uiSale.btn_cancel.clicked.connect(self.saleWindow.close)
        self.uiSale.tableWidget.setRowCount(self.rows)
        self.uiSale.btn_add.clicked.connect(self.newLine)
        self.uiSale.btn_delete.clicked.connect(self.deletLine)
        self.uiSale.btn_search.clicked.connect(self.searchInformation)
        self.uiSale.btn_total.clicked.connect(self.countTotal)
        self.uiSale.tableWidget.horizontalHeader().setStyleSheet(
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
        self.resizeColumns_sale()
        self.uiSale.btn_finish.clicked.connect(self.genNota)
        self.count = 0
        self.uiSale.dateEdit.setDate(date.today())

    def resizeColumns_sale(self):
        self.uiSale.tableWidget.setColumnWidth(0, self.width() * (15/100))
        self.uiSale.tableWidget.setColumnWidth(1, self.width() * (31/100))
        self.uiSale.tableWidget.setColumnWidth(2, self.width() * (15/100))
        self.uiSale.tableWidget.setColumnWidth(3, self.width() * (15/100))
        self.uiSale.tableWidget.setColumnWidth(4, self.width() * (15/100) + 5)

    def newLine(self):
        self.rows += 1
        self.uiSale.tableWidget.setRowCount(self.rows)

    def deletLine(self):
        index = self.uiSale.tableWidget.selectedIndexes()[0]
        self.uiSale.tableWidget.removeRow(index.row())
        self.rows -= 1

    def searchInformation(self):
        count = self.uiSale.tableWidget.rowCount()
        for n in range(count):
            index = self.uiSale.tableWidget.item(n, 0).text()
            data = self.banco.consulta("Produtos", campo="CODIGO", pesquisa=index)
            if data:
                item = QtWidgets.QTableWidgetItem(f"{data[0][0]:0>4}")
                item.setTextAlignment(QtCore.Qt.AlignRight + QtCore.Qt.AlignVCenter)
                self.uiSale.tableWidget.setItem(n, 0, item)
                item = QtWidgets.QTableWidgetItem(str(data[0][1]))
                item.setTextAlignment(QtCore.Qt.AlignVCenter)
                self.uiSale.tableWidget.setItem(n, 1, item)
                item = QtWidgets.QTableWidgetItem(f"{data[0][2]:.2f}")
                item.setTextAlignment(QtCore.Qt.AlignRight + QtCore.Qt.AlignVCenter)
                self.uiSale.tableWidget.setItem(n, 2, item)
            else:
                self.msgInfo(f"Não há produto com o código {index:0>4}")

    def countTotal(self):
        self.count = self.uiSale.tableWidget.rowCount()
        total = 0
        for n in range(self.count):
            preco = self.uiSale.tableWidget.item(n, 2)
            if not preco:
                break
            preco = preco.text()
            quant = self.uiSale.tableWidget.item(n, 3)
            if not quant:
                break
            quant = quant.text()
            if not quant:
                self.msgInfo("Por favor, digite as quantidades!")
                break
            total_linha = float(preco) * float(quant)
            total += total_linha
            quant = QtWidgets.QTableWidgetItem(quant)
            quant.setTextAlignment(QtCore.Qt.AlignRight + QtCore.Qt.AlignVCenter)
            self.uiSale.tableWidget.setItem(n, 3, quant)
            total_linha = QtWidgets.QTableWidgetItem(f"{total_linha:.2f}")
            total_linha.setTextAlignment(QtCore.Qt.AlignRight + QtCore.Qt.AlignVCenter)
            self.uiSale.tableWidget.setItem(n, 4, total_linha)

        self.uiSale.line_total.setText(f"{total:.2f}")
        dinheiro = self.uiSale.lineMoney.text()
        if dinheiro:
            troco = float(dinheiro) - total
            self.uiSale.lineTroco.setText(f"{troco:.2f}")

    def genNota(self):
        try:
            date = self.uiSale.dateEdit.date().toPyDate().isoformat().replace("-", "/")
            cpf = self.uiSale.lineCPF.text()
            name = self.uiSale.lineNome.text()

            if not name:
                self.msgInfo("Campo Nome em branco!")
                return

            if not cpf or not cpf.isnumeric() or len(cpf) > 11:
                self.msgInfo("CPF inválido!\nLembre-se de digitar somente os 11 números.")
                return
            
            cabecalho = [
                name,
                f"{cpf[0:3]}.{cpf[3:7]}.{cpf[7:10]}-{cpf[10:12]}",
                date[8:10:1] + "/" + date[5:8:1] + date[0:4:1]
            ]

            produtos = []
            if self.count > 0:
                for n in range(self.count):
                    produtos.append([
                        self.uiSale.tableWidget.item(n, 0).text(),
                        self.uiSale.tableWidget.item(n, 1).text(),
                        float(self.uiSale.tableWidget.item(n, 2).text()),
                        int(self.uiSale.tableWidget.item(n, 3).text()),
                        float(self.uiSale.tableWidget.item(n, 4).text())
                    ])
            
            total = float(self.uiSale.line_total.text())

            if produtos and cabecalho and total:
                arquivo = cabecalho[2].replace("/", "_") + "-" + cabecalho[0].replace(" ", "_")
                gerarRecibo(arquivo, produtos, total, cabecalho=cabecalho)
        except:
            self.msgInfo("Falha ao gerar nota.")

    def openEdit(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow2()
        self.ui.setupUi(self.window)
        self.window.show()
        self.window.setWindowTitle("Editar produto existente")
        self.ui.btn_confirm.setText("Editar produto")
        self.ui.btn_confirm.clicked.connect(self.editReg)
        self.ui.btn_cancel.clicked.connect(self.window.close)

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
            self.window.close()
            self.dados()
        else:
            #self.labelinfo.setText("Erro ao cadastrar produto, verifique os campos.")
            self.msgInfo("Erro ao cadastrar produto, verifique os campos.")

    def search(self):
        self.lineBusca = self.lineSearch.text()
        self.dados(busca=self.lineBusca, coluna=self.filter)

    def edit(self):
        indexes = self.table.selectedIndexes()
        self.data = []
        for index in sorted(indexes):
            self.data.append(index.data())
        if len(self.data) > 0:
            self.openEdit()
            self.data[2] = self.data[2].replace("R$ ", "")
            self.ui.linecod.setText(self.data[0])
            self.ui.linedesc.setText(self.data[1])
            self.ui.linevalor.setText(self.data[2])
            self.ui.linetipo.setText(self.data[3])
            self.ui.linecod.setDisabled(True)
        else:
            self.msgInfo("Nenhuma linha selecionada!")

    def editReg(self):
        campo_dado = [
            ["CODIGO", self.ui.linecod.text()],
            ["DESCRICAO", self.ui.linedesc.text()],
            ["VALOR_UNIT", self.ui.linevalor.text().replace(",", ".")],
            ["TIPO", self.ui.linetipo.text()]
        ]
        if self.banco.update("Produtos", self.data[0], campo_dado):
            self.msgInfo("Produto alterado com sucesso!")
            self.window.close()
            self.dados()
        else:
            self.msgInfo("Erro ao alterar registro.")

    def delete(self):
        indexes = self.table.selectedIndexes()
        if len(indexes) > 0:
            if len(indexes) == 4:
                self.codigo = indexes[0].data()
                self.msgYesNo(f"Deseja realmente excluir o produto {self.codigo}?")
            else:
                self.msgInfo("Selecione apenas uma linha por vez.")
        else:
            self.msgInfo("Nenhuma linha selecionada!")

    def delRegis(self):
        if self.banco.delete("Produtos", self.codigo):
            self.msgInfo(f"Produto {self.codigo} deletado com sucesso!")
            self.dados()
            self.yesNo_window.close()
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

    def msgYesNo(self, texto):
        self.yesNo_window = QtWidgets.QWidget()
        self.uiYesNo = Ui_Msg()
        self.uiYesNo.setupUi(self.yesNo_window)
        self.uiYesNo.label.setText(texto)
        self.yesNo_window.show()
        self.uiYesNo.label.setAlignment(QtCore.Qt.AlignCenter)
        self.uiYesNo.btn_no.clicked.connect(self.yesNo_window.close)
        self.uiYesNo.btn_yes.clicked.connect(self.delRegis)
        
