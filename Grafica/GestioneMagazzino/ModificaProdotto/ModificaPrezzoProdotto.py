from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


class ModificaPrezzoProdotto(object):

    def setupUi(self, Frame, prodotto):

        self.prodottoTrovato = prodotto
        Frame.setObjectName("Frame")
        Frame.resize(387, 246)
        Frame.setStyleSheet("QFrame{\n"
                            "background-color: rgb(255, 255, 255);\n"
                            "}")
        Frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame = Frame
        self.label_3 = QtWidgets.QLabel(Frame)
        self.label_3.setGeometry(QtCore.QRect(10, 70, 391, 31))
        self.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_3.setStyleSheet("QLabel{\n"
                                   "font-family: Helvetica, sans-serif;\n"
                                   "font-weight: 400;\n"
                                   "font-size: 16px\n"
                                   "}")
        self.label_3.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
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
        self.pushButtonModifica = QtWidgets.QPushButton(Frame)
        self.pushButtonModifica.setGeometry(QtCore.QRect(10, 150, 371, 31))
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
        self.doubleSpinBoxPrezzo = QtWidgets.QDoubleSpinBox(Frame)
        self.doubleSpinBoxPrezzo.setGeometry(QtCore.QRect(330, 100, 51, 31))
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
        self.horizontalSlider_2.setGeometry(QtCore.QRect(10, 100, 301, 31))
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
        icon.addPixmap(QtGui.QPixmap("Images\\log.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonLogout.setIcon(icon)
        self.pushButtonLogout.setCheckable(False)
        self.pushButtonLogout.setObjectName("pushButton_7")
        self.pushButtonModificaPrincipale = QtWidgets.QPushButton(Frame)
        self.pushButtonModificaPrincipale.setGeometry(QtCore.QRect(160, 200, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonModificaPrincipale.setFont(font)
        self.pushButtonModificaPrincipale.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButtonModificaPrincipale.setStyleSheet("QPushButton{\n"
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
        self.pushButtonModificaPrincipale.setIcon(icon1)
        self.pushButtonModificaPrincipale.setObjectName("pushButton_8")
        self.pushButtonModificaPrincipale.clicked.connect(self.openModificaPrincipaleProdotto)
        self.pushButtonLogout.clicked.connect(self.openLogin)
        self.pushButtonModifica.clicked.connect(self.clickModifica)

        self.retranslateUi(Frame)
        self.horizontalSlider_2.sliderMoved['int'].connect(self.doubleSpinBoxPrezzo.setValue)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Fumetteria - Modifica Prezzo Prodotto"))
        self.label_3.setText(_translate("Frame", "Modifica prezzo:"))
        self.label_4.setText(_translate("Frame", "MODIFICA PREZZO"))
        self.pushButtonModifica.setText(_translate("Frame", "Modifica"))
        self.pushButtonLogout.setText(_translate("Frame", " Logout"))
        self.pushButtonModificaPrincipale.setText(_translate("Frame", " Indietro"))

    # Metodo che permette di modificare il prezzo del prodotto trovato
    # dopo aver cliccato il pulsante Modifica.
    # Nel caso in cui il prezzo immesso è zero, viene visualizzata
    # una finestra di errore.
    # Nel caso in cui il prodotto abbia un'offerta e il prezzo immesso
    # risulta maggiore del prezzo dell'offerta, l'offerta viene eliminata e
    # viene sovrascritto il prodotto con gli attributi cambiati
    # all'interno del file di testo "Magazzino.txt" tramite
    # il metodo "sovrascriviDati" della classe
    # Magazzino per cambiare l'attributo prezzo del prodotto trovato
    # all'interno del file di testo "Magazzino.txt" a seguito della
    # comparsa di una finestra di avviso.
    # Anche nel caso generale i dati vengono sovrascritti all'interno del
    # file di testo.
    # Successivamente viene richiamato il metodo "self.openModificaEffettuata".
    def clickModifica(self):

        prezzoInserito = self.doubleSpinBoxPrezzo.text()

        # Risolve un problema d'incompatibilità dello spinBox
        # tra le versione di Windows10 e Windows11.
        if "," in prezzoInserito:
            prezzoVector = prezzoInserito.split(",")
            prezzoInserito = prezzoVector[0] + "." + prezzoVector[1]

        if float(prezzoInserito) != 0.00:
            if float(prezzoInserito) != float(self.prodottoTrovato.getPrezzo()):
                if str(self.prodottoTrovato.getOfferta()) != "True" or float(prezzoInserito) > float(
                        self.prodottoTrovato.getPrezzoOfferta()):
                    replacement = str(
                        self.prodottoTrovato.getNomeProdotto() + "-" + self.prodottoTrovato.getQuantitaMagazzino()
                        + "-" + prezzoInserito + "-" + self.prodottoTrovato.getCodiceSeriale()
                        + "-" + self.prodottoTrovato.getOfferta() + "-" + self.prodottoTrovato.getTipoOfferta()
                        + "-" + self.prodottoTrovato.getPrezzoOfferta() + "-" + self.prodottoTrovato.getDataScadenzaOfferta())
                    data = self.prodottoTrovato.getProdotto()
                    self.prodottoTrovato.sovrascriviDati(data, replacement)
                    self.openModificaEffettuata()
                else:
                    if float(prezzoInserito) <= float(self.prodottoTrovato.getPrezzoOfferta()):
                        replacement = str(
                            self.prodottoTrovato.getNomeProdotto() + "-" + self.prodottoTrovato.getQuantitaMagazzino()
                            + "-" + prezzoInserito + "-" + self.prodottoTrovato.getCodiceSeriale() + "-"
                            + "None-None-None-None")
                        data = self.prodottoTrovato.getProdotto()
                        self.prodottoTrovato.sovrascriviDati(data, replacement)
                        self.ErrorConflittoPrezzi()
                        self.openModificaEffettuata()
            else:
                self.ErrorConflittoPrezzi()
        else:
            self.ErrorPrezzoNullo()

    # Metodo che fa visualizzare a schermo l'interfaccia ModificaEffettuata.
    def openModificaEffettuata(self):
        from Grafica.GestioneMagazzino.ModificaProdotto.ModificaEffettuata import ModificaEffettuata
        self.modificaEffettuta = QtWidgets.QFrame()
        self.ui = ModificaEffettuata()
        self.ui.setupUi(self.modificaEffettuta)
        self.modificaEffettuta.show()
        self.frame.close()

    # Metodo che riporta l'utente all'interno della schermata ModificaPrincipalePrincipale.
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

    def ErrorPrezzo(self):
        self.ErrorBox = QMessageBox()
        self.ErrorBox.setWindowTitle("Errore")
        self.ErrorBox.setText("Il prezzo immessa è uguale al \nprezzo immesso in precedenza")
        self.ErrorBox.setStyleSheet(
            "QLabel{min-width:300 px; font-size: 14px; font-family: Helvetica, Sans-Serif; } QPushButton:hover{"
            "background-color: #14626c;color:white; }QPushButton{ width:40px; height:20px; font-size: 10px; "
            "font-family: Helvetica, Sans-Serif; border: 1px solid black; border-radius: 5px; }")
        self.ErrorBox.exec()

    def ErrorPrezzoNullo(self):
        self.ErrorBox = QMessageBox()
        self.ErrorBox.setWindowTitle("Errore")
        self.ErrorBox.setText("Il prezzo immesso non può essere 0.00")
        self.ErrorBox.setStyleSheet(
            "QLabel{min-width:300 px; font-size: 14px; font-family: Helvetica, Sans-Serif; } QPushButton:hover{"
            "background-color: #14626c;color:white; }QPushButton{ width:40px; height:20px; font-size: 10px; "
            "font-family: Helvetica, Sans-Serif; border: 1px solid black; border-radius: 5px; }")
        self.ErrorBox.exec()

    def ErrorConflittoPrezzi(self):
        self.ErrorBox = QMessageBox()
        self.ErrorBox.setWindowTitle("Rimozione Offerta")
        self.ErrorBox.setText("L'offerta è stata rimossa perchè il prezzo immesso\nè maggiore del prezzo "
                              "relativo all'offerta")
        self.ErrorBox.setStyleSheet(
            "QLabel{min-width:300 px; font-size: 14px; font-family: Helvetica, Sans-Serif; } QPushButton:hover{"
            "background-color: #14626c;color:white; }QPushButton{ width:40px; height:20px; font-size: 10px; "
            "font-family: Helvetica, Sans-Serif; border: 1px solid black; border-radius: 5px; }")
        self.ErrorBox.exec()
