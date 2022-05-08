import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QMessageBox
from mydesign import Ui_MainWindow


class Book(QMainWindow):
    def __init__(self):
        super(Book, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.start()
        self.checkin_completion = 0

    def start(self):
        pass

if __name__ == '__main__':
    app = QApplication([])
    application = Book()
    application.show()
    sys.exit(app.exec())