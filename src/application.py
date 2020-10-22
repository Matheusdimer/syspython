from mainWindow import mainWindow
from PyQt5 import QtWidgets

if __name__ == "__main__":
    qt = QtWidgets.QApplication([])
    app = mainWindow()
    app.show()
    qt.exec_()