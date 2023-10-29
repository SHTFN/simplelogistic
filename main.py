import sys
import sqlite3

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QDialog
from flightWidget import addFlightWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui.ui', self)
        self.addNote.clicked.connect(self.addNoteWidget)

    def deleteWidget(self):
        self.delete.emit(self.id_widget)

    def addNoteWidget(self):
        '''self.newWidget = QPushButton(self)
        self.flightLayout.addWidget(self.newWidget)'''
        widget = QDialog()
        ui = addFlightWidget()
        ui.setupUi(widget)
        widget.exec()





def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MainWindow()
    form.setFixedSize(880, 550)
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())