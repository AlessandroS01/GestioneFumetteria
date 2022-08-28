from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


class InserisciCodiceAbbonamento(object):

    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(411, 339)
        Frame.setStyleSheet("QFrame{\n"
                            "background-color: rgb(255, 255, 255);\n"
                            "}")
        Frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame = Frame
        self.label = QtWidgets.QLabel(Frame)
        self.label.setGeometry(QtCore.QRect(10, 60, 391, 71))
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setStyleSheet("QLabel{\n"
                                 "font-family: Helvetica, sans-serif;\n"
                                 "font-weight: 400;\n"
                                 "font-size: 16px\n"
                                 "}")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.lineEditCodiceAbbonamento = QtWidgets.QLineEdit(Frame)
        self.lineEditCodiceAbbonamento.setGeometry(QtCore.QRect(10, 160, 391, 31))
        self.lineEditCodiceAbbonamento.setStyleSheet("QLineEdit{\n"
                                    "border: 2px solid black;\n"
                                    "border-radius: 6px;\n"
                                    "}")
        self.lineEditCodiceAbbonamento.setObjectName("lineEdit")
        self.label_4 = QtWidgets.QLabel(Frame)
        self.label_4.setGeometry(QtCore.QRect(0, 20, 411, 31))
        self.label_4.setStyleSheet("QLabel{\n"
                                   "font-family: impact, sans-serif;\n"
                                   "font-size:30px;\n"
                                   "\n"
                                   "}")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.line = QtWidgets.QFrame(Frame)
        self.line.setGeometry(QtCore.QRect(20, 50, 371, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.pushButtonLogout = QtWidgets.QPushButton(Frame)
        self.pushButtonLogout.setGeometry(QtCore.QRect(10, 300, 141, 31))
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
        self.pushButtonInserisci = QtWidgets.QPushButton(Frame)
        self.pushButtonInserisci.setGeometry(QtCore.QRect(10, 200, 391, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonInserisci.setFont(font)
        self.pushButtonInserisci.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButtonInserisci.setStyleSheet("QPushButton{\n"
                                        "border: 2px solid black;\n"
                                        "border-radius: 10px;\n"
                                        "}\n"
                                        "QPushButton:hover{\n"
                                        "\n"
                                        "background-color: #14626c;\n"
                                        "color:white;\n"
                                        "}")
        self.pushButtonInserisci.setCheckable(False)
        self.pushButtonInserisci.setObjectName("pushButton_6")
        self.pushButtonGestioneVenditePrincipale = QtWidgets.QPushButton(Frame)
        self.pushButtonGestioneVenditePrincipale.setGeometry(QtCore.QRect(160, 300, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonGestioneVenditePrincipale.setFont(font)
        self.pushButtonGestioneVenditePrincipale.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButtonGestioneVenditePrincipale.setStyleSheet("QPushButton{\n"
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
        self.pushButtonGestioneVenditePrincipale.setIcon(icon1)
        self.pushButtonGestioneVenditePrincipale.setObjectName("pushButton_4")
        self.label_2 = QtWidgets.QLabel(Frame)
        self.label_2.setGeometry(QtCore.QRect(10, 140, 391, 16))
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setStyleSheet("QLabel{\n"
                                   "font-family: Helvetica, sans-serif;\n"
                                   "font-weight: 400;\n"
                                   "font-size: 16px\n"
                                   "}")
        self.label_2.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.pushButtonInserisciSenzaCodice = QtWidgets.QPushButton(Frame)
        self.pushButtonInserisciSenzaCodice.setGeometry(QtCore.QRect(10, 240, 391, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonInserisciSenzaCodice.setFont(font)
        self.pushButtonInserisciSenzaCodice.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButtonInserisciSenzaCodice.setStyleSheet("QPushButton{\n"
                                        "border: 2px solid black;\n"
                                        "border-radius: 10px;\n"
                                        "}\n"
                                        "QPushButton:hover{\n"
                                        "\n"
                                        "background-color: #14626c;\n"
                                        "color:white;\n"
                                        "}")
        self.pushButtonInserisciSenzaCodice.setCheckable(False)
        self.pushButtonInserisciSenzaCodice.setObjectName("pushButton_7")
        self.pushButtonInserisci.clicked.connect(self.clickInserisci)
        self.pushButtonInserisciSenzaCodice.clicked.connect(self.clickContinua)
        self.pushButtonLogout.clicked.connect(self.openLogin)
        self.pushButtonGestioneVenditePrincipale.clicked.connect(self.openGestioneVenditePrincipale)

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Fumetteria - Inserisci Codice Abbonamento"))
        self.label.setText(_translate("Frame", "Se l\'acquisto è stato fatto da un cliente abbonato\n"
                                               "inserisci il codice del suo abbonamento in modo che\n"
                                               " vengano applicate, se presenti, le offerte per abbonati. "))
        self.label_4.setText(_translate("Frame", "INSERISCI CODICE ABBONAMENTO"))
        self.pushButtonLogout.setText(_translate("Frame", " Logout"))
        self.pushButtonInserisci.setText(_translate("Frame", "Inserisci"))
        self.pushButtonGestioneVenditePrincipale.setText(_translate("Frame", " Indietro"))
        self.label_2.setText(_translate("Frame", "Inserisci il codice abbonamento:"))
        self.pushButtonInserisciSenzaCodice.setText(_translate("Frame", "Continua senza codice"))

    # Metodo che permette la ricerca di un abbonamento all'interno
    # del file di testo "Abbonamenti.txt" tramite l'utilizzo del codice
    # inserito dall'interfaccia.
    # Nel caso in cui l'abbonamento non venga trovato, viene
    # visualizzata una finestra di errore.
    # Nel caso in cui invece venga trovato, l'interfaccia AggiungiAcquisto,
    # richiamata tramite il metodo "self.openAggiungiAcquisto".
    def clickInserisci(self):
        from GestioneAbbonamenti.GestioneAbbonamenti import GestioneAbbonamenti

        gestoreAbbonamenti = GestioneAbbonamenti()
        codiceAbbonamento = self.lineEditCodiceAbbonamento.text()

        result = gestoreAbbonamenti.ricercaAbbonamentoCodice(codiceAbbonamento)

        if result[0] is True:
            self.AbbonamentoTrovato()
            self.openAggiungiAcquisto(True)
        else:
            self.ErrorRicerca()

    # Metodo apre direttamente l'interfaccia AggiungiAcquisto,
    # richiamata tramite il metodo "self.openAggiungiAcquisto".
    def clickContinua(self):

        self.openAggiungiAcquisto(False)

    # Metodo che serve ad aprire l'interfaccia AggiungiAcquisto, con una variabile
    # di controllo, che se settata a True, indica che l'abbonamento è stato
    # trovato con successo. Se settata a False, invece, indica che l'abbonamento cercato non esiste.
    def openAggiungiAcquisto(self, controllo):
        from Grafica.GestioneVendite.AggiungiAcquisto import AggiungiAcquisto
        self.aggiungiAcquisto = QtWidgets.QFrame()
        self.ui = AggiungiAcquisto()
        self.ui.setupUi(self.aggiungiAcquisto, controllo)
        self.aggiungiAcquisto.show()
        self.frame.close()

    # Metodo che permette di ritornare all'interfaccia iniziale
    # del programma, ovvero LoginAmministratore.
    def openLogin(self):
        from Grafica.GestioneLogin.LoginAmministratore import LoginAmministratore
        self.login = QtWidgets.QFrame()
        self.ui = LoginAmministratore()
        self.ui.setupUi(self.login)
        self.login.show()
        self.frame.close()

    # Metodo che permette di ritornare all'interfaccia GestioneVenditePrincipale.
    def openGestioneVenditePrincipale(self):
        from Grafica.GestioneVendite.GestioneVenditePrincipale import GestioneVenditePrincipale
        self.gestioneVenditePrincipale = QtWidgets.QFrame()
        self.ui = GestioneVenditePrincipale()
        self.ui.setupUi(self.gestioneVenditePrincipale)
        self.gestioneVenditePrincipale.show()
        self.frame.close()

    def ErrorRicerca(self):
        self.ErrorBox = QMessageBox()
        self.ErrorBox.setWindowTitle("Errore")
        self.ErrorBox.setText("L'abbonamento con il codice inserito\nnon esiste.")
        self.ErrorBox.setStyleSheet(
            "QLabel{min-width:300 px; font-size: 14px; font-family: Helvetica, Sans-Serif; } QPushButton:hover{"
            "background-color: #14626c;color:white; }QPushButton{ width:40px; height:20px; font-size: 10px; "
            "font-family: Helvetica, Sans-Serif; border: 1px solid black; border-radius: 5px; }")
        self.ErrorBox.exec()

    def AbbonamentoTrovato(self):
        self.ErrorBox = QMessageBox()
        self.ErrorBox.setWindowTitle("AbbonamentoTrovato")
        self.ErrorBox.setText("L'abbonamento con il codice inserito\nè stato inserito.")
        self.ErrorBox.setStyleSheet(
            "QLabel{min-width:300 px; font-size: 14px; font-family: Helvetica, Sans-Serif; } QPushButton:hover{"
            "background-color: #14626c;color:white; }QPushButton{ width:40px; height:20px; font-size: 10px; "
            "font-family: Helvetica, Sans-Serif; border: 1px solid black; border-radius: 5px; }")
        self.ErrorBox.exec()
