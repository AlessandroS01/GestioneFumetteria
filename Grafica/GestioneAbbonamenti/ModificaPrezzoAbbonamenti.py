from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


class ModificaPrezzoAbbonamenti(object):

    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(418, 243)
        Frame.setStyleSheet("QFrame{\n"
                            "background-color: rgb(255, 255, 255);\n"
                            "}")
        Frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame = Frame
        self.label_4 = QtWidgets.QLabel(Frame)
        self.label_4.setGeometry(QtCore.QRect(10, 20, 401, 31))
        self.label_4.setStyleSheet("QLabel{\n"
                                   "font-family: impact, sans-serif;\n"
                                   "font-size:30px;\n"
                                   "\n"
                                   "}")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.line = QtWidgets.QFrame(Frame)
        self.line.setGeometry(QtCore.QRect(30, 50, 361, 20))
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
        icon.addPixmap(QtGui.QPixmap("Images\\log.png"), QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        self.pushButtonLogout.setIcon(icon)
        self.pushButtonLogout.setCheckable(False)
        self.pushButtonLogout.setObjectName("pushButton_5")
        self.pushButtonGestioneAbbonamentiPrincipale = QtWidgets.QPushButton(Frame)
        self.pushButtonGestioneAbbonamentiPrincipale.setGeometry(QtCore.QRect(160, 200, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonGestioneAbbonamentiPrincipale.setFont(font)
        self.pushButtonGestioneAbbonamentiPrincipale.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButtonGestioneAbbonamentiPrincipale.setStyleSheet("QPushButton{\n"
                                                                   "border: 2px solid black;\n"
                                                                   "border-radius: 10px;\n"
                                                                   "}\n"
                                                                   "QPushButton:hover{\n"
                                                                   "\n"
                                                                   "background-color: #14626c;\n"
                                                                   "color:white;\n"
                                                                   "}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Images\\left.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonGestioneAbbonamentiPrincipale.setIcon(icon1)
        self.pushButtonGestioneAbbonamentiPrincipale.setObjectName("pushButton_4")
        self.pushButtonModifica = QtWidgets.QPushButton(Frame)
        self.pushButtonModifica.setGeometry(QtCore.QRect(10, 150, 391, 31))
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
        self.label_2 = QtWidgets.QLabel(Frame)
        self.label_2.setGeometry(QtCore.QRect(10, 70, 371, 31))
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setStyleSheet("QLabel{\n"
                                   "font-family: Helvetica, sans-serif;\n"
                                   "font-weight: 400;\n"
                                   "font-size: 16px\n"
                                   "}")
        self.label_2.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.doubleSpinBoxPrezzo = QtWidgets.QDoubleSpinBox(Frame)
        self.doubleSpinBoxPrezzo.setGeometry(QtCore.QRect(350, 100, 51, 31))
        self.doubleSpinBoxPrezzo.setStyleSheet("QDoubleSpinBox{\n"
                                               "border: 2px solid black;\n"
                                               "border-radius: 6px;\n"
                                               "}\n"
                                               "QDoubleSpinBox::up-button{\n"
                                               "\n"
                                               "\n"
                                               "}\n"
                                               "\n"
                                               "\n"
                                               "\n"
                                               "")
        self.doubleSpinBoxPrezzo.setWrapping(False)
        self.doubleSpinBoxPrezzo.setFrame(True)
        self.doubleSpinBoxPrezzo.setAlignment(QtCore.Qt.AlignCenter)
        self.doubleSpinBoxPrezzo.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.doubleSpinBoxPrezzo.setSpecialValueText("")
        self.doubleSpinBoxPrezzo.setMaximum(299.99)
        self.doubleSpinBoxPrezzo.setObjectName("doubleSpinBox_2")
        self.horizontalSlider_2 = QtWidgets.QSlider(Frame)
        self.horizontalSlider_2.setGeometry(QtCore.QRect(10, 100, 321, 31))
        self.horizontalSlider_2.setStyleSheet("QSlider::groove:horizontal {\n"
                                              "    border: 1px solid black;\n"
                                              "    height: 10px;\n"
                                              "    background: white;\n"
                                              "    margin: 0px;\n"
                                              "    border-radius: 4px;\n"
                                              "}\n"
                                              "QSlider::handle:horizontal {\n"
                                              "    background: #14626c;\n"
                                              "    border: 1px solid black;\n"
                                              "    width: 22px;\n"
                                              "    height: 8px;\n"
                                              "    border-radius: 4px;\n"
                                              "}")
        self.horizontalSlider_2.setMaximum(299)
        self.horizontalSlider_2.setSingleStep(1)
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setObjectName("horizontalSlider_2")
        self.pushButtonGestioneAbbonamentiPrincipale.clicked.connect(self.openGestioneAbbonamentiPrincipale)
        self.pushButtonLogout.clicked.connect(self.openLogin)
        self.pushButtonModifica.clicked.connect(self.clickModifica)

        self.retranslateUi(Frame)
        self.horizontalSlider_2.sliderMoved['int'].connect(self.doubleSpinBoxPrezzo.setValue)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Fumetteria - Gestione Abbonamenti"))
        self.label_4.setText(_translate("Frame", "MODIFICA PREZZO ABBONAMENTI"))
        self.pushButtonLogout.setText(_translate("Frame", " Logout"))
        self.pushButtonGestioneAbbonamentiPrincipale.setText(_translate("Frame", " Indietro"))
        self.pushButtonModifica.setText(_translate("Frame", "Modifica"))
        self.label_2.setText(_translate("Frame", "Prezzo imposto agli abbonamenti:"))

    # Metodo che permette di ritornare all'interfaccia iniziale
    # del programma, ovvero LoginAmministratore.
    def openLogin(self):
        from Grafica.GestioneLogin.LoginAmministratore import LoginAmministratore
        self.login = QtWidgets.QFrame()
        self.ui = LoginAmministratore()
        self.ui.setupUi(self.login)
        self.login.show()
        self.frame.close()

    # Metodo che permette di ritornare all'interfaccia GestioneAbbonamentiPrincipale.
    def openGestioneAbbonamentiPrincipale(self):
        from Grafica.GestioneAbbonamenti.GestioneAbbonamentiPrincipale import GestioneAbbonamentiPrincipale
        self.gestioneAbbonamentiPrincipale = QtWidgets.QFrame()
        self.ui = GestioneAbbonamentiPrincipale()
        self.ui.setupUi(self.gestioneAbbonamentiPrincipale)
        self.gestioneAbbonamentiPrincipale.show()
        self.frame.close()

    # Metodo che permette di modificare il prezzo degli abbonamenti.
    # Nel caso in cui il prezzo è uguale a quello precedente,
    # viene visualizzata una finestra di errore.
    # Nel caso in cui invece il codice immesso è utilizzabile,
    # viene richiamato il metodo "setPrezzoAbbonamento" della classe
    # GestioneAbbonamenti per cambiare l'attributo prezzoAbbonamento degli abbonamenti.
    # Successivamente viene richiamato il metodo "self.openModificaEffettuata".
    def clickModifica(self):

        from GestioneAbbonamenti.GestioneAbbonamenti import GestioneAbbonamenti
        prezzoInserito = self.doubleSpinBoxPrezzo.text()
        gestoreAbbonamenti = GestioneAbbonamenti()

        if float(prezzoInserito) != float(gestoreAbbonamenti.getPrezzoAbbonamento()):

            gestoreAbbonamenti.setPrezzoAbbonamento(prezzoInserito)
            self.openModificaEffettuata()

        else:
            self.ErrorPrezzoPrecedente()

    # Metodo che fa visualizzare a schermo l'interfaccia ModificaPrezzoAbbonamentiSuccesso.
    def openModificaEffettuata(self):
        from Grafica.GestioneAbbonamenti.ModificaPrezzoAbbonamentiSuccesso import ModificaPrezzoAbbonamentiSuccesso
        self.modificaEffettuta = QtWidgets.QFrame()
        self.ui = ModificaPrezzoAbbonamentiSuccesso()
        self.ui.setupUi(self.modificaEffettuta)
        self.modificaEffettuta.show()
        self.frame.close()

    def ErrorPrezzoPrecedente(self):
        self.ErrorBox = QMessageBox()
        self.ErrorBox.setWindowTitle("Errore")
        self.ErrorBox.setText("Il prezzo immesso non può essere \nuguale al prezzo precedente.")
        self.ErrorBox.setStyleSheet(
            "QLabel{min-width:300 px; font-size: 14px; font-family: Helvetica, Sans-Serif; } QPushButton:hover{"
            "background-color: #14626c;color:white; }QPushButton{ width:40px; height:20px; font-size: 10px; "
            "font-family: Helvetica, Sans-Serif; border: 1px solid black; border-radius: 5px; }")
        self.ErrorBox.exec()
