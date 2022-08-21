# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Lenovo\Desktop\University\MATERIE\2°ANNO 2° SEMESTRE\INGEGNERIA DEL SOFTWARE\Mockup\RicercaProdotto.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

from GestioneMagazzino.Magazzino import Magazzino


class RicercaProdotto(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(387, 258)
        Frame.setStyleSheet("QFrame{\n"
                            "background-color: rgb(255, 255, 255);\n"
                            "}")
        Frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame = Frame
        self.label = QtWidgets.QLabel(Frame)
        self.label.setGeometry(QtCore.QRect(10, 70, 391, 31))
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setStyleSheet("QLabel{\n"
                                 "font-family: Helvetica, sans-serif;\n"
                                 "font-weight: 400;\n"
                                 "font-size: 16px\n"
                                 "}")
        self.label.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.lineEditCodiceSeriale = QtWidgets.QLineEdit(Frame)
        self.lineEditCodiceSeriale.setGeometry(QtCore.QRect(10, 100, 371, 31))
        self.lineEditCodiceSeriale.setStyleSheet("QLineEdit{\n"
                                    "border: 2px solid black;\n"
                                    "border-radius: 6px;\n"
                                    "}")
        self.lineEditCodiceSeriale.setObjectName("lineEdit")
        self.label_4 = QtWidgets.QLabel(Frame)
        self.label_4.setGeometry(QtCore.QRect(20, 20, 381, 31))
        self.label_4.setStyleSheet("QLabel{\n"
                                   "font-family: impact, sans-serif;\n"
                                   "font-size:30px;\n"
                                   "\n"
                                   "}")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.line = QtWidgets.QFrame(Frame)
        self.line.setGeometry(QtCore.QRect(50, 50, 311, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.pushButtonLogout = QtWidgets.QPushButton(Frame)
        self.pushButtonLogout.setGeometry(QtCore.QRect(10, 220, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonLogout.setFont(font)
        self.pushButtonLogout.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButtonLogout.setStyleSheet("QPushButton{\n"
                                        "border: 2px solid black;\n"
                                        "border-radius: 10px;\n"
                                        "}\n"
                                        "QPushButton:hover{\n"
                                        "\n"
                                        "background-color: #14626c;\n"
                                        "color:white;\n"
                                        "}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(
            "Images\\log.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonLogout.setIcon(icon)
        self.pushButtonLogout.setCheckable(False)
        self.pushButtonLogout.setObjectName("pushButton_5")
        self.pushButtonRicerca = QtWidgets.QPushButton(Frame)
        self.pushButtonRicerca.setGeometry(QtCore.QRect(10, 150, 371, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonRicerca.setFont(font)
        self.pushButtonRicerca.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButtonRicerca.setStyleSheet("QPushButton{\n"
                                        "border: 2px solid black;\n"
                                        "border-radius: 10px;\n"
                                        "}\n"
                                        "QPushButton:hover{\n"
                                        "\n"
                                        "background-color: #14626c;\n"
                                        "color:white;\n"
                                        "}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(
            "Images\\magnifying-glass.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonRicerca.setIcon(icon1)
        self.pushButtonRicerca.setCheckable(False)
        self.pushButtonRicerca.setObjectName("pushButton_6")
        self.pushButtonGestioneMagazzino = QtWidgets.QPushButton(Frame)
        self.pushButtonGestioneMagazzino.setGeometry(QtCore.QRect(160, 220, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonGestioneMagazzino.setFont(font)
        self.pushButtonGestioneMagazzino.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButtonGestioneMagazzino.setStyleSheet("QPushButton{\n"
                                        "border: 2px solid black;\n"
                                        "border-radius: 10px;\n"
                                        "}\n"
                                        "QPushButton:hover{\n"
                                        "\n"
                                        "background-color: #14626c;\n"
                                        "color:white;\n"
                                        "}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(
            "Images\\left.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonGestioneMagazzino.setIcon(icon2)
        self.pushButtonGestioneMagazzino.setObjectName("pushButton_4")
        self.pushButtonGestioneMagazzino.clicked.connect(self.openGestioneMagazzino)
        self.pushButtonLogout.clicked.connect(self.openLogin)
        self.pushButtonRicerca.clicked.connect(self.clickRicerca)

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Fumetteria - Modifica Nome Utente"))
        self.label.setText(_translate("Frame", "Inserisci il codice del prodotto da ricercare:"))
        self.label_4.setText(_translate("Frame", "RICERCA PRODOTTO"))
        self.pushButtonLogout.setText(_translate("Frame", " Logout"))
        self.pushButtonRicerca.setText(_translate("Frame", " Ricerca"))
        self.pushButtonGestioneMagazzino.setText(_translate("Frame", " Indietro"))

    # permette di gestire il funzionamento del magazzino
    def openGestioneMagazzino(self):
        from Grafica.GestioneMagazzino.GestioneMagazzinoPrincipale import GestioneMagazzinoPrincipale
        self.gestioneMagazzino = QtWidgets.QFrame()
        self.ui = GestioneMagazzinoPrincipale()
        self.ui.setupUi(self.gestioneMagazzino)
        self.gestioneMagazzino.show()
        self.frame.close()  # hide serve a fare l'hide della schermata precedente

    # riporta alla pagina del login
    def openLogin(self):
        from Grafica.GestioneLogin.LoginAmministratore import LoginAmministratore
        self.login = QtWidgets.QFrame()
        self.ui = LoginAmministratore()
        self.ui.setupUi(self.login)
        self.login.show()
        self.frame.close()

    # una volta cliccata la ricerca del prodotto in base
    # alla presenza o meno del prodotto ottengo schermate diverse
    def clickRicerca(self):
        magazzino = Magazzino()

        codiceSeriale = self.lineEditCodiceSeriale.text()
        result = magazzino.ricercaProdotto(codiceSeriale)
        if result[0] is True:
            self.prodottoTrovato = result[1]
            self.openRicercaSuccesso()
        else:
            self.ErrorMessage()

    def ErrorMessage(self):
        self.ErrorBox = QMessageBox()
        self.ErrorBox.setWindowTitle("Errore")
        self.ErrorBox.setText("Il prodotto non si trova\nnel magazzino")
        self.ErrorBox.setStyleSheet(
            "QLabel{min-width:200 px; font-size: 14px; font-family: Helvetica, Sans-Serif; } QPushButton:hover{"
            "background-color: #14626c;color:white; }QPushButton{ width:40px; height:20px; font-size: 10px; "
            "font-family: Helvetica, Sans-Serif; border: 1px solid black; border-radius: 5px; }")
        self.ErrorBox.exec()

    # serve ad aprire la schermata relativa alla ricerca del prodotto andata a buon fine
    def openRicercaSuccesso(self):
        from Grafica.GestioneMagazzino.RicercaProdottoSuccesso import RicercaProdottoSuccesso
        self.ricercaProdottoSuccesso = QtWidgets.QFrame()
        self.ui = RicercaProdottoSuccesso()
        self.ui.setupUi(self.ricercaProdottoSuccesso, self.prodottoTrovato)
        self.ricercaProdottoSuccesso.show()
        self.frame.close()