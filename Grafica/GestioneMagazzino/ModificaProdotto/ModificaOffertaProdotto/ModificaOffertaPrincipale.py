from PyQt5 import QtCore, QtGui, QtWidgets


class ModificaOffertaPrincipale(object):

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
        self.line.setGeometry(QtCore.QRect(30, 50, 381, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.pushButton_9 = QtWidgets.QPushButton(Frame)
        self.pushButton_9.setGeometry(QtCore.QRect(20, 200, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_9.setStyleSheet("QPushButton{\n"
                                        "border: 2px solid black;\n"
                                        "border-radius: 10px;\n"
                                        "}\n"
                                        "QPushButton:hover{\n"
                                        "\n"
                                        "background-color: #14626c;\n"
                                        "color:white;\n"
                                        "}")
        self.pushButton_9.setCheckable(False)
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_8 = QtWidgets.QPushButton(Frame)
        self.pushButton_8.setGeometry(QtCore.QRect(20, 140, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_8.setStyleSheet("QPushButton{\n"
                                        "border: 2px solid black;\n"
                                        "border-radius: 10px;\n"
                                        "}\n"
                                        "QPushButton:hover{\n"
                                        "\n"
                                        "background-color: #14626c;\n"
                                        "color:white;\n"
                                        "}")
        self.pushButton_8.setCheckable(False)
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_13 = QtWidgets.QPushButton(Frame)
        self.pushButton_13.setGeometry(QtCore.QRect(230, 200, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_13.setFont(font)
        self.pushButton_13.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_13.setStyleSheet("QPushButton{\n"
                                         "border: 2px solid black;\n"
                                         "border-radius: 10px;\n"
                                         "}\n"
                                         "QPushButton:hover{\n"
                                         "\n"
                                         "background-color: #14626c;\n"
                                         "color:white;\n"
                                         "}")
        self.pushButton_13.setCheckable(False)
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_12 = QtWidgets.QPushButton(Frame)
        self.pushButton_12.setGeometry(QtCore.QRect(230, 140, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_12.setStyleSheet("QPushButton{\n"
                                         "border: 2px solid black;\n"
                                         "border-radius: 10px;\n"
                                         "}\n"
                                         "QPushButton:hover{\n"
                                         "\n"
                                         "background-color: #14626c;\n"
                                         "color:white;\n"
                                         "}")
        self.pushButton_12.setCheckable(False)
        self.pushButton_12.setObjectName("pushButton_12")
        self.label = QtWidgets.QLabel(Frame)
        self.label.setGeometry(QtCore.QRect(10, 70, 421, 41))
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setStyleSheet("QLabel{\n"
                                 "font-family: Helvetica, sans-serif;\n"
                                 "font-weight: 400;\n"
                                 "font-size: 16px\n"
                                 "}")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
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
        self.pushButtonLogout.setObjectName("pushButton_6")
        self.pushButtonModficaProdottoPrincipale = QtWidgets.QPushButton(Frame)
        self.pushButtonModficaProdottoPrincipale.setGeometry(QtCore.QRect(160, 320, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonModficaProdottoPrincipale.setFont(font)
        self.pushButtonModficaProdottoPrincipale.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButtonModficaProdottoPrincipale.setStyleSheet("QPushButton{\n"
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
        self.pushButtonModficaProdottoPrincipale.setIcon(icon1)
        self.pushButtonModficaProdottoPrincipale.setObjectName("pushButton_5")
        self.pushButtonModficaProdottoPrincipale.clicked.connect(self.openModificaPrincipaleProdotto)
        self.pushButtonLogout.clicked.connect(self.openLogin)

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Fumetteria - Modifica Nome Utente"))
        self.label_4.setText(_translate("Frame", "MODIFICA OFFERTA PRODOTTO"))
        self.pushButton_9.setText(_translate("Frame", "Modifica\n"
                                                      "Data Scadenza "))
        self.pushButton_8.setText(_translate("Frame", "Modifica\n"
                                                      "Tipo Offerta"))
        self.pushButton_13.setText(_translate("Frame", "Elimina \n"
                                                       "Offerta"))
        self.pushButton_12.setText(_translate("Frame", "Modifica \n"
                                                       "Prezzo Offerta"))
        self.label.setText(_translate("Frame", "Seleziona una delle opzioni per modificare l\'offerta relativa\n"
                                               " al prodotto. Clicca indietro per tornare a modifica prodotto"))
        self.pushButtonLogout.setText(_translate("Frame", " Logout"))
        self.pushButtonModficaProdottoPrincipale.setText(_translate("Frame", " Indietro"))

        # Metodo che riporta l'utente all'interno della schermata ModificaPrincipalePrincipale
        def openModificaPrincipaleProdotto(self):
            from Grafica.GestioneMagazzino.ModificaProdotto.ModificaPrincipaleProdotto import ModificaPrincipaleProdotto
            self.modificaPrincipaleProdotto = QtWidgets.QFrame()
            self.ui = ModificaPrincipaleProdotto()
            self.ui.setupUi(self.modificaPrincipaleProdotto, self.prodottoTrovato)
            self.modificaPrincipaleProdotto.show()
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