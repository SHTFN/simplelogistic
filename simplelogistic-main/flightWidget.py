from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton

class flightWidget(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('C:/Users/Albu_S/PycharmProjects/pythonProject/Simple Logstics/simplelogistic-main/widget.ui', self)

    def setupUi(self, widget):
        print(123)
        