from datetime import datetime

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


class ModificaDataScadenzaOfferta(object):

    def setupUi(self, Frame, prodotto):
        self.prodottoTrovato = prodotto
        Frame.setObjectName("Frame")
        Frame.resize(387, 241)
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
        self.pushButtonModifica = QtWidgets.QPushButton(Frame)
        self.pushButtonModifica.setGeometry(QtCore.QRect(10, 150, 371, 31))
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
        self.label_3 = QtWidgets.QLabel(Frame)
        self.label_3.setGeometry(QtCore.QRect(10, 70, 371, 21))
        self.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_3.setStyleSheet("QLabel{\n"
                                   "font-family: Helvetica, sans-serif;\n"
                                   "font-weight: 400;\n"
                                   "font-size: 16px\n"
                                   "}")
        self.label_3.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.dateEditDataScadenzaOfferta = QtWidgets.QDateEdit(Frame)
        self.dateEditDataScadenzaOfferta.setGeometry(QtCore.QRect(10, 100, 371, 31))
        self.dateEditDataScadenzaOfferta.setStyleSheet("QDateEdit{\n"
                                                       "border: 2px solid black;\n"
                                                       "border-radius: 6px;\n"
                                                       "}")
        self.dateEditDataScadenzaOfferta.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.dateEditDataScadenzaOfferta.setCalendarPopup(False)
        self.dateEditDataScadenzaOfferta.setDate(QtCore.QDate(2023, 1, 1))
        self.dateEditDataScadenzaOfferta.setObjectName("dateEdit")
        self.pushButtonLogout.clicked.connect(self.openLogin)
        self.pushButtonModificaOffertaPrincipale.clicked.connect(self.openModificaOffertaPrincipaleProdotto)
        self.pushButtonModifica.clicked.connect(self.clickModifica)

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Fumetteria - Modifica Data Scadenza Offerta"))
        self.label_4.setText(_translate("Frame", "MODIFICA DATA SCADENZA"))
        self.pushButtonLogout.setText(_translate("Frame", " Logout"))
        self.pushButtonModificaOffertaPrincipale.setText(_translate("Frame", " Indietro"))
        self.pushButtonModifica.setText(_translate("Frame", "Modifica"))
        self.label_3.setText(_translate("Frame", "Data scadenza offerta:"))

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
        from Grafica.GestioneMagazzino.ModificaProdotto.ModificaOffertaProdotto.ModificaOffertaPrincipale import \
            ModificaOffertaPrincipale
        self.modificaOffertaPrincipale = QtWidgets.QFrame()
        self.ui = ModificaOffertaPrincipale()
        self.ui.setupUi(self.modificaOffertaPrincipale, self.prodottoTrovato)
        self.modificaOffertaPrincipale.show()
        self.frame.close()

    # Metodo che serve a cambiare la data di scadenza
    # dell'offerta del prodotto cercato.
    # Nel caso in cui la data immessa è precedente alla data
    # odierna, viene visualizzata una finestra d'errore.
    # Nel caso in cui invece non si commetta l'errore,
    # viene richiamato il metodo "sovrascriviDati" di Prodotto
    # per effettuare il cambiamento al prodotto.
    # In seguito viene richiamato il metodo "self.openModificaOffertaSuccesso".
    def clickModifica(self):

        dataScadenzaOffertaText = self.dateEditDataScadenzaOfferta.text()

        dataScadenzaOffertaDatetime = datetime.strptime(dataScadenzaOffertaText, '%d/%m/%Y').date()
        today = datetime.now().date()

        if dataScadenzaOffertaDatetime > today:
            replacement = str(
                self.prodottoTrovato.getNomeProdotto() + "-" + self.prodottoTrovato.getQuantitaMagazzino()
                + "-" + self.prodottoTrovato.getPrezzo() + "-" + self.prodottoTrovato.getCodiceSeriale()
                + "-" + self.prodottoTrovato.getOfferta() + "-" + self.prodottoTrovato.getTipoOfferta()
                + "-" + self.prodottoTrovato.getPrezzoOfferta() + "-" + dataScadenzaOffertaText)
            data = self.prodottoTrovato.getProdotto()
            self.prodottoTrovato.sovrascriviDati(data, replacement)
            self.openModificaOffertaEffettuata()
        else:
            self.ErrorData()

    # Metodo che fa visualizzare a schermo l'interfaccia ModificaOffertaEffettuata.
    def openModificaOffertaEffettuata(self):
        from Grafica.GestioneMagazzino.ModificaProdotto.ModificaOffertaProdotto.ModificaOffertaEffettuata import \
            ModificaOffertaEffettuata
        self.modificaOffertaEffettuta = QtWidgets.QFrame()
        self.ui = ModificaOffertaEffettuata()
        self.ui.setupUi(self.modificaOffertaEffettuta)
        self.modificaOffertaEffettuta.show()
        self.frame.close()

    def ErrorData(self):
        self.ErrorBox = QMessageBox()
        self.ErrorBox.setWindowTitle("Errore")
        self.ErrorBox.setText("Re-inserire la data")
        self.ErrorBox.setStyleSheet(
            "QLabel{min-width:200 px; font-size: 14px; font-family: Helvetica, Sans-Serif; } QPushButton:hover{"
            "background-color: #14626c;color:white; }QPushButton{ width:40px; height:20px; font-size: 10px; "
            "font-family: Helvetica, Sans-Serif; border: 1px solid black; border-radius: 5px; }")
        self.ErrorBox.exec()
