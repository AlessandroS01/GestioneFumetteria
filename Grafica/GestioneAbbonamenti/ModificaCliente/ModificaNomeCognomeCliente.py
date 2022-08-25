from PyQt5 import QtCore, QtGui, QtWidgets


class ModificaNomeCognomeCliente(object):

    def setupUi(self, Frame,abbonamento):
        self.abbonamentoTrovato=abbonamento
        Frame.setObjectName("Frame")
        Frame.resize(411, 331)
        Frame.setStyleSheet("QFrame{\n"
                            "background-color: rgb(255, 255, 255);\n"
                            "}")
        Frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame = Frame
        self.label = QtWidgets.QLabel(Frame)
        self.label.setGeometry(QtCore.QRect(10, 150, 391, 31))
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setStyleSheet("QLabel{\n"
                                "font-family: Helvetica, sans-serif;\n"
                                "font-weight: 400;\n"
                                "font-size: 16px\n"
                                "}")
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Frame)
        self.lineEdit.setGeometry(QtCore.QRect(10, 190, 391, 31))
        self.lineEdit.setStyleSheet("QLineEdit{\n"
                                    "border: 2px solid black;\n"
                                    "border-radius: 6px;\n"
                                    "}")
        self.lineEdit.setObjectName("lineEdit")
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
        self.pushButtonLogout.setGeometry(QtCore.QRect(10, 290, 141, 31))
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
        icon.addPixmap(QtGui.QPixmap("C:\\Users\\dsant\\Desktop\\Mockup\\log.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonLogout.setIcon(icon)
        self.pushButtonLogout.setCheckable(False)
        self.pushButtonLogout.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(Frame)
        self.pushButton_6.setGeometry(QtCore.QRect(10, 230, 391, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_6.setStyleSheet("QPushButton{\n"
                                        "border: 2px solid black;\n"
                                        "border-radius: 10px;\n"
                                        "}\n"
                                        "QPushButton:hover{\n"
                                        "\n"
                                        "background-color: #14626c;\n"
                                        "color:white;\n"
                                        "}")
        self.pushButton_6.setCheckable(False)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButtonModificaClientePrinciaple = QtWidgets.QPushButton(Frame)
        self.pushButtonModificaClientePrinciaple.setGeometry(QtCore.QRect(160, 290, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonModificaClientePrinciaple.setFont(font)
        self.pushButtonModificaClientePrinciaple.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButtonModificaClientePrinciaple.setStyleSheet("QPushButton{\n"
                                        "border: 2px solid black;\n"
                                        "border-radius: 10px;\n"
                                        "}\n"
                                        "QPushButton:hover{\n"
                                        "\n"
                                        "background-color: #14626c;\n"
                                        "color:white;\n"
                                        "}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:\\Users\\dsant\\Desktop\\Mockup\\left.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonModificaClientePrinciaple.setIcon(icon1)
        self.pushButtonModificaClientePrinciaple.setObjectName("pushButton_4")
        self.radioButton_2 = QtWidgets.QRadioButton(Frame)
        self.radioButton_2.setGeometry(QtCore.QRect(11, 120, 91, 21))
        self.radioButton_2.setStyleSheet("QRadioButton{\n"
                                            "font-family: Helvetica, sans-serif;\n"
                                            "font-size:13px;\n"
                                            "}")
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton = QtWidgets.QRadioButton(Frame)
        self.radioButton.setGeometry(QtCore.QRect(11, 96, 91, 21))
        self.radioButton.setStyleSheet("QRadioButton{\n"
                                        "font-family: Helvetica, sans-serif;\n"
                                        "font-size:13px;\n"
                                        "}")
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName("radioButton")
        self.label_2 = QtWidgets.QLabel(Frame)
        self.label_2.setGeometry(QtCore.QRect(10, 60, 391, 31))
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setStyleSheet("QLabel{\n"
                                    "font-family: Helvetica, sans-serif;\n"
                                    "font-weight: 400;\n"
                                    "font-size: 16px\n"
                                    "}")
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.pushButtonLogout.clicked.connect(self.openLogin)
        self.pushButtonModificaClientePrinciaple.clicked.connect(self.openModificaClientePrincipale)

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Fumetteria - Modifica Generalità Cliente"))
        self.label.setText(_translate("Frame", "Inserisci il nome/cognome del cliente"))
        self.label_4.setText(_translate("Frame", "MODIFICA GENERALITA\' CLIENTE"))
        self.pushButtonLogout.setText(_translate("Frame", " Logout"))
        self.pushButton_6.setText(_translate("Frame", "Modifica"))
        self.pushButtonModificaClientePrinciaple.setText(_translate("Frame", " Indietro"))
        self.radioButton_2.setText(_translate("Frame", "Cognome"))
        self.radioButton.setText(_translate("Frame", "Nome"))
        self.label_2.setText(_translate("Frame", "Seleziona quale campo del cliente vuoi modificare:"))

    def openLogin(self):
        from Grafica.GestioneLogin.LoginAmministratore import LoginAmministratore
        self.login = QtWidgets.QFrame()
        self.ui = LoginAmministratore()
        self.ui.setupUi(self.login)
        self.login.show()
        self.frame.close()

    def openModificaClientePrincipale(self):
        from Grafica.GestioneAbbonamenti.ModificaCliente.ModificaClientePrincipale import ModificaClientePrincipale
        self.modificaClientePrincipale = QtWidgets.QFrame()
        self.ui = ModificaClientePrincipale()
        self.ui.setupUi(self.modificaClientePrincipale, self.abbonamentoTrovato)
        self.modificaClientePrincipale.show()
        self.frame.close()