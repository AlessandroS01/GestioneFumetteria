from PyQt5 import QtCore, QtGui, QtWidgets


class ModificaPrincipaleProdotto(object):

    def setupUi(self, Frame, prodotto):

        self.prodottoTrovato = prodotto
        Frame.setObjectName("Frame")
        Frame.resize(437, 362)
        Frame.setStyleSheet("QFrame{\n"
                            "background-color: rgb(255, 255, 255);\n"
                            "}")
        Frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame = Frame
        self.label_4 = QtWidgets.QLabel(Frame)
        self.label_4.setGeometry(QtCore.QRect(10, 20, 421, 31))
        self.label_4.setStyleSheet("QLabel{\n"
                                   "font-family: impact, sans-serif;\n"
                                   "font-size:30px;\n"
                                   "\n"
                                   "}")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.line = QtWidgets.QFrame(Frame)
        self.line.setGeometry(QtCore.QRect(50, 50, 321, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.pushButtonLogout = QtWidgets.QPushButton(Frame)
        self.pushButtonLogout.setGeometry(QtCore.QRect(10, 320, 141, 31))
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
        self.pushButtonRicercaProdottoSuccesso = QtWidgets.QPushButton(Frame)
        self.pushButtonRicercaProdottoSuccesso.setGeometry(QtCore.QRect(160, 320, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonRicercaProdottoSuccesso.setFont(font)
        self.pushButtonRicercaProdottoSuccesso.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButtonRicercaProdottoSuccesso.setStyleSheet("QPushButton{\n"
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
        self.pushButtonRicercaProdottoSuccesso.setIcon(icon1)
        self.pushButtonRicercaProdottoSuccesso.setObjectName("pushButton_4")
        self.pushButtonModificaQuantita = QtWidgets.QPushButton(Frame)
        self.pushButtonModificaQuantita.setGeometry(QtCore.QRect(20, 110, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonModificaQuantita.setFont(font)
        self.pushButtonModificaQuantita.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButtonModificaQuantita.setStyleSheet("QPushButton{\n"
                                                      "border: 2px solid black;\n"
                                                      "border-radius: 10px;\n"
                                                      "}\n"
                                                      "QPushButton:hover{\n"
                                                      "\n"
                                                      "background-color: #14626c;\n"
                                                      "color:white;\n"
                                                      "}")
        self.pushButtonModificaQuantita.setCheckable(False)
        self.pushButtonModificaQuantita.setObjectName("pushButton_8")
        self.pushButtonModificaCodice = QtWidgets.QPushButton(Frame)
        self.pushButtonModificaCodice.setGeometry(QtCore.QRect(20, 170, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonModificaCodice.setFont(font)
        self.pushButtonModificaCodice.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButtonModificaCodice.setStyleSheet("QPushButton{\n"
                                                    "border: 2px solid black;\n"
                                                    "border-radius: 10px;\n"
                                                    "}\n"
                                                    "QPushButton:hover{\n"
                                                    "\n"
                                                    "background-color: #14626c;\n"
                                                    "color:white;\n"
                                                    "}")
        self.pushButtonModificaCodice.setCheckable(False)
        self.pushButtonModificaCodice.setObjectName("pushButton_9")
        self.pushButtonModificaOffertaProdottoPrincipale = QtWidgets.QPushButton(Frame)
        self.pushButtonModificaOffertaProdottoPrincipale.setGeometry(QtCore.QRect(120, 240, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonModificaOffertaProdottoPrincipale.setFont(font)
        self.pushButtonModificaOffertaProdottoPrincipale.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButtonModificaOffertaProdottoPrincipale.setStyleSheet("QPushButton{\n"
                                         "border: 2px solid black;\n"
                                         "border-radius: 10px;\n"
                                         "}\n"
                                         "QPushButton:hover{\n"
                                         "\n"
                                         "background-color: #14626c;\n"
                                         "color:white;\n"
                                         "}")
        self.pushButtonModificaOffertaProdottoPrincipale.setCheckable(False)
        self.pushButtonModificaOffertaProdottoPrincipale.setObjectName("pushButton_10")
        self.pushButtonModificaPrezzo = QtWidgets.QPushButton(Frame)
        self.pushButtonModificaPrezzo.setGeometry(QtCore.QRect(230, 110, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonModificaPrezzo.setFont(font)
        self.pushButtonModificaPrezzo.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButtonModificaPrezzo.setStyleSheet("QPushButton{\n"
                                                    "border: 2px solid black;\n"
                                                    "border-radius: 10px;\n"
                                                    "}\n"
                                                    "QPushButton:hover{\n"
                                                    "\n"
                                                    "background-color: #14626c;\n"
                                                    "color:white;\n"
                                                    "}")
        self.pushButtonModificaPrezzo.setCheckable(False)
        self.pushButtonModificaPrezzo.setObjectName("pushButton_12")
        self.pushButtonElimina = QtWidgets.QPushButton(Frame)
        self.pushButtonElimina.setGeometry(QtCore.QRect(230, 170, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonElimina.setFont(font)
        self.pushButtonElimina.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButtonElimina.setStyleSheet("QPushButton{\n"
                                         "border: 2px solid black;\n"
                                         "border-radius: 10px;\n"
                                         "}\n"
                                         "QPushButton:hover{\n"
                                         "\n"
                                         "background-color: #14626c;\n"
                                         "color:white;\n"
                                         "}")
        self.pushButtonElimina.setCheckable(False)
        self.pushButtonElimina.setObjectName("pushButton_13")
        self.label = QtWidgets.QLabel(Frame)
        self.label.setGeometry(QtCore.QRect(10, 60, 421, 41))
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setStyleSheet("QLabel{\n"
                                 "font-family: Helvetica, sans-serif;\n"
                                 "font-weight: 400;\n"
                                 "font-size: 16px\n"
                                 "}")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButtonLogout.clicked.connect(self.openLogin)
        self.pushButtonRicercaProdottoSuccesso.clicked.connect(self.openRicercaProdottoSuccesso)
        self.pushButtonModificaQuantita.clicked.connect(self.openModificaQuantitaProdotto)
        self.pushButtonModificaPrezzo.clicked.connect(self.openModificaPrezzoProdotto)
        self.pushButtonModificaCodice.clicked.connect(self.openModificaCodice)
        self.pushButtonElimina.clicked.connect(self.openEliminaProdotto)
        self.pushButtonModificaOffertaProdottoPrincipale.clicked.connect(self.openModificaOffertaProdottoPrincipale)

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Fumetteria - Modifica Prodotto"))
        self.label_4.setText(_translate("Frame", "MODIFICA PRODOTTO"))
        self.pushButtonLogout.setText(_translate("Frame", " Logout"))
        self.pushButtonRicercaProdottoSuccesso.setText(_translate("Frame", " Indietro"))
        self.pushButtonModificaQuantita.setText(_translate("Frame", "Modifica\n"
                                                                    "Quantità Prodotto"))
        self.pushButtonModificaCodice.setText(_translate("Frame", "Modifica\n"
                                                                  "Codice Seriale "))
        self.pushButtonModificaOffertaProdottoPrincipale.setText(_translate("Frame", "Modifica\n"
                                                       " Offerta Prodotto"))
        self.pushButtonModificaPrezzo.setText(_translate("Frame", "Modifica \n"
                                                                  "Prezzo Prodotto"))
        self.pushButtonElimina.setText(_translate("Frame", "Elimina \n"
                                                       " Prodotto"))
        self.label.setText(_translate("Frame", "Seleziona una delle opzioni per modificare il prodotto "))

    # Metodo che permette di ritornare all'interfaccia iniziale
    # del programma, ovvero LoginAmministratore.
    def openLogin(self):
        from Grafica.GestioneLogin.LoginAmministratore import LoginAmministratore
        self.login = QtWidgets.QFrame()
        self.ui = LoginAmministratore()
        self.ui.setupUi(self.login)
        self.login.show()
        self.frame.close()

    # Metodo che fa visualizzare a schermo l'interfaccia RicercaProdottoSuccesso.
    def openRicercaProdottoSuccesso(self):
        from Grafica.GestioneMagazzino.RicercaProdottoSuccesso import RicercaProdottoSuccesso
        self.modificaQuantitaProdotto = QtWidgets.QFrame()
        self.ui = RicercaProdottoSuccesso()
        self.ui.setupUi(self.modificaQuantitaProdotto, self.prodottoTrovato)
        self.modificaQuantitaProdotto.show()
        self.frame.close()

    # Metodo che permette di visualizzare l'interfaccia
    # utilizzata per modificare la quantità del prodotto trovato
    # all'interno del magazzino.
    # L'interfaccia è ModificaQuantitaProdotto.
    def openModificaQuantitaProdotto(self):
        from Grafica.GestioneMagazzino.ModificaProdotto.ModificaQuantitaProdotto import ModificaQuantitaProdotto
        self.modificaQuantitaProdotto = QtWidgets.QFrame()
        self.ui = ModificaQuantitaProdotto()
        self.ui.setupUi(self.modificaQuantitaProdotto, self.prodottoTrovato)
        self.modificaQuantitaProdotto.show()
        self.frame.close()

    # Metodo che permette di visualizzare l'interfaccia
    # utilizzata per modificare il prezzo del prodotto trovato
    # all'interno del magazzino.
    # L'interfaccia è ModificaPrezzoProdotto.
    def openModificaPrezzoProdotto(self):
        from Grafica.GestioneMagazzino.ModificaProdotto.ModificaPrezzoProdotto import ModificaPrezzoProdotto
        self.modificaPrezzoProdotto = QtWidgets.QFrame()
        self.ui = ModificaPrezzoProdotto()
        self.ui.setupUi(self.modificaPrezzoProdotto, self.prodottoTrovato)
        self.modificaPrezzoProdotto.show()
        self.frame.close()

    # Metodo che permette di visualizzare l'interfaccia
    # utilizzata per modificare il codice del prodotto trovato
    # all'interno del magazzino.
    # L'interfaccia è ModificaCodiceProdotto.
    def openModificaCodice(self):
        from Grafica.GestioneMagazzino.ModificaProdotto.ModificaCodiceProdotto import ModificaCodiceProdotto
        self.modificaCodice = QtWidgets.QFrame()
        self.ui = ModificaCodiceProdotto()
        self.ui.setupUi(self.modificaCodice, self.prodottoTrovato)
        self.modificaCodice.show()
        self.frame.close()

    # Metodo che permette di visualizzare l'interfaccia
    # utilizzata per eliminare il prodotto trovato dal magazzino.
    # L'interfaccia è EliminaProdotto.
    def openEliminaProdotto(self):
        from Grafica.GestioneMagazzino.ModificaProdotto.EliminaProdotto import EliminaProdotto
        self.eliminaProdotto = QtWidgets.QFrame()
        self.ui = EliminaProdotto()
        self.ui.setupUi(self.eliminaProdotto, self.prodottoTrovato)
        self.eliminaProdotto.show()
        self.frame.close()

    # Metodo che permette di visualizzare l'interfaccia
    # utilizzata per modificare l'offerta del prodotto trovato
    # all'interno del magazzino.
    # L'interfaccia è ModificaOffertaProdotto.
    def openModificaOffertaProdottoPrincipale(self):
            from Grafica.GestioneMagazzino.ModificaProdotto.ModificaOffertaProdotto.ModificaOffertaPrincipale import ModificaOffertaPrincipale
            self.modificaOffertaPrincipale = QtWidgets.QFrame()
            self.ui = ModificaOffertaPrincipale()
            self.ui.setupUi(self.modificaOffertaPrincipale, self.prodottoTrovato)
            self.modificaOffertaPrincipale.show()
            self.frame.close()
