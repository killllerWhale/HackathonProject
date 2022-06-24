import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from mydesign import Ui_MainWindow
import pyrebase
import re
import urllib.request
from gensim.models.doc2vec import Doc2Vec
import pymorphy2


config = {
    "apiKey": "AIzaSyBNnLM1ItodpQFU8jvkwuYOniyQ97VZADA",
    "authDomain": "bookfinder-97299.firebaseapp.com",
    "databaseURL": "https://bookfinder-97299-default-rtdb.europe-west1.firebasedatabase.app",
    "projectId": "bookfinder-97299",
    "storageBucket": "bookfinder-97299.appspot.com",
    "messagingSenderId": "1079515581653",
    "appId": "1:1079515581653:web:57e569b2c6e82161e9265c",
    "measurementId": "G-V8NT67P272"
}

firebase = pyrebase.initialize_app(config)

login = "ruslan@gmail.com"
password = "12345678"

auth = firebase.auth()
auth.sign_in_with_email_and_password(login, password)

db = firebase.database()


class Vector:
    def __init__(self):
        logo = urllib.request.urlopen("https://drive.google.com/u/0/uc?id=1sMGmBQGyy4ZH1rIcMzL8Tymi6_WAYVF_&export=download").read()
        f = open("d2v_Model_new", "wb")
        f.write(logo)
        f.close()

    def pos(self,word, morth=pymorphy2.MorphAnalyzer()):
        return morth.parse(word)[0].tag.POS

    def similarity(self, text):
        d2v_model = Doc2Vec.load('d2v_Model_new')
        test_text = text.lower().split()
        functors_pos = {'INTJ', 'PRCL', 'CONJ', 'PREP'}
        s = [word for word in test_text if self.pos(word) not in functors_pos]
        result = ""
        for i in range(len(s)):
            result += s[i] + " "
        result = re.sub('[^a-zA-ZА-я]', ' ', result)
        result = result.replace("  ", " ")
        result = result.replace("   ", " ")
        result = result.replace("    ", " ")
        result = result.replace("     ", " ")
        result = result.replace("      ", " ")
        result = result.lower().split()
        inferred_vector = d2v_model.infer_vector(result)
        sims = d2v_model.dv.most_similar([inferred_vector], topn=10)
        return sims


class Book(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.start()
        self.checkin_completion = 0
        self.widget = QtWidgets.QWidget()
        self.vbox = QtWidgets.QVBoxLayout()
        self.ui.scrollAreaWidgetContents.setLayout(self.vbox)
        self.ui.scrollArea.verticalScrollBar().update()
        self.ui.textEdit.textChanged.connect(lambda:self.enter())

    def start(self):
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
        vector = Vector()
        try:
            self.clearvbox()
            text = self.ui.textEdit.toPlainText()
            self.ui.textEdit.setText("")
            reternn = vector.similarity(text)
            self.ui.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
            for i in range(len(reternn)):
                textPrecent = int(reternn[i][1] * 100)
                name = db.child(reternn[i][0]).child("col1").get().val()
                desc = db.child(reternn[i][0]).child("col2").get().val()
                textlabel = name + "  (совпадение: " + str(textPrecent) + "%)"
                textlabel2 = desc
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
            print(e)


if __name__ == '__main__':
    app = QApplication([])
    application = Book()
    application.show()
    sys.exit(app.exec())