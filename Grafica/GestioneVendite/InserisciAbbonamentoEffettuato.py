from PyQt5 import QtCore, QtGui, QtWidgets


class InserisciAbbonamentoEffettuato(object):

    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(407, 201)
        Frame.setStyleSheet("QFrame{\n"
                            "background-color: rgb(255, 255, 255);\n"
                            "}")
        Frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame = Frame
        self.label_4 = QtWidgets.QLabel(Frame)
        self.label_4.setGeometry(QtCore.QRect(10, 20, 381, 31))
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
        self.pushButtonGestioneVenditePrincipale = QtWidgets.QPushButton(Frame)
        self.pushButtonGestioneVenditePrincipale.setGeometry(QtCore.QRect(130, 130, 151, 41))
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
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Images\\wallet.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonGestioneVenditePrincipale.setIcon(icon)
        self.pushButtonGestioneVenditePrincipale.setCheckable(False)
        self.pushButtonGestioneVenditePrincipale.setObjectName("pushButton_7")
        self.label_5 = QtWidgets.QLabel(Frame)
        self.label_5.setGeometry(QtCore.QRect(0, 60, 401, 61))
        self.label_5.setStyleSheet("QLabel{\n"
                                   "font-family: Helvetica, sans-serif;\n"
                                   "font-weight: 400;\n"
                                   "font-size: 15px\n"
                                   "}")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.pushButtonGestioneVenditePrincipale.clicked.connect(self.openGestioneVenditePrincipale)

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Fumetteria - Inserimento Effettuato"))
        self.label_4.setText(_translate("Frame", "INSERIMENTO EFFETTUATO"))
        self.pushButtonGestioneVenditePrincipale.setText(_translate("Frame", "Gestione"))
        self.label_5.setText(_translate("Frame", "Il cliente è stato abbonato con successo.\n"
                                                 " Cliccare sul pulsante per tornare alla gestione delle vendite."))

    # Metodo che permette di ritornare all'interfaccia GestioneVenditePrincipale.
    def openGestioneVenditePrincipale(self):
        from Grafica.GestioneVendite.GestioneVenditePrincipale import GestioneVenditePrincipale
        self.gestioneVenditePrincipale = QtWidgets.QFrame()
        self.ui = GestioneVenditePrincipale()
        self.ui.setupUi(self.gestioneVenditePrincipale)
        self.gestioneVenditePrincipale.show()
        self.frame.close()
