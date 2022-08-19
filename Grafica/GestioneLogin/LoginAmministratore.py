# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Lenovo\Desktop\University\MATERIE\2°ANNO 2° SEMESTRE\INGEGNERIA DEL SOFTWARE\Mockup\LoginAmministratore.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

from Amministratore.Amministratore import Amministratore


class LoginAmministratore(object):

    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(484, 333)
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        Frame.setFont(font)
        Frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit = QtWidgets.QLineEdit(Frame)
        self.lineEdit.setGeometry(QtCore.QRect(20, 150, 451, 31))
        self.lineEdit.setStyleSheet("border: 1px solid black;\n"
                                    "border-radius: 10px;")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(20, 220, 451, 31))
        self.lineEdit_2.setStyleSheet("border: 1px solid black;\n"
                                      "border-radius: 10px;")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label = QtWidgets.QLabel(Frame)
        self.label.setGeometry(QtCore.QRect(20, 120, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Frame)
        self.label_2.setGeometry(QtCore.QRect(20, 190, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Frame)
        self.label_3.setGeometry(QtCore.QRect(180, 10, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.line = QtWidgets.QFrame(Frame)
        self.line.setGeometry(QtCore.QRect(40, 50, 391, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_4 = QtWidgets.QLabel(Frame)
        self.label_4.setGeometry(QtCore.QRect(50, 70, 371, 31))
        self.label_4.setStyleSheet("border: 1px solid black;\n"
                                   "border-radius:10px;")
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(Frame)
        self.pushButton.setGeometry(QtCore.QRect(20, 270, 451, 41))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton{border: 2px solid black; border-radius: 10px;}QPushButton:hover{background-color: #14626c;color:white;}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.clickButton)
        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Fumetteria"))
        self.label.setText(_translate("Frame", "USERNAME:"))
        self.label_2.setText(_translate("Frame", "PASSWORD:"))
        self.label_3.setText(_translate("Frame", "FUMETTERIA"))
        self.label_4.setText(
            _translate("Frame", "Iserisci le credenziali per effettuare il login e iniziare ad utilizzare il programma"))
        self.pushButton.setText(_translate("Frame", "Login"))

    def clickButton(self):
        amministratore = Amministratore()

        nomeUtente = self.lineEdit.text()
        password = self.lineEdit_2.text()

        if amministratore.controlloCredenziali(nomeUtente, password):
            print("T")
            #   compare la finestra per la gestione della fumetteria
            return True

        else:
            self.ErrorMessage()
            print("F")
            return False

    def ErrorMessage(self):
        self.ErrorBox = QMessageBox()
        self.ErrorBox.setWindowTitle("Errore")
        self.ErrorBox.setText("Email o password errati")
        self.ErrorBox.setStyleSheet("QLabel{min-width:200 px; font-size: 16px; font-family: Helvetica, Sans-Serif; } QPushButton:hover{background-color: #14626c;color:white; }QPushButton{ width:40px; height:20px; font-size: 10px; font-family: Helvetica, Sans-Serif; border: 1px solid black; border-radius: 5px; }")
        self.ErrorBox.exec()




