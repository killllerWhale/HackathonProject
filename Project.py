import sys

from PyQt5 import QtWidgets, QtCore
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
        self.widget = QtWidgets.QWidget()
        self.vbox = QtWidgets.QVBoxLayout()
        self.ui.scrollAreaWidgetContents.setLayout(self.vbox)
        self.ui.scrollArea.verticalScrollBar().update()

    def start(self):
        self.vector.parsi()
        self.ui.pushButton.clicked.connect(lambda:self.text_searche())

    def text_searche(self):
        text = self.ui.textEdit.toPlainText()
        self.ui.textEdit.setText("")
        reternn = self.vector.similarity(text)
        self.ui.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        print(reternn)
        for i in range(len(reternn)):
            textlabel = self.vector.book_name[reternn[i][0]]
            textlabel2 = self.vector.book_desc_norm[reternn[i][0]]
            textPrecent = int(reternn[i][1])
            label = QtWidgets.QLabel(textlabel+"  (совпадение: " + str(textPrecent*100) + "%)")
            label.setStyleSheet('color: rgb(4, 53, 185); font: bold 18px;')
            label5 = QtWidgets.QLabel("(совпадение: " + str(textPrecent*100) + "%)")
            label5.setStyleSheet('color: rgb(4, 53, 185); font: bold 6px;')
            label4 = QtWidgets.QLabel()
            label4.setMinimumHeight(3)
            label2 = QtWidgets.QLabel(textlabel2)
            label2.setStyleSheet('color: rgb(86, 111, 178); font: bold 13px;')
            label2.setMinimumHeight(48)
            label3 = QtWidgets.QLabel()
            label3.setMinimumHeight(8)
            if len(textlabel) >= 40:
                label.setWordWrap(True)
            if len(textlabel2) >= 40:
                label2.setWordWrap(True)

            self.vbox.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
            self.vbox.addWidget(label)
            self.vbox.addWidget(label5)
            self.vbox.addWidget(label4)
            self.vbox.addWidget(label2)
            self.vbox.addWidget(label3)
            self.vbox.update()

        # for i in range(len(sims)):
        #     print("----------")
        #     print(self.book_name[sims[i][0]], end="\n")
        #     print(self.book_desc_norm[sims[i][0]], end="\n")
        #     print("----------")



if __name__ == '__main__':
    app = QApplication([])
    application = Book()
    application.show()
    sys.exit(app.exec())