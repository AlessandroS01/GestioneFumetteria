from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


class ModificaTelefonoCliente(object):

    def setupUi(self, Frame, abbonamento):
        self.abbonamentoTrovato = abbonamento
        Frame.setObjectName("Frame")
        Frame.resize(411, 243)
        Frame.setStyleSheet("QFrame{\n"
                            "background-color: rgb(255, 255, 255);\n"
                            "}")
        Frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame = Frame
        self.label = QtWidgets.QLabel(Frame)
        self.label.setGeometry(QtCore.QRect(10, 70, 391, 21))
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setStyleSheet("QLabel{\n"
                                "font-family: Helvetica, sans-serif;\n"
                                "font-weight: 400;\n"
                                "font-size: 16px\n"
                                "}")
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.lineEditTelefono = QtWidgets.QLineEdit(Frame)
        self.lineEditTelefono.setGeometry(QtCore.QRect(10, 100, 391, 31))
        self.lineEditTelefono.setStyleSheet("QLineEdit{\n"
                                    "border: 2px solid black;\n"
                                    "border-radius: 6px;\n"
                                    "}")
        self.lineEditTelefono.setObjectName("lineEdit")
        self.label_4 = QtWidgets.QLabel(Frame)
        self.label_4.setGeometry(QtCore.QRect(10, 20, 391, 31))
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
        self.pushButtonModifica = QtWidgets.QPushButton(Frame)
        self.pushButtonModifica.setGeometry(QtCore.QRect(10, 140, 391, 31))
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
        self.pushButtonModificaClientePrincipale = QtWidgets.QPushButton(Frame)
        self.pushButtonModificaClientePrincipale.setGeometry(QtCore.QRect(160, 200, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonModificaClientePrincipale.setFont(font)
        self.pushButtonModificaClientePrincipale.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButtonModificaClientePrincipale.setStyleSheet("QPushButton{\n"
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
        self.pushButtonModificaClientePrincipale.setIcon(icon1)
        self.pushButtonModificaClientePrincipale.setObjectName("pushButton_4")
        self.pushButtonLogout.clicked.connect(self.openLogin)
        self.pushButtonModificaClientePrincipale.clicked.connect(self.openModificaClientePrincipale)
        self.pushButtonModifica.clicked.connect(self.clickModifica)

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Fumetteria - Modifica Telefono Cliente"))
        self.label.setText(_translate("Frame", "Inserisci il nuovo numero di telefono del cliente:"))
        self.label_4.setText(_translate("Frame", "MODIFICA TELEFONO CLIENTE"))
        self.pushButtonLogout.setText(_translate("Frame", " Logout"))
        self.pushButtonModifica.setText(_translate("Frame", "Modifica"))
        self.pushButtonModificaClientePrincipale.setText(_translate("Frame", " Indietro"))

    # Metodo che permette di ritornare all'interfaccia iniziale
    # del programma, ovvero LoginAmministratore.
    def openLogin(self):
        from Grafica.GestioneLogin.LoginAmministratore import LoginAmministratore
        self.login = QtWidgets.QFrame()
        self.ui = LoginAmministratore()
        self.ui.setupUi(self.login)
        self.login.show()
        self.frame.close()

    # Metodo che permette di ritornare all'interfaccia ModificaClientePrincipale.
    def openModificaClientePrincipale(self):
        from Grafica.GestioneAbbonamenti.ModificaCliente.ModificaClientePrincipale import ModificaClientePrincipale
        self.modificaClientePrincipale = QtWidgets.QFrame()
        self.ui = ModificaClientePrincipale()
        self.ui.setupUi(self.modificaClientePrincipale, self.abbonamentoTrovato)
        self.modificaClientePrincipale.show()
        self.frame.close()

    # Metodo che permette di modificare il telefono del cliente trovato
    # dopo aver cliccato il pulsante Modifica.
    # Nel caso in cui il numero di telefono inserito è già utilizzato da un altro cliente o
    # dallo stesso, viene visualizzata una schermata di errore.
    # Nel caso in cui non si commettano errori, viene richiamato il
    # metodo "sovrascriviDati" della classe Abbonamento per cambiare l'attributo
    # telefono del cliente trovato all'interno del file di testo "Abbonamenti.txt".
    # Successivamente viene richiamato il metodo "self.openModificaEffettuata".
    def clickModifica(self):

        from GestioneAbbonamenti.GestioneAbbonamenti import GestioneAbbonamenti
        telefonoNuovo = self.lineEditTelefono.text()
        gestoreAbbonamenti = GestioneAbbonamenti()

        if telefonoNuovo.isnumeric():
            if gestoreAbbonamenti.ricercaTelefono(telefonoNuovo)[0] is False:

                self.abbonamentoTrovato.modificaTelefono(telefonoNuovo)
                self.openModificaEffettuata()
            else:
                self.ErrorTelefonoEsistente()
        else:
            self.ErrorTelefono()

    # Metodo che fa visualizzare a schermo l'interfaccia ModificaClienteSuccesso.
    def openModificaEffettuata(self):
        from Grafica.GestioneAbbonamenti.ModificaCliente.ModificaClienteSuccesso import ModificaClienteSuccesso
        self.modificaEffettuta = QtWidgets.QFrame()
        self.ui = ModificaClienteSuccesso()
        self.ui.setupUi(self.modificaEffettuta)
        self.modificaEffettuta.show()
        self.frame.close()

    def ErrorTelefonoEsistente(self):
        self.ErrorBox = QMessageBox()
        self.ErrorBox.setWindowTitle("Errore")
        self.ErrorBox.setText("Il telefono inserito è già esistente.")
        self.ErrorBox.setStyleSheet(
            "QLabel{min-width:300 px; font-size: 14px; font-family: Helvetica, Sans-Serif; } QPushButton:hover{"
            "background-color: #14626c;color:white; }QPushButton{ width:40px; height:20px; font-size: 10px; "
            "font-family: Helvetica, Sans-Serif; border: 1px solid black; border-radius: 5px; }")
        self.ErrorBox.exec()

    def ErrorTelefono(self):
        self.ErrorBox = QMessageBox()
        self.ErrorBox.setWindowTitle("Errore")
        self.ErrorBox.setText("Il numero di telefono può contenere \nsolo caratteri numerici.")
        self.ErrorBox.setStyleSheet(
            "QLabel{min-width:300 px; font-size: 14px; font-family: Helvetica, Sans-Serif; } QPushButton:hover{"
            "background-color: #14626c;color:white; }QPushButton{ width:40px; height:20px; font-size: 10px; "
            "font-family: Helvetica, Sans-Serif; border: 1px solid black; border-radius: 5px; }")
        self.ErrorBox.exec()
