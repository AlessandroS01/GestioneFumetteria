from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


class RicercaProdottoSuccesso(object):

    def setupUi(self, Frame, prodotto):
        self.prodottoTrovato = prodotto
        Frame.setObjectName("Frame")
        Frame.resize(403, 395)
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
        icon.addPixmap(QtGui.QPixmap("Images\\log.png"), QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        self.pushButtonLogout.setIcon(icon)
        self.pushButtonLogout.setCheckable(False)
        self.pushButtonLogout.setObjectName("pushButton_5")
        self.pushButtonModifica = QtWidgets.QPushButton(Frame)
        self.pushButtonModifica.setGeometry(QtCore.QRect(20, 270, 361, 31))
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
        self.pushButtonRicercaProdotto = QtWidgets.QPushButton(Frame)
        self.pushButtonRicercaProdotto.setGeometry(QtCore.QRect(160, 360, 141, 31))
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
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Images\\left.png"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.pushButtonRicercaProdotto.setIcon(icon1)
        self.pushButtonRicercaProdotto.setObjectName("pushButton_4")
        self.label = QtWidgets.QLabel(Frame)
        self.label.setGeometry(QtCore.QRect(10, 60, 391, 61))
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setStyleSheet("QLabel{\n"
                                 "font-family: Helvetica, sans-serif;\n"
                                 "font-weight: 400;\n"
                                 "font-size: 16px\n"
                                 "}")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.listWidget = QtWidgets.QListWidget(Frame)
        self.listWidget.setGeometry(QtCore.QRect(20, 120, 361, 141))
        self.listWidget.setStyleSheet("QScrollBar:vertical {\n"
                                      "            border: 0px solid #999999;\n"
                                      "            background:transparent;\n"
                                      "            width:10px;    \n"
                                      "            margin: 0px 0px 0px 0px;\n"
                                      "        }\n"
                                      "        QScrollBar::handle:vertical {         \n"
                                      "       \n"
                                      "            min-height: 0px;\n"
                                      "              border: 0px solid red;\n"
                                      "            border-radius: 4px;\n"
                                      "            background-color: #14626c;\n"
                                      "        }\n"
                                      "        QScrollBar::add-line:vertical {       \n"
                                      "            height: 0px;\n"
                                      "            subcontrol-position: bottom;\n"
                                      "            subcontrol-origin: margin;\n"
                                      "        }\n"
                                      "        QScrollBar::sub-line:vertical {\n"
                                      "            height: 0 px;\n"
                                      "            subcontrol-position: top;\n"
                                      "            subcontrol-origin: margin;\n"
                                      "        }\n"
                                      "\n"
                                      "QListView{\n"
                                      "border-radius:8px;\n"
                                      "border:2px solid black;\n"
                                      "} \n"
                                      "\n"
                                      "\n"
                                      "QListView::item:selected\n"
                                      "{\n"
                                      "border : 0px;\n"
                                      "background : transparent;\n"
                                      "}\n"
                                      "\n"
                                      " QListView::item::hover\n"
                                      "{\n"
                                      "background : transparent;\n"
                                      "}")
        self.listWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.listWidget.setDefaultDropAction(QtCore.Qt.IgnoreAction)
        self.listWidget.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignVCenter)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(False)
        font.setUnderline(False)
        item.setFont(font)
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(False)
        font.setUnderline(False)
        item.setFont(font)
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(False)
        font.setUnderline(False)
        item.setFont(font)
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(False)
        font.setUnderline(False)
        item.setFont(font)
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(False)
        font.setUnderline(False)
        item.setFont(font)
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(False)
        font.setUnderline(False)
        item.setFont(font)
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(False)
        font.setUnderline(False)
        item.setFont(font)
        self.listWidget.addItem(item)
        self.pushButtonAggiungiOfferta = QtWidgets.QPushButton(Frame)
        self.pushButtonAggiungiOfferta.setGeometry(QtCore.QRect(20, 310, 361, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonAggiungiOfferta.setFont(font)
        self.pushButtonAggiungiOfferta.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButtonAggiungiOfferta.setStyleSheet("QPushButton{\n"
                                                     "border: 2px solid black;\n"
                                                     "border-radius: 10px;\n"
                                                     "}\n"
                                                     "QPushButton:hover{\n"
                                                     "\n"
                                                     "background-color: #14626c;\n"
                                                     "color:white;\n"
                                                     "}")
        self.pushButtonAggiungiOfferta.setCheckable(False)
        self.pushButtonAggiungiOfferta.setObjectName("pushButton_7")
        self.pushButtonLogout.clicked.connect(self.openLogin)
        self.pushButtonRicercaProdotto.clicked.connect(self.openRicercaProdotto)
        self.pushButtonAggiungiOfferta.clicked.connect(self.clickAggiungiOfferta)
        self.pushButtonModifica.clicked.connect(self.openModifica)

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Fumetteria - Prodotto Trovato"))
        self.label_4.setText(_translate("Frame", "PRODOTTO TROVATO"))
        self.pushButtonLogout.setText(_translate("Frame", " Logout"))
        self.pushButtonModifica.setText(_translate("Frame", "Modifica"))
        self.pushButtonRicercaProdotto.setText(_translate("Frame", " Indietro"))
        self.label.setText(_translate("Frame", "La ricerca è andata a buon fine. Cliccare il pulsante\n"
                                               "modifica per modificare il prodotto."))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("Frame", "Nome Prodotto : " + self.prodottoTrovato.getNomeProdotto()))
        item = self.listWidget.item(1)
        item.setText(_translate("Frame", "Quantità Prodotto : " + self.prodottoTrovato.getQuantitaMagazzino()))
        item = self.listWidget.item(2)
        item.setText(_translate("Frame", "Prezzo Prodotto : " + self.prodottoTrovato.getPrezzo() + " €"))
        item = self.listWidget.item(3)
        item.setText(_translate("Frame", "Codice Seriale : " + self.prodottoTrovato.getCodiceSeriale()))
        item = self.listWidget.item(4)
        item.setText(_translate("Frame", "Offerta : " + self.prodottoTrovato.getOfferta()))
        item = self.listWidget.item(5)
        item.setText(_translate("Frame", "Tipo Offerta : " + self.prodottoTrovato.getTipoOfferta()))
        item = self.listWidget.item(6)
        item.setText(_translate("Frame", "Prezzo Offerta : " + self.prodottoTrovato.getPrezzoOfferta() + " €"))
        item = self.listWidget.item(7)
        item.setText(_translate("Frame", "Data Scadenza Offerta : " + self.prodottoTrovato.getDataScadenzaOfferta()))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.pushButtonAggiungiOfferta.setText(_translate("Frame", "Aggiungi Offerta"))

    # Metodo che permette di ritornare all'interfaccia iniziale
    # del programma, ovvero LoginAmministratore.
    def openLogin(self):
        from Grafica.GestioneLogin.LoginAmministratore import LoginAmministratore
        self.login = QtWidgets.QFrame()
        self.ui = LoginAmministratore()
        self.ui.setupUi(self.login)
        self.login.show()
        self.frame.close()

    # Metodo che riporta l'utente all'interno della schermata RicercaProdotto
    # dopo aver cliccato indietro.
    def openRicercaProdotto(self):
        from Grafica.GestioneMagazzino.RicercaProdotto import RicercaProdotto
        self.ricercaProdotto = QtWidgets.QFrame()
        self.ui = RicercaProdotto()
        self.ui.setupUi(self.ricercaProdotto)
        self.ricercaProdotto.show()
        self.frame.close()

    # Metodo che viene eseguito quando si clicca il pulsante AggiungiOfferta.
    # Nel caso in cui il prodotto trovato ha già settata un'offerta (generale o
    # meno), viene visualizzata una schermata di errore.
    # Nel caso in cui il prodotto non avesse un'offerta già settata,
    # viene richiamato il metodo "self.openAggiungiOfferta".
    def clickAggiungiOfferta(self):

        if self.prodottoTrovato.getOfferta() == "None":
            self.openAggiungiOfferta()
        else:
            self.ErrorOfferta()

    # Metodo richiamato da "self.clickAggiungiOfferta" per aprire
    # l'interfaccia AggiungiOffertaDopoRicerca su cui si può andare
    # ad aggiungere un'offerta al prodotto trovato.
    def openAggiungiOfferta(self):
        from Grafica.GestioneMagazzino.AggiungiOffertaDopoRicerca import AggiungiOffertaDopoRicerca
        self.aggiungiOfferta = QtWidgets.QFrame()
        self.ui = AggiungiOffertaDopoRicerca()
        self.ui.setupUi(self.aggiungiOfferta, self.prodottoTrovato)
        self.aggiungiOfferta.show()
        self.frame.close()

    # Metodo utilizzato per aprire la interfaccia ModificaPrincipaleProdotto
    # in cui si possono effettuare le modifiche sul prodotto trovato grazie
    # all'utilizzo dell'interfaccia RicercaProdotto.
    def openModifica(self):
        from Grafica.GestioneMagazzino.ModificaProdotto.ModificaPrincipaleProdotto import ModificaPrincipaleProdotto
        self.modificaPrincipaleProdotto = QtWidgets.QFrame()
        self.ui = ModificaPrincipaleProdotto()
        self.ui.setupUi(self.modificaPrincipaleProdotto, self.prodottoTrovato)
        self.modificaPrincipaleProdotto.show()
        self.frame.close()

    def ErrorOfferta(self):
        self.ErrorBox = QMessageBox()
        self.ErrorBox.setWindowTitle("Errore")
        self.ErrorBox.setText("Il prodotto ha già un'offerta.\nPer modificare l'offerta cliccare su modifica")
        self.ErrorBox.setStyleSheet(
            "QLabel{min-width:300 px; font-size: 14px; font-family: Helvetica, Sans-Serif; } QPushButton:hover{"
            "background-color: #14626c;color:white; }QPushButton{ width:40px; height:20px; font-size: 10px; "
            "font-family: Helvetica, Sans-Serif; border: 1px solid black; border-radius: 5px; }")
        self.ErrorBox.exec()
