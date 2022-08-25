from PyQt5 import QtCore, QtGui, QtWidgets


class GestioneAbbonamentiPrincipale(object):

    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(459, 397)
        Frame.setStyleSheet("QFrame{\n"
                            "background-color: rgb(255, 255, 255);\n"
                            "}")
        Frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame = Frame
        self.label_4 = QtWidgets.QLabel(Frame)
        self.label_4.setGeometry(QtCore.QRect(10, 10, 441, 31))
        self.label_4.setStyleSheet("QLabel{\n"
                                   "font-family: impact, sans-serif;\n"
                                   "font-size:30px;\n"
                                   "\n"
                                   "}")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.line = QtWidgets.QFrame(Frame)
        self.line.setGeometry(QtCore.QRect(70, 40, 311, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.pushButtonLogout = QtWidgets.QPushButton(Frame)
        self.pushButtonLogout.setGeometry(QtCore.QRect(10, 360, 141, 31))
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
        self.pushButtonVistaHome = QtWidgets.QPushButton(Frame)
        self.pushButtonVistaHome.setGeometry(QtCore.QRect(160, 360, 141, 31))
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
        icon1.addPixmap(QtGui.QPixmap("Images\\home.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonVistaHome.setIcon(icon1)
        self.pushButtonVistaHome.setObjectName("pushButton_4")
        self.pushButton_2 = QtWidgets.QPushButton(Frame)
        self.pushButton_2.setGeometry(QtCore.QRect(240, 160, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_2.setStyleSheet("QPushButton{\n"
                                        "border: 2px solid black;\n"
                                        "border-radius: 10px;\n"
                                        "}\n"
                                        "QPushButton:hover{\n"
                                        "\n"
                                        "background-color: #14626c;\n"
                                        "color:white;\n"
                                        "}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButtonRicercaAbbonamento = QtWidgets.QPushButton(Frame)
        self.pushButtonRicercaAbbonamento.setGeometry(QtCore.QRect(20, 220, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonRicercaAbbonamento.setFont(font)
        self.pushButtonRicercaAbbonamento.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButtonRicercaAbbonamento.setStyleSheet("QPushButton{\n"
                                                        "border: 2px solid black;\n"
                                                        "border-radius: 10px;\n"
                                                        "}\n"
                                                        "QPushButton:hover{\n"
                                                        "\n"
                                                        "background-color: #14626c;\n"
                                                        "color:white;\n"
                                                        "}")
        self.pushButtonRicercaAbbonamento.setObjectName("pushButton_3")
        self.pushButtonModificaPrezzoAbbonamento = QtWidgets.QPushButton(Frame)
        self.pushButtonModificaPrezzoAbbonamento.setGeometry(QtCore.QRect(240, 220, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonModificaPrezzoAbbonamento.setFont(font)
        self.pushButtonModificaPrezzoAbbonamento.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButtonModificaPrezzoAbbonamento.setStyleSheet("QPushButton{\n"
                                        "border: 2px solid black;\n"
                                        "border-radius: 10px;\n"
                                        "}\n"
                                        "QPushButton:hover{\n"
                                        "\n"
                                        "background-color: #14626c;\n"
                                        "color:white;\n"
                                        "}")
        self.pushButtonModificaPrezzoAbbonamento.setObjectName("pushButton_6")
        self.pushButtonVisualizzaClientiAbbonati = QtWidgets.QPushButton(Frame)
        self.pushButtonVisualizzaClientiAbbonati.setGeometry(QtCore.QRect(20, 160, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonVisualizzaClientiAbbonati.setFont(font)
        self.pushButtonVisualizzaClientiAbbonati.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButtonVisualizzaClientiAbbonati.setStyleSheet("QPushButton{\n"
                                                               "border: 2px solid black;\n"
                                                               "border-radius: 10px;\n"
                                                               "}\n"
                                                               "QPushButton:hover{\n"
                                                               "\n"
                                                               "background-color: #14626c;\n"
                                                               "color:white;\n"
                                                               "}")
        self.pushButtonVisualizzaClientiAbbonati.setObjectName("pushButton")
        self.pushButtonVisualizzaAbbonamentiAttivi = QtWidgets.QPushButton(Frame)
        self.pushButtonVisualizzaAbbonamentiAttivi.setGeometry(QtCore.QRect(20, 280, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonVisualizzaAbbonamentiAttivi.setFont(font)
        self.pushButtonVisualizzaAbbonamentiAttivi.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButtonVisualizzaAbbonamentiAttivi.setStyleSheet("QPushButton{\n"
                                        "border: 2px solid black;\n"
                                        "border-radius: 10px;\n"
                                        "}\n"
                                        "QPushButton:hover{\n"
                                        "\n"
                                        "background-color: #14626c;\n"
                                        "color:white;\n"
                                        "}")
        self.pushButtonVisualizzaAbbonamentiAttivi.setObjectName("pushButton_7")
        self.pushButtonVisualizzaProdottiAbbonati = QtWidgets.QPushButton(Frame)
        self.pushButtonVisualizzaProdottiAbbonati.setGeometry(QtCore.QRect(240, 280, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonVisualizzaProdottiAbbonati.setFont(font)
        self.pushButtonVisualizzaProdottiAbbonati.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButtonVisualizzaProdottiAbbonati.setStyleSheet("QPushButton{\n"
                                                                "border: 2px solid black;\n"
                                                                "border-radius: 10px;\n"
                                                                "}\n"
                                                                "QPushButton:hover{\n"
                                                                "\n"
                                                                "background-color: #14626c;\n"
                                                                "color:white;\n"
                                                                "}")
        self.pushButtonVisualizzaProdottiAbbonati.setObjectName("pushButton_8")
        self.label = QtWidgets.QLabel(Frame)
        self.label.setGeometry(QtCore.QRect(0, 60, 451, 81))
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setStyleSheet("QLabel{\n"
                                 "font-family: Helvetica, sans-serif;\n"
                                 "font-weight: 400;\n"
                                 "font-size: 16px\n"
                                 "}")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButtonLogout.clicked.connect(self.openLogin)
        self.pushButtonVistaHome.clicked.connect(self.openVistaHome)
        self.pushButtonVisualizzaProdottiAbbonati.clicked.connect(self.openVisualizzaProdottiAbbonati)
        self.pushButtonRicercaAbbonamento.clicked.connect(self.openRicercaAbbonamento)
        self.pushButtonVisualizzaClientiAbbonati.clicked.connect(self.openVisualizzaClientiAbbonati)
        self.pushButtonVisualizzaAbbonamentiAttivi.clicked.connect(self.openVisualizzaAbbonamentiAttivi)
        self.pushButtonModificaPrezzoAbbonamento.clicked.connect(self.openModificaPrezzoAbbonamento)

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Fumetteria - Gestione Abbonamenti"))
        self.label_4.setText(_translate("Frame", "GESTIONE ABBONAMENTI"))
        self.pushButtonLogout.setText(_translate("Frame", " Logout"))
        self.pushButtonVistaHome.setText(_translate("Frame", " Home"))
        self.pushButton_2.setText(_translate("Frame", "Statistiche \n"
                                                      " Abbonamenti "))
        self.pushButtonRicercaAbbonamento.setText(_translate("Frame", "Ricerca \n"
                                                                      " Abbonamento"))
        self.pushButtonModificaPrezzoAbbonamento.setText(_translate("Frame", "Modifica Prezzo\nAbbonamento"))
        self.pushButtonVisualizzaClientiAbbonati.setText(_translate("Frame", "Visualizza \n"
                                                                             "Clienti Abbonati"))
        self.pushButtonVisualizzaAbbonamentiAttivi.setText(_translate("Frame", "Visualizza\n"
                                                      "Abbonamenti Attivi"))
        self.pushButtonVisualizzaProdottiAbbonati.setText(_translate("Frame", "Visualizza Prodotti\nper Abbonati"))
        self.label.setText(_translate("Frame", "Utilizza i pulsanti per navigare tra le attività. Se vuoi\n"
                                               " visualizzare quanti abbonamenti sono stati emessi in un giorno\n"
                                               " clicca Statistiche Abbonamenti. I prodotti per abbonati sono\n"
                                               "prodotti che hanno un'offerta per abbonati."))

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
    # possono visualizzare i prodotti in offerta per gli abbonati.
    # L'interfaccia è : VisualizzaProdottiAbbonati
    def openVisualizzaProdottiAbbonati(self):
        from Grafica.GestioneAbbonamenti.VisualizzaProdottiAbbonati import VisualizzaProdottiAbbonati
        self.visualizzaProdottiAbbonati = QtWidgets.QFrame()
        self.ui = VisualizzaProdottiAbbonati()
        self.ui.setupUi(self.visualizzaProdottiAbbonati)
        self.visualizzaProdottiAbbonati.show()
        self.frame.close()

    # Metodo che permette di aprire l'interfaccia sulla quale si
    # può ricercare un abbonamento.
    # L'interfaccia è : RicercaAbbonamento.
    def openRicercaAbbonamento(self):
        from Grafica.GestioneAbbonamenti.RicercaAbbonamento import RicercaAbbonamento
        self.ricercaAbbonamento = QtWidgets.QFrame()
        self.ui = RicercaAbbonamento()
        self.ui.setupUi(self.ricercaAbbonamento)
        self.ricercaAbbonamento.show()
        self.frame.close()

    # Metodo che permette di aprire l'interfaccia sulla quale si
    # possono vedere quali sono i clienti abbonati, con abbonamento
    # scaduto o meno.
    # L'interfaccia è : VisualizzaClientiAbbonati.
    def openVisualizzaClientiAbbonati(self):
        from Grafica.GestioneAbbonamenti.VisualizzaClientiAbbonati import VisualizzaClientiAbbonati
        self.visualizzaClientiabbonati = QtWidgets.QFrame()
        self.ui = VisualizzaClientiAbbonati()
        self.ui.setupUi(self.visualizzaClientiabbonati)
        self.visualizzaClientiabbonati.show()
        self.frame.close()

    # Metodo che permette di aprire l'interfaccia sulla quale si
    # possono vedere quali sono i clienti abbonati, con abbonamento
    # rigorosamente attivo.
    # L'interfaccia è : VisualizzaAbbonamentiAttivi.
    def openVisualizzaAbbonamentiAttivi(self):
        from Grafica.GestioneAbbonamenti.VisualizzaAbbonamentiAttivi import VisualizzaAbbonamentiAttivi
        self.visualizzaAbbonamentiAttivi = QtWidgets.QFrame()
        self.ui = VisualizzaAbbonamentiAttivi()
        self.ui.setupUi(self.visualizzaAbbonamentiAttivi)
        self.visualizzaAbbonamentiAttivi.show()
        self.frame.close()

    # Metodo che permette di aprire l'interfaccia sulla quale si
    # può cambiare il prezzo degli abbonamenti.
    # L'interfaccia è : ModificaPrezzoAbbonamento.
    def openModificaPrezzoAbbonamento(self):
        from Grafica.GestioneAbbonamenti.ModificaPrezzoAbbonamenti import ModificaPrezzoAbbonamenti
        self.modificaPrezzoAbbonamento = QtWidgets.QFrame()
        self.ui = ModificaPrezzoAbbonamenti()
        self.ui.setupUi(self.modificaPrezzoAbbonamento)
        self.modificaPrezzoAbbonamento.show()
        self.frame.close()
