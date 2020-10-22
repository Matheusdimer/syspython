from main import Ui_MainWindow
from cadastro import Ui_MainWindow2
from PyQt5 import QtWidgets
import sys

class Lista(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

qt = QtWidgets.QApplication([])
app = Lista()
app.show()
qt.exec_()

