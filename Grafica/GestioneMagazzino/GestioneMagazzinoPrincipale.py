from PyQt5 import QtCore, QtGui, QtWidgets


class GestioneMagazzinoPrincipale(object):

    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(414, 362)
        Frame.setStyleSheet("QFrame{\n"
                            "background-color: rgb(255, 255, 255);\n"
                            "}")
        self.frame = Frame
        self.label_2 = QtWidgets.QLabel(Frame)
        self.label_2.setGeometry(QtCore.QRect(70, 20, 261, 31))
        self.label_2.setStyleSheet("QLabel{\n"
                                   "font-family: impact, sans-serif;\n"
                                   "font-size:30px;\n"
                                   "\n"
                                   "}")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.line = QtWidgets.QFrame(Frame)
        self.line.setGeometry(QtCore.QRect(40, 50, 321, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.pushButton_2 = QtWidgets.QPushButton(Frame)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 150, 161, 51))
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
        self.pushButtonRicercaProdotto = QtWidgets.QPushButton(Frame)
        self.pushButtonRicercaProdotto.setGeometry(QtCore.QRect(230, 150, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonRicercaProdotto.setFont(font)
        self.pushButtonRicercaProdotto.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButtonRicercaProdotto.setStyleSheet("QPushButton{\n"
                                                     "border: 2px solid black;\n"
                                                     "border-radius: 10px;\n"
                                                     "}\n"
                                                     "QPushButton:hover{\n"
                                                     "\n"
                                                     "background-color: #14626c;\n"
                                                     "color:white;\n"
                                                     "}")
        self.pushButtonRicercaProdotto.setObjectName("pushButton_3")
        self.label = QtWidgets.QLabel(Frame)
        self.label.setGeometry(QtCore.QRect(20, 70, 371, 61))
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setStyleSheet("QLabel{\n"
                                 "font-family: Helvetica, sans-serif;\n"
                                 "font-weight: 400;\n"
                                 "font-size: 16px\n"
                                 "}")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButtonVistaHome = QtWidgets.QPushButton(Frame)
        self.pushButtonVistaHome.setGeometry(QtCore.QRect(160, 320, 141, 31))
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
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(
            "Images\\home.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonVistaHome.setIcon(icon)
        self.pushButtonVistaHome.setObjectName("pushButton_4")
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
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(
            "Images\\log.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonLogout.setIcon(icon1)
        self.pushButtonLogout.setCheckable(False)
        self.pushButtonLogout.setObjectName("pushButton_5")
        self.pushButtonAggiungiProdotto = QtWidgets.QPushButton(Frame)
        self.pushButtonAggiungiProdotto.setGeometry(QtCore.QRect(130, 220, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonAggiungiProdotto.setFont(font)
        self.pushButtonAggiungiProdotto.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButtonAggiungiProdotto.setStyleSheet("QPushButton{\n"
                                                      "border: 2px solid black;\n"
                                                      "border-radius: 10px;\n"
                                                      "}\n"
                                                      "QPushButton:hover{\n"
                                                      "\n"
                                                      "background-color: #14626c;\n"
                                                      "color:white;\n"
                                                      "}")
        self.pushButtonAggiungiProdotto.setObjectName("pushButton_6")
        self.pushButtonVistaHome.clicked.connect(self.openVistaHome)
        self.pushButtonLogout.clicked.connect(self.openLogin)
        self.pushButtonAggiungiProdotto.clicked.connect(self.openAggiungiProdotto)
        self.pushButtonRicercaProdotto.clicked.connect(self.openRicercaProdotto)

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Fumetteria - Gestione Magazzino"))
        self.label_2.setText(_translate("Frame", "GESTIONE MAGAZZINO"))
        self.pushButton_2.setText(_translate("Frame", "Visualizza \n"
                                                      "Magazzino"))
        self.pushButtonRicercaProdotto.setText(_translate("Frame", "Ricerca \n"
                                                                   "Prodotto"))
        self.label.setText(_translate("Frame", "Scegli una delle tre opzioni disponibili o clicca \n"
                                               "il tasto home per tornare alla Home. Per modificare\n"
                                               "un prodotto effettua la Ricerca"))
        self.pushButtonVistaHome.setText(_translate("Frame", "Home"))
        self.pushButtonLogout.setText(_translate("Frame", " Logout"))
        self.pushButtonAggiungiProdotto.setText(_translate("Frame", "Aggiungi \n"
                                                                    "Prodotto"))

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
    # può aggiungere un prodotto all'interno del file "Magazzino.txt".
    # L'interfaccia è : AggiungiProdotto
    def openAggiungiProdotto(self):
        from Grafica.GestioneMagazzino.AggiungiProdotto import AggiungiProdotto
        self.aggiungiProdotto = QtWidgets.QFrame()
        self.ui = AggiungiProdotto()
        self.ui.setupUi(self.aggiungiProdotto)
        self.aggiungiProdotto.show()
        self.frame.close()

    # Metodo che permette di aprire l'interfaccia sulla quale si
    # può ricercare un prodotto tramite codice seriale.
    # L'interfaccia è : RicercaProdotto
    def openRicercaProdotto(self):
        from Grafica.GestioneMagazzino.RicercaProdotto import RicercaProdotto
        self.ricercaProdotto = QtWidgets.QFrame()
        self.ui = RicercaProdotto()
        self.ui.setupUi(self.ricercaProdotto)
        self.ricercaProdotto.show()
        self.frame.close()
