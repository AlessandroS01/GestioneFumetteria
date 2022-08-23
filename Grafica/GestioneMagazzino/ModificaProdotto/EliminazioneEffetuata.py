from PyQt5 import QtCore, QtGui, QtWidgets


class EliminazioneEffettuata(object):

    def setupUi(self, Frame):

        Frame.setObjectName("Frame")
        Frame.resize(407, 195)
        Frame.setStyleSheet("QFrame{\n"
                            "background-color: rgb(255, 255, 255);\n"
                            "}")
        Frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame = Frame
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
        self.pushButtonGestioneMagazzinoPrincipale = QtWidgets.QPushButton(Frame)
        self.pushButtonGestioneMagazzinoPrincipale.setGeometry(QtCore.QRect(130, 130, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonGestioneMagazzinoPrincipale.setFont(font)
        self.pushButtonGestioneMagazzinoPrincipale.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButtonGestioneMagazzinoPrincipale.setStyleSheet("QPushButton{\n"
                                               "border: 2px solid black;\n"
                                               "border-radius: 10px;\n"
                                               "}\n"
                                               "QPushButton:hover{\n"
                                               "\n"
                                               "background-color: #14626c;\n"
                                               "color:white;\n"
                                               "}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Images\\warehouse.png"), QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        self.pushButtonGestioneMagazzinoPrincipale.setIcon(icon)
        self.pushButtonGestioneMagazzinoPrincipale.setCheckable(False)
        self.pushButtonGestioneMagazzinoPrincipale.setObjectName("pushButton_7")
        self.label_5 = QtWidgets.QLabel(Frame)
        self.label_5.setGeometry(QtCore.QRect(0, 60, 401, 61))
        self.label_5.setStyleSheet("QLabel{\n"
                                   "font-family: Helvetica, sans-serif;\n"
                                   "font-weight: 400;\n"
                                   "font-size: 15px\n"
                                   "}")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.pushButtonGestioneMagazzinoPrincipale.clicked.connect(self.openGestioneMagazzinoPrincipale)

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Fumetteria - Eliminazione Effettuata"))
        self.label_4.setText(_translate("Frame", "PRODOTTO ELIMINATO "))
        self.pushButtonGestioneMagazzinoPrincipale.setText(_translate("Frame", "Magazzino"))
        self.label_5.setText(_translate("Frame", "Il prodotto è stato eliminato con successo.\n"
                                                 " Cliccare sul pulsante per tornare alla gestione del magazzino"))

    # Metodo che permette di ritornare all'interfaccia GestioneMagazzinoPrincipale.
    def openGestioneMagazzinoPrincipale(self):
        from Grafica.GestioneMagazzino.GestioneMagazzinoPrincipale import GestioneMagazzinoPrincipale
        self.gestioneMagazzinoPrincipale = QtWidgets.QFrame()
        self.ui = GestioneMagazzinoPrincipale()
        self.ui.setupUi(self.gestioneMagazzinoPrincipale)
        self.gestioneMagazzinoPrincipale.show()
        self.frame.close()

