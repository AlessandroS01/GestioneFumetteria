from PyQt5 import QtCore, QtGui, QtWidgets

from GestioneAbbonamenti.GestioneAbbonamenti import GestioneAbbonamenti


class InserisciAbbonamento(object):

    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(387, 562)
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
        self.lineEditNomeCliente = QtWidgets.QLineEdit(Frame)
        self.lineEditNomeCliente.setGeometry(QtCore.QRect(10, 100, 371, 31))
        self.lineEditNomeCliente.setStyleSheet("QLineEdit{\n"
                                    "border: 2px solid black;\n"
                                    "border-radius: 6px;\n"
                                    "}")
        self.lineEditNomeCliente.setObjectName("lineEdit")
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
        self.pushButtonLogout.setGeometry(QtCore.QRect(10, 520, 141, 31))
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
        self.pushButtonInserisci.setGeometry(QtCore.QRect(10, 460, 371, 31))
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
        self.pushButtonGestioneVenditePrincipale.setGeometry(QtCore.QRect(160, 520, 141, 31))
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
        self.lineEditCognomeCliente = QtWidgets.QLineEdit(Frame)
        self.lineEditCognomeCliente.setGeometry(QtCore.QRect(10, 170, 371, 31))
        self.lineEditCognomeCliente.setStyleSheet("QLineEdit{\n"
                                      "border: 2px solid black;\n"
                                      "border-radius: 6px;\n"
                                      "}")
        self.lineEditCognomeCliente.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(Frame)
        self.label_3.setGeometry(QtCore.QRect(10, 140, 391, 21))
        self.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_3.setStyleSheet("QLabel{\n"
                                   "font-family: Helvetica, sans-serif;\n"
                                   "font-weight: 400;\n"
                                   "font-size: 16px\n"
                                   "}")
        self.label_3.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(Frame)
        self.label_5.setGeometry(QtCore.QRect(10, 210, 391, 21))
        self.label_5.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_5.setStyleSheet("QLabel{\n"
                                   "font-family: Helvetica, sans-serif;\n"
                                   "font-weight: 400;\n"
                                   "font-size: 16px\n"
                                   "}")
        self.label_5.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.lineEditCodiceFiscaleCliente = QtWidgets.QLineEdit(Frame)
        self.lineEditCodiceFiscaleCliente.setGeometry(QtCore.QRect(10, 240, 371, 31))
        self.lineEditCodiceFiscaleCliente.setStyleSheet("QLineEdit{\n"
                                      "border: 2px solid black;\n"
                                      "border-radius: 6px;\n"
                                      "}")
        self.lineEditCodiceFiscaleCliente.setObjectName("lineEdit_3")
        self.label_6 = QtWidgets.QLabel(Frame)
        self.label_6.setGeometry(QtCore.QRect(10, 280, 391, 21))
        self.label_6.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_6.setStyleSheet("QLabel{\n"
                                   "font-family: Helvetica, sans-serif;\n"
                                   "font-weight: 400;\n"
                                   "font-size: 16px\n"
                                   "}")
        self.label_6.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.lineEditEmailCliente = QtWidgets.QLineEdit(Frame)
        self.lineEditEmailCliente.setGeometry(QtCore.QRect(10, 310, 371, 31))
        self.lineEditEmailCliente.setStyleSheet("QLineEdit{\n"
                                      "border: 2px solid black;\n"
                                      "border-radius: 6px;\n"
                                      "}")
        self.lineEditEmailCliente.setObjectName("lineEdit_4")
        self.label_7 = QtWidgets.QLabel(Frame)
        self.label_7.setGeometry(QtCore.QRect(10, 350, 391, 21))
        self.label_7.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_7.setStyleSheet("QLabel{\n"
                                   "font-family: Helvetica, sans-serif;\n"
                                   "font-weight: 400;\n"
                                   "font-size: 16px\n"
                                   "}")
        self.label_7.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.lineEditTelefonoCliente = QtWidgets.QLineEdit(Frame)
        self.lineEditTelefonoCliente.setGeometry(QtCore.QRect(10, 380, 371, 31))
        self.lineEditTelefonoCliente.setStyleSheet("QLineEdit{\n"
                                      "border: 2px solid black;\n"
                                      "border-radius: 6px;\n"
                                      "}")
        self.lineEditTelefonoCliente.setObjectName("lineEdit_5")
        self.pushButtonGestioneVenditePrincipale.clicked.connect(self.openGestioneVenditePrincipale)
        self.pushButtonLogout.clicked.connect(self.openLogin)
        self.pushButtonInserisci.clicked.connect(self.clickInserisciAbbonamento)

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Fumetteria - Inserisci Abbonamento"))
        self.label.setText(_translate("Frame", "Inserisci nome cliente:"))
        self.label_4.setText(_translate("Frame", "INSERISCI ABBONAMENTO"))
        self.pushButtonLogout.setText(_translate("Frame", " Logout"))
        self.pushButtonInserisci.setText(_translate("Frame", "Inserisci"))
        self.pushButtonGestioneVenditePrincipale.setText(_translate("Frame", " Indietro"))
        self.label_3.setText(_translate("Frame", "Inserisci cognome cliente:"))
        self.label_5.setText(_translate("Frame", "Inserisci codice fiscale cliente:"))
        self.label_6.setText(_translate("Frame", "Inserisci email cliente:"))
        self.label_7.setText(_translate("Frame", "Inserisci telefono cliente:"))

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

    # Metodo utilizzato per andare ad inserire sul file un
    # nuovo abbonamento a seguito delle verifiche necessarie
    # per settare email e telefono del cliente.
    # Se tutti i vari controlli vengono superati,
    # viene aperte l'interfaccia di conferma dell'inserimento del
    # nuovo abbonamento.
    def clickInserisciAbbonamento(self):

        gestoreAbbonamenti = GestioneAbbonamenti()

        nome = self.lineEditNomeCliente.text()
        cognome = self.lineEditCognomeCliente.text()
        codiceFiscale = self.lineEditCodiceFiscaleCliente.text()
        telefono = self.lineEditTelefonoCliente.text()
        email = self.lineEditEmailCliente.text()



