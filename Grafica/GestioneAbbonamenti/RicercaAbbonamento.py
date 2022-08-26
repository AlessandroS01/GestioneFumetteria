from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


class RicercaAbbonamento(object):

    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(387, 271)
        Frame.setStyleSheet("QFrame{\n"
                            "background-color: rgb(255, 255, 255);\n"
                            "}")
        Frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame = Frame
        self.label = QtWidgets.QLabel(Frame)
        self.label.setGeometry(QtCore.QRect(10, 110, 371, 31))
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setStyleSheet("QLabel{\n"
                                 "font-family: Helvetica, sans-serif;\n"
                                 "font-weight: 400;\n"
                                 "font-size: 16px\n"
                                 "}")
        self.label.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.lineEditCodiceAbbonamento = QtWidgets.QLineEdit(Frame)
        self.lineEditCodiceAbbonamento.setGeometry(QtCore.QRect(10, 140, 371, 31))
        self.lineEditCodiceAbbonamento.setStyleSheet("QLineEdit{\n"
                                                     "border: 2px solid black;\n"
                                                     "border-radius: 6px;\n"
                                                     "}")
        self.lineEditCodiceAbbonamento.setObjectName("lineEdit")
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
        self.line.setGeometry(QtCore.QRect(40, 50, 311, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.pushButtonLogout = QtWidgets.QPushButton(Frame)
        self.pushButtonLogout.setGeometry(QtCore.QRect(10, 230, 141, 31))
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
        self.pushButtonRicerca = QtWidgets.QPushButton(Frame)
        self.pushButtonRicerca.setGeometry(QtCore.QRect(10, 180, 371, 31))
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
        icon1.addPixmap(QtGui.QPixmap("Images\\magnifying-glass.png"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.pushButtonRicerca.setIcon(icon1)
        self.pushButtonRicerca.setCheckable(False)
        self.pushButtonRicerca.setObjectName("pushButton_6")
        self.pushButtonGestioneAbbonamentiPrincipale = QtWidgets.QPushButton(Frame)
        self.pushButtonGestioneAbbonamentiPrincipale.setGeometry(QtCore.QRect(160, 230, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonGestioneAbbonamentiPrincipale.setFont(font)
        self.pushButtonGestioneAbbonamentiPrincipale.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButtonGestioneAbbonamentiPrincipale.setStyleSheet("QPushButton{\n"
                                                                   "border: 2px solid black;\n"
                                                                   "border-radius: 10px;\n"
                                                                   "}\n"
                                                                   "QPushButton:hover{\n"
                                                                   "\n"
                                                                   "background-color: #14626c;\n"
                                                                   "color:white;\n"
                                                                   "}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Images\\left.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonGestioneAbbonamentiPrincipale.setIcon(icon2)
        self.pushButtonGestioneAbbonamentiPrincipale.setObjectName("pushButton_4")
        self.label_2 = QtWidgets.QLabel(Frame)
        self.label_2.setGeometry(QtCore.QRect(10, 70, 371, 41))
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setStyleSheet("QLabel{\n"
                                   "font-family: Helvetica, sans-serif;\n"
                                   "font-weight: 400;\n"
                                   "font-size: 16px\n"
                                   "}")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.pushButtonGestioneAbbonamentiPrincipale.clicked.connect(self.openGestioneAbbonamentiPrincipale)
        self.pushButtonLogout.clicked.connect(self.openLogin)
        self.pushButtonRicerca.clicked.connect(self.clickRicerca)

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Fumetteria - Ricerca Abbonamento"))
        self.label.setText(_translate("Frame", "Inserisci il codice dell\'abbonamento da ricercare:"))
        self.label_4.setText(_translate("Frame", "RICERCA ABBONAMENTO"))
        self.pushButtonLogout.setText(_translate("Frame", " Logout"))
        self.pushButtonRicerca.setText(_translate("Frame", " Ricerca"))
        self.pushButtonGestioneAbbonamentiPrincipale.setText(_translate("Frame", " Indietro"))
        self.label_2.setText(_translate("Frame", "Una volta effettuata la ricerca potrai modificare le\n"
                                                 " informazioni del cliente."))

    # Metodo che permette di ritornare all'interfaccia GestioneAbbonamentiPrincipale.
    def openGestioneAbbonamentiPrincipale(self):
        from Grafica.GestioneAbbonamenti.GestioneAbbonamentiPrincipale import GestioneAbbonamentiPrincipale
        self.gestioneAbbonamentiPrincipale = QtWidgets.QFrame()
        self.ui = GestioneAbbonamentiPrincipale()
        self.ui.setupUi(self.gestioneAbbonamentiPrincipale)
        self.gestioneAbbonamentiPrincipale.show()
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

    # Metodo che permette la ricerca di un abbonamento all'interno
    # del file di testo "Abbonamenti.txt" tramite l'utilizzo del codice
    # inserito dall'interfaccia.
    # Nel caso in cui l'abbonamento non venga trovato, viene
    # visualizzata una finestra di errore.
    # Nel caso in cui invece venga trovato, questo
    # viene salvato in una nuova istanza di Abbonamento e viene
    # richiamato il metodo "self.openRicercaSuccesso".
    def clickRicerca(self):
        from GestioneAbbonamenti.GestioneAbbonamenti import GestioneAbbonamenti

        gestoreAbbonamenti = GestioneAbbonamenti()
        codiceAbbonamento = self.lineEditCodiceAbbonamento.text()

        result = gestoreAbbonamenti.ricercaAbbonamentoCodice(codiceAbbonamento)

        if result[0] is True:
            abbonamentoTrovato = result[1]
            self.openRicercaSuccesso(abbonamentoTrovato)
        else:
            self.ErrorRicerca()

    # Metodo che serve ad aprire l'interfaccia relativa alla
    # ricerca del prodotto andata a buon fine, ovvero RicercaAbbonamentoSuccesso
    # in cui si possono vedere le informazioni relative a quell'abbonamento.
    def openRicercaSuccesso(self, abbonamento):
        from Grafica.GestioneAbbonamenti.RicercaAbbonamentoSuccesso import RicercaAbbonamentoSuccesso
        self.ricercaAbbonamentoSuccesso = QtWidgets.QFrame()
        self.ui = RicercaAbbonamentoSuccesso()
        self.ui.setupUi(self.ricercaAbbonamentoSuccesso, abbonamento)
        self.ricercaAbbonamentoSuccesso.show()
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
