from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton

class addFlightWidget(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('widget.ui', self)

    def setupUI(self):
        