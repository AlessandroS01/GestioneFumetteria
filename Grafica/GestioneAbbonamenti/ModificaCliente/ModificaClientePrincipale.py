from PyQt5 import QtCore, QtGui, QtWidgets


class ModificaClientePrincipale(object):
    def setupUi(self, Frame, abbonamento):
        self.abbonamentoTrovato = abbonamento
        Frame.setObjectName("Frame")
        Frame.resize(448, 309)
        Frame.setStyleSheet("QFrame{\n"
                            "background-color: rgb(255, 255, 255);\n"
                            "}")
        Frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame = Frame
        self.label_4 = QtWidgets.QLabel(Frame)
        self.label_4.setGeometry(QtCore.QRect(10, 20, 431, 31))
        self.label_4.setStyleSheet("QLabel{\n"
                                    "font-family: impact, sans-serif;\n"
                                    "font-size:30px;\n"
                                    "\n"
                                    "}")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.line = QtWidgets.QFrame(Frame)
        self.line.setGeometry(QtCore.QRect(50, 50, 321, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.pushButtonLogout = QtWidgets.QPushButton(Frame)
        self.pushButtonLogout.setGeometry(QtCore.QRect(10, 270, 141, 31))
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
        self.pushButtonRicercaSuccesso = QtWidgets.QPushButton(Frame)
        self.pushButtonRicercaSuccesso.setGeometry(QtCore.QRect(160, 270, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonRicercaSuccesso.setFont(font)
        self.pushButtonRicercaSuccesso.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButtonRicercaSuccesso.setStyleSheet("QPushButton{\n"
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
        self.pushButtonRicercaSuccesso.setIcon(icon1)
        self.pushButtonRicercaSuccesso.setObjectName("pushButton_4")
        self.pushButtonNomeCognome = QtWidgets.QPushButton(Frame)
        self.pushButtonNomeCognome.setGeometry(QtCore.QRect(20, 120, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonNomeCognome.setFont(font)
        self.pushButtonNomeCognome.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButtonNomeCognome.setStyleSheet("QPushButton{\n"
                                        "border: 2px solid black;\n"
                                        "border-radius: 10px;\n"
                                        "}\n"
                                        "QPushButton:hover{\n"
                                        "\n"
                                        "background-color: #14626c;\n"
                                        "color:white;\n"
                                        "}")
        self.pushButtonNomeCognome.setCheckable(False)
        self.pushButtonNomeCognome.setObjectName("pushButton_8")
        self.pushButtonModificaEmail = QtWidgets.QPushButton(Frame)
        self.pushButtonModificaEmail.setGeometry(QtCore.QRect(20, 180, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonModificaEmail.setFont(font)
        self.pushButtonModificaEmail.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButtonModificaEmail.setStyleSheet("QPushButton{\n"
                                        "border: 2px solid black;\n"
                                        "border-radius: 10px;\n"
                                        "}\n"
                                        "QPushButton:hover{\n"
                                        "\n"
                                        "background-color: #14626c;\n"
                                        "color:white;\n"
                                        "}")
        self.pushButtonModificaEmail.setCheckable(False)
        self.pushButtonModificaEmail.setObjectName("pushButton_9")
        self.pushButtonModificaCodiceFiscale = QtWidgets.QPushButton(Frame)
        self.pushButtonModificaCodiceFiscale.setGeometry(QtCore.QRect(230, 120, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonModificaCodiceFiscale.setFont(font)
        self.pushButtonModificaCodiceFiscale.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButtonModificaCodiceFiscale.setStyleSheet("QPushButton{\n"
                                        "border: 2px solid black;\n"
                                        "border-radius: 10px;\n"
                                        "}\n"
                                        "QPushButton:hover{\n"
                                        "\n"
                                        "background-color: #14626c;\n"
                                        "color:white;\n"
                                        "}")
        self.pushButtonModificaCodiceFiscale.setCheckable(False)
        self.pushButtonModificaCodiceFiscale.setObjectName("pushButton_12")
        self.pushButton_13 = QtWidgets.QPushButton(Frame)
        self.pushButton_13.setGeometry(QtCore.QRect(230, 180, 201, 51))
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
        self.label = QtWidgets.QLabel(Frame)
        self.label.setGeometry(QtCore.QRect(10, 60, 431, 41))
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setStyleSheet("QLabel{\n"
                                "font-family: Helvetica, sans-serif;\n"
                                "font-weight: 400;\n"
                                "font-size: 16px\n"
                                "}")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButtonLogout.clicked.connect(self.openLogin)
        self.pushButtonRicercaSuccesso.clicked.connect(self.openRicercaSuccesso)
        self.pushButtonNomeCognome.clicked.connect(self.openModificaNomeCognomeCliente)
        self.pushButtonModificaEmail.clicked.connect(self.openModificaEmailCliente)
        self.pushButtonModificaCodiceFiscale.clicked.connect(self.openModificaCodiceFiscaleCliente)

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Fumetteria - Modifica Cliente"))
        self.label_4.setText(_translate("Frame", "MODIFICA CLIENTE"))
        self.pushButtonLogout.setText(_translate("Frame", " Logout"))
        self.pushButtonRicercaSuccesso.setText(_translate("Frame", " Indietro"))
        self.pushButtonNomeCognome.setText(_translate("Frame", "Modifica Nome/\n"
                                            "Cognome Cliente"))
        self.pushButtonModificaEmail.setText(_translate("Frame", "Modifica\n"
                                            "Email"))
        self.pushButtonModificaCodiceFiscale.setText(_translate("Frame", "Modifica \n"
                                            "Codice Fiscale"))
        self.pushButton_13.setText(_translate("Frame", "Modifica \n"
                                                " Telefono"))
        self.label.setText(_translate("Frame", "Seleziona una delle opzioni per modificare il le informazioni\n"
                                    "relative al cliente"))

    def openLogin(self):
        from Grafica.GestioneLogin.LoginAmministratore import LoginAmministratore
        self.login = QtWidgets.QFrame()
        self.ui = LoginAmministratore()
        self.ui.setupUi(self.login)
        self.login.show()
        self.frame.close()

    def openRicercaSuccesso(self):
        from Grafica.GestioneAbbonamenti.RicercaAbbonamentoSuccesso import RicercaAbbonamentoSuccesso
        self.ricercaAbbonamentoSuccesso = QtWidgets.QFrame()
        self.ui = RicercaAbbonamentoSuccesso()
        self.ui.setupUi(self.ricercaAbbonamentoSuccesso,self.abbonamentoTrovato)
        self.ricercaAbbonamentoSuccesso.show()
        self.frame.close()

    def openModificaNomeCognomeCliente(self):
        from Grafica.GestioneAbbonamenti.ModificaCliente.ModificaNomeCognomeCliente import ModificaNomeCognomeCliente
        self.modificaNomeCognomeCliente = QtWidgets.QFrame()
        self.ui = ModificaNomeCognomeCliente()
        self.ui.setupUi(self.modificaNomeCognomeCliente,self.abbonamentoTrovato)
        self.modificaNomeCognomeCliente.show()
        self.frame.close()

    def openModificaEmailCliente(self):
        from Grafica.GestioneAbbonamenti.ModificaCliente.ModificaEmailCliente import ModificaEmailCliente
        self.modificaEmailCliente = QtWidgets.QFrame()
        self.ui = ModificaEmailCliente()
        self.ui.setupUi(self.modificaEmailCliente,self.abbonamentoTrovato)
        self.modificaEmailCliente.show()
        self.frame.close()
    def openModificaCodiceFiscaleCliente(self):
        from Grafica.GestioneAbbonamenti.ModificaCliente.ModificaCodiceFiscaleCliente import ModificaCodiceFiscaleCliente
        self.modificaCodiceFiscaleCliente = QtWidgets.QFrame()
        self.ui = ModificaCodiceFiscaleCliente()
        self.ui.setupUi(self.modificaCodiceFiscaleCliente,self.abbonamentoTrovato)
        self.modificaCodiceFiscaleCliente.show()
        self.frame.close()