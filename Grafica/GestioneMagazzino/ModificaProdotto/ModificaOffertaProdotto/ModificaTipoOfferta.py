from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

from Amministratore.Amministratore import Amministratore


class ModificaTipoOfferta(object):

    def setupUi(self, Frame, prodotto):

        self.prodottoTrovato = prodotto
        Frame.setObjectName("Frame")
        Frame.resize(387, 241)
        Frame.setStyleSheet("QFrame{\n"
                            "background-color: rgb(255, 255, 255);\n"
                            "}")
        Frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame = Frame
        self.label = QtWidgets.QLabel(Frame)
        self.label.setGeometry(QtCore.QRect(10, 70, 371, 31))
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setStyleSheet("QLabel{\n"
                                 "font-family: Helvetica, sans-serif;\n"
                                 "font-weight: 400;\n"
                                 "font-size: 16px\n"
                                 "}")
        self.label.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
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
        self.radioButton = QtWidgets.QRadioButton(Frame)
        self.radioButton.setGeometry(QtCore.QRect(10, 106, 82, 21))
        self.radioButton.setStyleSheet("QRadioButton{\n"
                                       "font-family: Helvetica, sans-serif;\n"
                                       "font-size:13px;\n"
                                       "}")
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName("radioButton")
        self.TipoOfferta = QtWidgets.QButtonGroup(Frame)
        self.TipoOfferta.setObjectName("TipoOfferta")
        self.TipoOfferta.addButton(self.radioButton)
        self.radioButton_2 = QtWidgets.QRadioButton(Frame)
        self.radioButton_2.setGeometry(QtCore.QRect(10, 130, 82, 21))
        self.radioButton_2.setStyleSheet("QRadioButton{\n"
                                         "font-family: Helvetica, sans-serif;\n"
                                         "font-size:13px;\n"
                                         "}")
        self.radioButton_2.setObjectName("radioButton_2")
        self.TipoOfferta.addButton(self.radioButton_2)
        self.pushButtonModifica = QtWidgets.QPushButton(Frame)
        self.pushButtonModifica.setGeometry(QtCore.QRect(10, 160, 371, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonModifica.setFont(font)
        self.pushButtonModifica.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButtonModifica.setStyleSheet("QPushButton{\n"
                                        "border: 2px solid black;\n"
                                        "border-radius: 10px;\n"
                                        "}\n"
                                        "QPushButton:hover{\n"
                                        "\n"
                                        "background-color: #14626c;\n"
                                        "color:white;\n"
                                        "}")
        self.pushButtonModifica.setCheckable(False)
        self.pushButtonModifica.setObjectName("pushButton_6")
        self.pushButtonLogout.clicked.connect(self.openLogin)
        self.pushButtonModificaOffertaPrincipale.clicked.connect(self.openModificaOffertaPrincipaleProdotto)
        self.pushButtonModifica.clicked.connect(self.clickModifica)

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Fumetteria - Aggiungi Offerta"))
        self.label.setText(_translate("Frame", "Modifica il tipo di offerta:"))
        self.label_4.setText(_translate("Frame", "MODIFICA TIPO OFFERTA"))
        self.pushButtonLogout.setText(_translate("Frame", " Logout"))
        self.pushButtonModificaOffertaPrincipale.setText(_translate("Frame", " Indietro"))
        self.radioButton.setText(_translate("Frame", "Generale"))
        self.radioButton_2.setText(_translate("Frame", "Abbonati"))
        self.pushButtonModifica.setText(_translate("Frame", "Modifica"))

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

    # Metodo che serve a cambiare l'offerta del prodotto cercato.
    # Nel caso in cui il tipo dell'offerta immesso è uguale a quello
    # già presente, viene visualizzata una finestra d'errore.
    # Nel caso in cui invece non si commetta l'errore,
    # viene richiamato il metodo "sovrascriviDati" di Prodotto
    # per effettuare il cambiamento al prodotto.
    # In seguito viene richiamato il metodo "self.openModificaOffertaSuccesso".
    def clickModifica(self):

        tipoOfferta = self.TipoOfferta.checkedButton().text()

        if tipoOfferta != self.prodottoTrovato.getTipoOfferta():
            replacement = str(
                self.prodottoTrovato.getNomeProdotto() + "-" + self.prodottoTrovato.getQuantitaMagazzino()
                + "-" + self.prodottoTrovato.getPrezzo() + "-" + self.prodottoTrovato.getCodiceSeriale()
                + "-" + self.prodottoTrovato.getOfferta() + "-" + tipoOfferta
                + "-" + self.prodottoTrovato.getPrezzoOfferta() + "-" + self.prodottoTrovato.getDataScadenzaOfferta())
            data = self.prodottoTrovato.getProdotto()
            self.prodottoTrovato.sovrascriviDati(data, replacement)
            self.openModificaOffertaEffettuata()

        else:
            self.ErrorTipoOfferta()

    # Metodo che fa visualizzare a schermo l'interfaccia ModificaOffertaEffettuata.
    def openModificaOffertaEffettuata(self):
        from Grafica.GestioneMagazzino.ModificaProdotto.ModificaOffertaProdotto.ModificaOffertaEffettuata import ModificaOffertaEffettuata
        self.modificaOffertaEffettuta = QtWidgets.QFrame()
        self.ui = ModificaOffertaEffettuata()
        self.ui.setupUi(self.modificaOffertaEffettuta)
        self.modificaOffertaEffettuta.show()
        self.frame.close()

    def ErrorTipoOfferta(self):
        self.ErrorBox = QMessageBox()
        self.ErrorBox.setWindowTitle("Errore")
        self.ErrorBox.setText("Il tipo dell'offerta non può essere\nuguale al tipo precedente.")
        self.ErrorBox.setStyleSheet(
            "QLabel{min-width:300 px; font-size: 14px; font-family: Helvetica, Sans-Serif; } QPushButton:hover{"
            "background-color: #14626c;color:white; }QPushButton{ width:40px; height:20px; font-size: 10px; "
            "font-family: Helvetica, Sans-Serif; border: 1px solid black; border-radius: 5px; }")
        self.ErrorBox.exec()