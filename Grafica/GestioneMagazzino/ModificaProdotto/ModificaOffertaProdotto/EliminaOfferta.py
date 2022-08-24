from PyQt5 import QtCore, QtGui, QtWidgets


class EliminaOfferta(object):

    def setupUi(self, Frame, prodotto):
        self.prodottoTrovato = prodotto
        Frame.setObjectName("Frame")
        Frame.resize(387, 246)
        Frame.setStyleSheet("QFrame{\n"
                            "background-color: rgb(255, 255, 255);\n"
                            "}")
        Frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame = Frame
        self.label_4 = QtWidgets.QLabel(Frame)
        self.label_4.setGeometry(QtCore.QRect(10, 20, 371, 31))
        self.label_4.setStyleSheet("QLabel{\n"
                                   "font-family: impact, sans-serif;\n"
                                   "font-size:30px;\n"
                                   "\n"
                                   "}")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.line = QtWidgets.QFrame(Frame)
        self.line.setGeometry(QtCore.QRect(50, 50, 281, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.pushButtonLogout = QtWidgets.QPushButton(Frame)
        self.pushButtonLogout.setGeometry(QtCore.QRect(10, 200, 141, 31))
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
        icon.addPixmap(QtGui.QPixmap("Images\\log.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonLogout.setIcon(icon)
        self.pushButtonLogout.setCheckable(False)
        self.pushButtonLogout.setObjectName("pushButton_5")
        self.pushButtonModificaOffertaPrincipale = QtWidgets.QPushButton(Frame)
        self.pushButtonModificaOffertaPrincipale.setGeometry(QtCore.QRect(160, 200, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonModificaOffertaPrincipale.setFont(font)
        self.pushButtonModificaOffertaPrincipale.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButtonModificaOffertaPrincipale.setStyleSheet("QPushButton{\n"
                                        "border: 2px solid black;\n"
                                        "border-radius: 10px;\n"
                                        "}\n"
                                        "QPushButton:hover{\n"
                                        "\n"
                                        "background-color: #14626c;\n"
                                        "color:white;\n"
                                        "}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Images\\left.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonModificaOffertaPrincipale.setIcon(icon1)
        self.pushButtonModificaOffertaPrincipale.setObjectName("pushButton_4")
        self.label_5 = QtWidgets.QLabel(Frame)
        self.label_5.setGeometry(QtCore.QRect(10, 70, 371, 61))
        self.label_5.setStyleSheet("QLabel{\n"
                                   "font-family: Helvetica, sans-serif;\n"
                                   "font-weight: 400;\n"
                                   "font-size: 16px\n"
                                   "}")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.pushButtonEliminaOfferta = QtWidgets.QPushButton(Frame)
        self.pushButtonEliminaOfferta.setGeometry(QtCore.QRect(10, 130, 361, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonEliminaOfferta.setFont(font)
        self.pushButtonEliminaOfferta.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButtonEliminaOfferta.setStyleSheet("QPushButton{\n"
                                        "border: 2px solid black;\n"
                                        "border-radius: 10px;\n"
                                        "}\n"
                                        "QPushButton:hover{\n"
                                        "\n"
                                        "background-color: #14626c;\n"
                                        "color:white;\n"
                                        "}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Images\\delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonEliminaOfferta.setIcon(icon2)
        self.pushButtonEliminaOfferta.setCheckable(False)
        self.pushButtonEliminaOfferta.setObjectName("pushButton_7")
        self.pushButtonLogout.clicked.connect(self.openLogin)
        self.pushButtonModificaOffertaPrincipale.clicked.connect(self.openModificaOffertaPrincipaleProdotto)
        self.pushButtonEliminaOfferta.clicked.connect(self.clickElimina)

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Fumetteria - Elimina Offerta Prodotto"))
        self.label_4.setText(_translate("Frame", "ELIMINA OFFERTA "))
        self.pushButtonLogout.setText(_translate("Frame", " Logout"))
        self.pushButtonModificaOffertaPrincipale.setText(_translate("Frame", " Indietro"))
        self.label_5.setText(_translate("Frame", "Sei sicuro di voler eliminare l\'offerta relativa\n"
                                                 " al prodotto in modo definitivo ?"))
        self.pushButtonEliminaOfferta.setText(_translate("Frame", " Elimina Offerta"))

    # Metodo che permette di ritornare all'interfaccia iniziale
    # del programma, ovvero LoginAmministratore.
    def openLogin(self):
        from Grafica.GestioneLogin.LoginAmministratore import LoginAmministratore
        self.login = QtWidgets.QFrame()
        self.ui = LoginAmministratore()
        self.ui.setupUi(self.login)
        self.login.show()
        self.frame.close()

    # Metodo che riporta l'utente all'interno della schermata ModificaOffertaPrincipale
    def openModificaOffertaPrincipaleProdotto(self):
        from Grafica.GestioneMagazzino.ModificaProdotto.ModificaOffertaProdotto.ModificaOffertaPrincipale import ModificaOffertaPrincipale
        self.modificaOffertaPrincipale = QtWidgets.QFrame()
        self.ui = ModificaOffertaPrincipale()
        self.ui.setupUi(self.modificaOffertaPrincipale, self.prodottoTrovato)
        self.modificaOffertaPrincipale.show()
        self.frame.close()

    # Metodo che serve a eliminare l'offerta del prodotto cercato.
    # Nel caso in cui si clicchi direttamente su elimina,
    # viene richiamato il metodo "" di Prodotto
    # per effettuare il cambiamento al prodotto.
    # In seguito viene richiamato il metodo "self.openModificaOffertaSuccesso".
    def clickElimina(self):

        self.prodottoTrovato.eliminaOfferta()
        self.openEliminaOffertaEffettuata()

    # Metodo che fa visualizzare a schermo l'interfaccia EliminaOffertaEffettuata.
    def openEliminaOffertaEffettuata(self):
        from Grafica.GestioneMagazzino.ModificaProdotto.ModificaOffertaProdotto.EliminaOffertaEffettuata import EliminaOffertaEffettuata
        self.eliminaOffertaEffettuata = QtWidgets.QFrame()
        self.ui = EliminaOffertaEffettuata()
        self.ui.setupUi(self.eliminaOffertaEffettuata)
        self.eliminaOffertaEffettuata.show()
        self.frame.close()
