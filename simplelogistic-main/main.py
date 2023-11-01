import sys
import sqlite3
from pathlib import Path
from sys import argv



from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QDialog, QTableWidgetItem

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        script_dir = Path(argv[0]).parent.resolve()

        # Подключение .ui файлов
        uic.loadUi(script_dir / 'main.ui', self)

        # Подключение к базе данных
        db_path = script_dir / 'flightsDB.sqlite'
        self.con = sqlite3.connect(db_path)

        # Подключение обработчиков
        self.addNote.clicked.connect(self.selectData)
        # self.sortComboBox.currentTextChanged.connect(self.sortComboBoxChanged)

        self.tableWidget.setSortingEnabled(True)

        self.selectData()

    def selectData(self):
        query = "SELECT departurePoint, departureDate, arrivalPoint, arrivalDate, price, downtime, driversFullName, " \
                "driversSalary, driversDowntime, fuelConsumption, additionalExpenses FROM flights"
        res = self.con.cursor().execute(query).fetchall()
        title = ['Дата загрузки', 'Дата выгрузки', 'Точка загрузки',  'Точка выгрузки',
                 'Цена загрузки', 'Простой\nзагрузки', 'ФИО водителя', 'Зарплата\nводителя',
                 'Простой водителя', 'Траты на бензин', 'Дополнительные\nтраты']
        self.tableWidget.setColumnCount(len(title))
        self.tableWidget.setRowCount(0)

        self.tableWidget.setHorizontalHeaderLabels(title)
        for i, row in enumerate(res):
            self.tableWidget.setRowCount(
                self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableWidget.setItem(
                    i, j, QTableWidgetItem(str(elem)))
        self.tableWidget.resizeColumnsToContents()

    def deleteWidget(self):
        self.delete.emit(self.id_widget)

    def addNoteWidget(self):
        '''self.newWidget = QPushButton(self)
        self.flightLayout.addWidget(self.newWidget)'''
        pass

    '''def sortComboBoxChanged(self):
        text = self.sortComboBox.currentText()
        if text == 'Дате: ближайшие':
            print('Дате: ближайшие')
        elif text == 'Дате: дальнейшие':
            print('дальнейшие')
        elif text == 'Прибыль 🠕':
            print('Прибыль 🠕')
        elif text == 'Прибыль 🠗':
            print('Прибыль 🠗')'''


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MainWindow()
    form.setFixedSize(1540, 640)
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())