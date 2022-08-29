from PyQt5 import QtCore, QtGui, QtWidgets


class GestioneVenditePrincipale(object):

    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(476, 388)
        Frame.setStyleSheet("QFrame{\n"
                            "background-color: rgb(255, 255, 255);\n"
                            "}")
        Frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame = Frame
        self.label_4 = QtWidgets.QLabel(Frame)
        self.label_4.setGeometry(QtCore.QRect(10, 10, 461, 31))
        self.label_4.setStyleSheet("QLabel{\n"
                                   "font-family: impact, sans-serif;\n"
                                   "font-size:30px;\n"
                                   "\n"
                                   "}")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.line = QtWidgets.QFrame(Frame)
        self.line.setGeometry(QtCore.QRect(80, 40, 311, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.pushButtonLogout = QtWidgets.QPushButton(Frame)
        self.pushButtonLogout.setGeometry(QtCore.QRect(10, 350, 141, 31))
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
        icon.addPixmap(QtGui.QPixmap("Images\\log.png"), QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        self.pushButtonLogout.setIcon(icon)
        self.pushButtonLogout.setCheckable(False)
        self.pushButtonLogout.setObjectName("pushButton_5")
        self.pushButtonVistaHome = QtWidgets.QPushButton(Frame)
        self.pushButtonVistaHome.setGeometry(QtCore.QRect(160, 350, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonVistaHome.setFont(font)
        self.pushButtonVistaHome.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButtonVistaHome.setStyleSheet("QPushButton{\n"
                                               "border: 2px solid black;\n"
                                               "border-radius: 10px;\n"
                                               "}\n"
                                               "QPushButton:hover{\n"
                                               "\n"
                                               "background-color: #14626c;\n"
                                               "color:white;\n"
                                               "}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Images\\home.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonVistaHome.setIcon(icon1)
        self.pushButtonVistaHome.setObjectName("pushButton_4")
        self.pushButtonAcquistoAbbonamento = QtWidgets.QPushButton(Frame)
        self.pushButtonAcquistoAbbonamento.setGeometry(QtCore.QRect(250, 180, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonAcquistoAbbonamento.setFont(font)
        self.pushButtonAcquistoAbbonamento.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButtonAcquistoAbbonamento.setStyleSheet("QPushButton{\n"
                                                         "border: 2px solid black;\n"
                                                         "border-radius: 10px;\n"
                                                         "}\n"
                                                         "QPushButton:hover{\n"
                                                         "\n"
                                                         "background-color: #14626c;\n"
                                                         "color:white;\n"
                                                         "}")
        self.pushButtonAcquistoAbbonamento.setObjectName("pushButton_2")
        self.pushButtonRegistrazioneAcquisto = QtWidgets.QPushButton(Frame)
        self.pushButtonRegistrazioneAcquisto.setGeometry(QtCore.QRect(30, 180, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonRegistrazioneAcquisto.setFont(font)
        self.pushButtonRegistrazioneAcquisto.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButtonRegistrazioneAcquisto.setStyleSheet("QPushButton{\n"
                                                           "border: 2px solid black;\n"
                                                           "border-radius: 10px;\n"
                                                           "}\n"
                                                           "QPushButton:hover{\n"
                                                           "\n"
                                                           "background-color: #14626c;\n"
                                                           "color:white;\n"
                                                           "}")
        self.pushButtonRegistrazioneAcquisto.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(Frame)
        self.label.setGeometry(QtCore.QRect(10, 50, 461, 121))
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setStyleSheet("QLabel{\n"
                                 "font-family: Helvetica, sans-serif;\n"
                                 "font-weight: 400;\n"
                                 "font-size: 16px\n"
                                 "}")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButtonVenditeGiornaliere = QtWidgets.QPushButton(Frame)
        self.pushButtonVenditeGiornaliere.setGeometry(QtCore.QRect(30, 250, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonVenditeGiornaliere.setFont(font)
        self.pushButtonVenditeGiornaliere.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButtonVenditeGiornaliere.setStyleSheet("QPushButton{\n"
                                                        "border: 2px solid black;\n"
                                                        "border-radius: 10px;\n"
                                                        "}\n"
                                                        "QPushButton:hover{\n"
                                                        "\n"
                                                        "background-color: #14626c;\n"
                                                        "color:white;\n"
                                                        "}")
        self.pushButtonVenditeGiornaliere.setObjectName("pushButton_3")
        self.pushButtonInserisciDataIncasso = QtWidgets.QPushButton(Frame)
        self.pushButtonInserisciDataIncasso.setGeometry(QtCore.QRect(250, 250, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonInserisciDataIncasso.setFont(font)
        self.pushButtonInserisciDataIncasso.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButtonInserisciDataIncasso.setStyleSheet("QPushButton{\n"
                                                          "border: 2px solid black;\n"
                                                          "border-radius: 10px;\n"
                                                          "}\n"
                                                          "QPushButton:hover{\n"
                                                          "\n"
                                                          "background-color: #14626c;\n"
                                                          "color:white;\n"
                                                          "}")
        self.pushButtonInserisciDataIncasso.setObjectName("pushButton_6")
        self.pushButtonLogout.clicked.connect(self.openLogin)
        self.pushButtonVistaHome.clicked.connect(self.openVistaHome)
        self.pushButtonRegistrazioneAcquisto.clicked.connect(self.openInserisciCodiceAbbonamento)
        self.pushButtonAcquistoAbbonamento.clicked.connect(self.openAcquistoAbbonamento)
        self.pushButtonVenditeGiornaliere.clicked.connect(self.openInserisciDataVendite)
        self.pushButtonInserisciDataIncasso.clicked.connect(self.openInserisciDataIncasso)

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Fumetteria - Gestione Vendite"))
        self.label_4.setText(_translate("Frame", "GESTIONE VENDITE"))
        self.pushButtonLogout.setText(_translate("Frame", " Logout"))
        self.pushButtonVistaHome.setText(_translate("Frame", "Home"))
        self.pushButtonAcquistoAbbonamento.setText(_translate("Frame", "Acquisto\n"
                                                                       " Abbonamento"))
        self.pushButtonRegistrazioneAcquisto.setText(_translate("Frame", "Registrazione\n"
                                                                         " Acquisto"))
        self.label.setText(_translate("Frame", "Utilizzare i pulsanti per navigare tra le attività. Se vuoi \n"
                                               " registrare un acquisto effettuato da parte di un cliente cliccare\n"
                                               "Registrazione Acquisto. Se si vuole aggiungere un nuovo\n"
                                               "cliente abbonato, cliccare Acquisto Abbonamento. Se si vogliono\n"
                                               " le vendite o l\'incasso totale durante una giornata, cliccare sui\n"
                                               " due relativi pulsanti."))
        self.pushButtonVenditeGiornaliere.setText(_translate("Frame", "Visualizza\n"
                                                                      " Vendite Giornata"))
        self.pushButtonInserisciDataIncasso.setText(_translate("Frame", "Visualizza\n"
                                                                        " Incasso Giornata"))

    # Metodo che permette di ritornare all'interfaccia VistaHome.
    def openVistaHome(self):
        from Grafica.GestioneGeneraleProgramma.VistaHome import VistaHome
        self.home = QtWidgets.QFrame()
        self.ui = VistaHome()
        self.ui.setupUi(self.home)
        self.home.show()
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

    # Metodo che permette di aprire l'interfaccia sulla quale si
    # può immettere il codice abbonamento per ricercare un abbonamento
    # prima di effettuare un acquisto.
    # L'interfaccia è : InserisciCodiceAbbonamento
    def openInserisciCodiceAbbonamento(self):
        from Grafica.GestioneVendite.InserisciCodiceAbbonamento import InserisciCodiceAbbonamento
        self.inserisciCodiceAbbonamento = QtWidgets.QFrame()
        self.ui = InserisciCodiceAbbonamento()
        self.ui.setupUi(self.inserisciCodiceAbbonamento)
        self.inserisciCodiceAbbonamento.show()
        self.frame.close()

    # Metodo che permette di aprire l'interfaccia sulla quale si
    # può creare e salvare un nuovo abbonamento.
    # L'interfaccia è : InserisciAbbonamento
    def openAcquistoAbbonamento(self):
        from Grafica.GestioneVendite.InserisciAbbonamento import InserisciAbbonamento
        self.inserisciAbbonamento = QtWidgets.QFrame()
        self.ui = InserisciAbbonamento()
        self.ui.setupUi(self.inserisciAbbonamento)
        self.inserisciAbbonamento.show()
        self.frame.close()

    # Metodo che permette di aprire l'interfaccia sulla quale si
    # possono cercare le vendite avvenute durante una giornata.
    # L'interfaccia è : InserisciDataVendite
    def openInserisciDataVendite(self):
        from Grafica.GestioneVendite.InserisciDataVendite import InserisciDataVendite
        self.inserisciDataVendite = QtWidgets.QFrame()
        self.ui = InserisciDataVendite()
        self.ui.setupUi(self.inserisciDataVendite)
        self.inserisciDataVendite.show()
        self.frame.close()

    # Metodo che permette di aprire l'interfaccia sulla quale si
    # può vedere l'incasso durante una giornata.
    # L'interfaccia è : InserisciDataIncasso
    def openInserisciDataIncasso(self):
        from Grafica.GestioneVendite.InserisciDataIncasso import InserisciDataIncasso
        self.inserisciDataIncasso = QtWidgets.QFrame()
        self.ui = InserisciDataIncasso()
        self.ui.setupUi(self.inserisciDataIncasso)
        self.inserisciDataIncasso.show()
        self.frame.close()
