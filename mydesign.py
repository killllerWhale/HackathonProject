# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 750)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        MainWindow.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(0, 50, 400, 50))
        self.textEdit.setStyleSheet("")
        self.textEdit.setPlaceholderText(" Введите описание книги...")
        self.textEdit.setObjectName("textEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 500, 50))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(400, 50, 100, 50))
        self.pushButton.setStyleSheet("background-color: rgb(85, 109, 236);\n"
"color: rgb(255, 255, 255);\n"
"font: 16pt \"MingLiU-ExtB\";")
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 100, 501, 41))
        self.label_2.setStyleSheet("background-color: rgb(232, 232, 232);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(0, 150, 501, 101))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(0, 470, 501, 101))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(0, 420, 501, 41))
        self.label_5.setStyleSheet("background-color: rgb(232, 232, 232);")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(0, 260, 501, 41))
        self.label_6.setStyleSheet("background-color: rgb(232, 232, 232);")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(0, 310, 501, 101))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(0, 630, 500, 101))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(0, 580, 500, 41))
        self.label_9.setStyleSheet("background-color: rgb(232, 232, 232);")
        self.label_9.setObjectName("label_9")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "BookFinder"))
        self.label.setText(_translate("MainWindow", "BookFinder"))
        self.pushButton.setText(_translate("MainWindow", "найти"))
        self.label_2.setText(_translate("MainWindow", " книга 1"))
        self.label_3.setText(_translate("MainWindow", " описание"))
        self.label_4.setText(_translate("MainWindow", " описание"))
        self.label_5.setText(_translate("MainWindow", " книга 3"))
        self.label_6.setText(_translate("MainWindow", " книга 2"))
        self.label_7.setText(_translate("MainWindow", " описание"))
        self.label_8.setText(_translate("MainWindow", " описание"))
        self.label_9.setText(_translate("MainWindow", " книга 4"))