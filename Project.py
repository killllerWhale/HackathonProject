import sys

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox

from mydesign import Ui_MainWindow
from test import Vector


class Book(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.vector = Vector()
        self.start()
        self.checkin_completion = 0
        self.widget = QtWidgets.QWidget()
        self.vbox = QtWidgets.QVBoxLayout()
        self.ui.scrollAreaWidgetContents.setLayout(self.vbox)
        self.ui.scrollArea.verticalScrollBar().update()
        self.ui.textEdit.textChanged.connect(lambda:self.enter())

    def start(self):
        self.vector.parsi()
        self.ui.pushButton.clicked.connect(lambda: self.text_searche())

    def enter(self):
        if self.ui.textEdit.toPlainText() == "\n":
            msg = QMessageBox()
            msg.setWindowTitle("Ошибка")
            msg.setText("Введите описание книги! ")
            msg.setIcon(QMessageBox.Warning)
            msg.exec_()
        elif "\n" in self.ui.textEdit.toPlainText():
            self.text_searche()

    def clearvbox(self, L=False):
        if not L:
            L = self.vbox
        if L is not None:
            while L.count():
                item = L.takeAt(0)

                widget = item.widget()

                if widget is not None:
                    widget.deleteLater()
                else:
                    self.clearvbox(item.layout())

    def text_searche(self):
        try:
            self.clearvbox()
            text = self.ui.textEdit.toPlainText()
            self.ui.textEdit.setText("")
            reternn = self.vector.similarity(text)
            self.ui.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
            for i in range(len(reternn)):
                textPrecent = int(reternn[i][1] * 100)
                textlabel = self.vector.book_name[reternn[i][0]] +"  (совпадение: " + str(textPrecent) + "%)"
                textlabel2 = self.vector.book_desc_norm[reternn[i][0]]
                label = QtWidgets.QLabel(textlabel)
                label.setMaximumWidth(460)
                label.setMinimumHeight(4)
                label.setStyleSheet('color: rgb(4, 53, 185); font: bold 18px;')
                label2 = QtWidgets.QLabel(textlabel2)
                label2.setStyleSheet('color: rgb(86, 111, 178); font: bold 13px;')
                label2.setMinimumHeight(60)
                label2.setMaximumWidth(460)
                label3 = QtWidgets.QLabel()
                label3.setMinimumHeight(8)
                if len(textlabel) >= 40:
                    label.setWordWrap(True)
                    label3.setWordWrap(True)
                if len(textlabel2) >= 40:
                    label2.setWordWrap(True)
                    label3.setWordWrap(True)

                self.vbox.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
                self.vbox.addWidget(label)
                self.vbox.addWidget(label2)
                self.vbox.addWidget(label3)
                self.vbox.update()

        except Exception as e:
            msg = QMessageBox()
            msg.setWindowTitle("Ошибка")
            msg.setText("Что то пошло не так ")
            msg.setIcon(QMessageBox.Warning)
            msg.exec_()


if __name__ == '__main__':
    app = QApplication([])
    application = Book()
    application.show()
    sys.exit(app.exec())