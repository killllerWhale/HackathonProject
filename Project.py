import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QMessageBox

import test
from mydesign import Ui_MainWindow
from test import Vector



class Book(QMainWindow):
    def __init__(self):
        super(Book, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.vector = Vector()
        self.start()
        self.checkin_completion = 0

    def start(self):
        self.vector.parsi()
        self.ui.pushButton.clicked.connect(lambda:self.text_searche())

    def text_searche(self):
        text = self.ui.textEdit.toPlainText()
        print(self.vector.similarity(text))
        self.ui.textEdit.setText("")


if __name__ == '__main__':
    app = QApplication([])
    application = Book()
    application.show()
    sys.exit(app.exec())