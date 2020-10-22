from main import *
from cadastro import *
import sys

class Lista(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

qt = QApplication([])
app = Lista()
app.show()
qt.exec_()

