from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


class InserisciDataIncasso(object):

    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(387, 241)
        Frame.setStyleSheet("QFrame{\n"
                            "background-color: rgb(255, 255, 255);\n"
                            "}")
        Frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame = Frame
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
        self.line.setGeometry(QtCore.QRect(20, 50, 351, 20))
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
        icon.addPixmap(QtGui.QPixmap("Images\\log.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonLogout.setIcon(icon)
        self.pushButtonLogout.setCheckable(False)
        self.pushButtonLogout.setObjectName("pushButton_5")
        self.pushButtonGestioneVenditePrincipale = QtWidgets.QPushButton(Frame)
        self.pushButtonGestioneVenditePrincipale.setGeometry(QtCore.QRect(160, 200, 141, 31))
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
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Images\\left.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonGestioneVenditePrincipale.setIcon(icon1)
        self.pushButtonGestioneVenditePrincipale.setObjectName("pushButton_4")
        self.pushButtonRicerca = QtWidgets.QPushButton(Frame)
        self.pushButtonRicerca.setGeometry(QtCore.QRect(10, 150, 371, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonRicerca.setFont(font)
        self.pushButtonRicerca.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButtonRicerca.setStyleSheet("QPushButton{\n"
                                             "border: 2px solid black;\n"
                                             "border-radius: 10px;\n"
                                             "}\n"
                                             "QPushButton:hover{\n"
                                             "\n"
                                             "background-color: #14626c;\n"
                                             "color:white;\n"
                                             "}")
        self.pushButtonRicerca.setCheckable(False)
        self.pushButtonRicerca.setObjectName("pushButton_6")
        self.label_3 = QtWidgets.QLabel(Frame)
        self.label_3.setGeometry(QtCore.QRect(10, 70, 371, 21))
        self.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_3.setStyleSheet("QLabel{\n"
                                   "font-family: Helvetica, sans-serif;\n"
                                   "font-weight: 400;\n"
                                   "font-size: 16px\n"
                                   "}")
        self.label_3.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.dateEdit = QtWidgets.QDateEdit(Frame)
        self.dateEdit.setGeometry(QtCore.QRect(10, 100, 371, 31))
        self.dateEdit.setStyleSheet("QDateEdit{\n"
                                    "border: 2px solid black;\n"
                                    "border-radius: 6px;\n"
                                    "}")
        self.dateEdit.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.dateEdit.setCalendarPopup(False)
        self.dateEdit.setDate(QtCore.QDate(2023, 1, 1))
        self.dateEdit.setObjectName("dateEdit")
        self.pushButtonLogout.clicked.connect(self.openLogin)
        self.pushButtonGestioneVenditePrincipale.clicked.connect(self.openGestioneVenditePrincipale)
        self.pushButtonRicerca.clicked.connect(self.clickRicerca)

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Fumetteria - Inserisci Data Incasso"))
        self.label_4.setText(_translate("Frame", "DATA INCASSO"))
        self.pushButtonLogout.setText(_translate("Frame", " Logout"))
        self.pushButtonGestioneVenditePrincipale.setText(_translate("Frame", " Indietro"))
        self.pushButtonRicerca.setText(_translate("Frame", " Ricerca"))
        self.label_3.setText(_translate("Frame", "Inserisci la data per visualizzare l\'incasso:"))

    # Metodo che permette di ritornare all'interfaccia iniziale
    # del programma, ovvero LoginAmministratore.
    def openLogin(self):
        from Grafica.GestioneLogin.LoginAmministratore import LoginAmministratore
        self.login = QtWidgets.QFrame()
        self.ui = LoginAmministratore()
        self.ui.setupUi(self.login)
        self.login.show()
        self.frame.close()

    # Metodo che permette di ritornare all'interfaccia GestioneVenditePrincipale.
    def openGestioneVenditePrincipale(self):
        from Grafica.GestioneVendite.GestioneVenditePrincipale import GestioneVenditePrincipale
        self.gestioneVenditePrincipale = QtWidgets.QFrame()
        self.ui = GestioneVenditePrincipale()
        self.ui.setupUi(self.gestioneVenditePrincipale)
        self.gestioneVenditePrincipale.show()
        self.frame.close()

    # Metodo che permette di visualizza l'incasso durante la giornata immessa.
    # Nel caso in cui non fossero state effettuate vendite, viene visualizzata una schermata di errore.
    # Nel caso in cui esistessero invece,
    # viene visualizzata una schermata contenente l'incasso durante quella giornata
    # tramite "self.openIncassoGiornaliero".
    def clickRicerca(self):
        from GestioneVendite.GestoreVendite import GestoreVendite
        gestoreVendite = GestoreVendite()

        giornoText = self.dateEdit.date().day()
        meseText = self.dateEdit.date().month()
        annoText = self.dateEdit.date().year()

        dataImmessa = str(str(giornoText) + "/" +
                          str(meseText) + "/" +
                          str(annoText))

        ritorno = gestoreVendite.getVenditeGiornata(dataImmessa)

        if len(ritorno[0]) != 0:
            self.openIncassoGiornaliero(dataImmessa, gestoreVendite)
        else:
            self.ErrorData()

    # Metodo che fa visualizzare a schermo l'interfaccia IncassoGiornaliero.
    def openIncassoGiornaliero(self, dataEmissione, gestoreVendite):
        from Grafica.GestioneVendite.IncassoGiornaliero import IncassoGiornaliero
        self.incassoGiornaliero = QtWidgets.QFrame()
        self.ui = IncassoGiornaliero()
        self.ui.setupUi(self.incassoGiornaliero, dataEmissione, gestoreVendite)
        self.incassoGiornaliero.show()
        self.frame.close()

    def ErrorData(self):
        self.ErrorBox = QMessageBox()
        self.ErrorBox.setWindowTitle("Errore")
        self.ErrorBox.setText("Durante la giornata immessa non sono state\neffettuate vendite.")
        self.ErrorBox.setStyleSheet(
            "QLabel{min-width:300 px; font-size: 14px; font-family: Helvetica, Sans-Serif; } QPushButton:hover{"
            "background-color: #14626c;color:white; }QPushButton{ width:40px; height:20px; font-size: 10px; "
            "font-family: Helvetica, Sans-Serif; border: 1px solid black; border-radius: 5px; }")
        self.ErrorBox.exec()
