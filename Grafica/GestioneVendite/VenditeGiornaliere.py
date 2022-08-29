from PyQt5 import QtCore, QtGui, QtWidgets


class VenditeGiornaliere(object):

    def setupUi(self, Frame, gestoreVendite, dataImmessa):

        self.gestoreVendite = gestoreVendite
        self.listaVendite = self.gestoreVendite.getVenditeGiornata(dataImmessa)[0]
        self.dataImmessa = dataImmessa
        Frame.setObjectName("Frame")
        Frame.resize(872, 651)
        Frame.setStyleSheet("QFrame{\n"
                            "background-color: rgb(255, 255, 255);\n"
                            "}")
        Frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame = Frame
        self.label_4 = QtWidgets.QLabel(Frame)
        self.label_4.setGeometry(QtCore.QRect(10, 10, 851, 41))
        self.label_4.setStyleSheet("QLabel{\n"
                                   "font-family: impact, sans-serif;\n"
                                   "font-size:40px;\n"
                                   "\n"
                                   "}")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.line = QtWidgets.QFrame(Frame)
        self.line.setGeometry(QtCore.QRect(175, 50, 521, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_5 = QtWidgets.QLabel(Frame)
        self.label_5.setGeometry(QtCore.QRect(10, 70, 851, 71))
        self.label_5.setStyleSheet("QLabel{\n"
                                   "font-family: Helvetica, sans-serif;\n"
                                   "font-weight: 400;\n"
                                   "font-size: 18px\n"
                                   "}")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.pushButtonInserisciDataVendite = QtWidgets.QPushButton(Frame)
        self.pushButtonInserisciDataVendite.setGeometry(QtCore.QRect(160, 610, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonInserisciDataVendite.setFont(font)
        self.pushButtonInserisciDataVendite.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButtonInserisciDataVendite.setStyleSheet("QPushButton{\n"
                                        "border: 2px solid black;\n"
                                        "border-radius: 10px;\n"
                                        "}\n"
                                        "QPushButton:hover{\n"
                                        "\n"
                                        "background-color: #14626c;\n"
                                        "color:white;\n"
                                        "}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Images\\left.png"), QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        self.pushButtonInserisciDataVendite.setIcon(icon)
        self.pushButtonInserisciDataVendite.setObjectName("pushButton_4")
        self.pushButtonLogout = QtWidgets.QPushButton(Frame)
        self.pushButtonLogout.setGeometry(QtCore.QRect(10, 610, 141, 31))
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
        icon1.addPixmap(QtGui.QPixmap("Images\\log.png"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.pushButtonLogout.setIcon(icon1)
        self.pushButtonLogout.setCheckable(False)
        self.pushButtonLogout.setObjectName("pushButton_8")
        self.tableWidget = QtWidgets.QTableWidget(Frame)
        self.tableWidget.setGeometry(QtCore.QRect(130, 150, 604, 401))
        self.tableWidget.setStyleSheet("\n"
                                       "QHeaderView::section {\n"
                                       "background-color: #14626c;\n"
                                       "color:white;\n"
                                       "font-weight:bold;\n"
                                       "\n"
                                       "}\n"
                                       "\n"
                                       "QTableWidget {\n"
                                       "gridline-color: black;\n"
                                       "font-size: 14px;\n"
                                       "font-family:Helvetica,sans-serif;\n"
                                       "border: 2px solid black;\n"
                                       "border-radius:6px;\n"
                                       "}\n"
                                       "")
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(self.righeTabella())
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)

        # Utilizzato per creare la tabella su cui inserire i vari
        # prodotti e con i corrispettivi attributi che sono salvati all'interno del
        # file di testo "ScontriniProdotti.txt".
        for riga in range(0, self.righeTabella()):
            for colonna in range(0, 3):
                item = QtWidgets.QTableWidgetItem()
                item.setFlags(QtCore.Qt.ItemIsEnabled)
                self.tableWidget.setItem(riga, colonna, item)

        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget.verticalHeader().setVisible(False)
        self.pushButtonIncasso = QtWidgets.QPushButton(Frame)
        self.pushButtonIncasso.setGeometry(QtCore.QRect(590, 560, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonIncasso.setFont(font)
        self.pushButtonIncasso.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButtonIncasso.setStyleSheet("QPushButton{\n"
                                             "border: 2px solid black;\n"
                                             "border-radius: 10px;\n"
                                             "}\n"
                                             "QPushButton:hover{\n"
                                             "\n"
                                             "background-color: #14626c;\n"
                                             "color:white;\n"
                                             "}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Images\\coin.png"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.pushButtonIncasso.setIcon(icon1)
        self.pushButtonIncasso.setObjectName("pushButton_5")
        self.pushButtonLogout.clicked.connect(self.openLogin)
        self.pushButtonInserisciDataVendite.clicked.connect(self.openInserisciDataVendite)
        self.pushButtonIncasso.clicked.connect(self.openIncassoGiornaliero)

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Fumetteria - Gestione Magazzino"))
        self.label_4.setText(_translate("Frame", "VISUALIZZA VENDITE"))
        self.label_5.setText(_translate("Frame",
                                        "Di seguito sono riportate le informazioni relative alle vendite avvenute "
                                        "durante la giornata immessa.\n "
                                        "Per tornare indietro o effettuare il logout utilizzare i pulsanti in basso a "
                                        "sinistra. "))

        self.pushButtonInserisciDataVendite.setText(_translate("Frame", " Indietro"))
        self.pushButtonLogout.setText(_translate("Frame", " Logout"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Frame", "Nome"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Frame", "Quantita Acquistate"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Frame", "Prezzo Vendita"))

        self.righeSettate = 0

        # Utilizzato per popolare la tabella con i vari
        # prodotti che sono salvati all'interno del
        # file di testo "Magazzino.txt".
        for riga in range(len(self.listaVendite)):

            vendite = self.listaVendite[riga]

            if "-" in vendite:

                vendita = vendite.split("-")

                for index in range(len(vendita)):
                    dettagliVendita = vendita[index].split("|")
                    nomeProdotto = dettagliVendita[0]
                    quantitaAcquistate = dettagliVendita[2]
                    prezzo = dettagliVendita[3]

                    item = self.tableWidget.item(self.righeSettate, 0)
                    item.setText(_translate("Frame", nomeProdotto))
                    item = self.tableWidget.item(self.righeSettate, 1)
                    item.setText(_translate("Frame", quantitaAcquistate))
                    item = self.tableWidget.item(self.righeSettate, 2)
                    item.setText(_translate("Frame", prezzo))

                    self.righeSettate += 1
            else:

                dettagliVendita = vendite.split("|")
                nomeProdotto = dettagliVendita[0]
                quantitaAcquistate = dettagliVendita[2]
                prezzo = dettagliVendita[3]

                item = self.tableWidget.item(self.righeSettate, 0)
                item.setText(_translate("Frame", nomeProdotto))
                item = self.tableWidget.item(self.righeSettate, 1)
                item.setText(_translate("Frame", quantitaAcquistate))
                item = self.tableWidget.item(self.righeSettate, 2)
                item.setText(_translate("Frame", prezzo))

                self.righeSettate += 1

        self.pushButtonIncasso.setText(_translate("Frame", "Incasso"))

    # Metodo utilizzato per contare il numero delle righe
    # che devono essere settate alla tabella.
    def righeTabella(self):

        contariga = 0

        for riga in range(0, len(self.listaVendite)):
            vendite = self.listaVendite[riga]
            if "-" in vendite:
                vendita = vendite.split("-")
                for index in range(len(vendita)):
                    contariga += 1

            else:
                contariga += 1

        return contariga

    # Metodo che permette di ritornare all'interfaccia iniziale
    # del programma, ovvero LoginAmministratore.
    def openLogin(self):
        from Grafica.GestioneLogin.LoginAmministratore import LoginAmministratore
        self.login = QtWidgets.QFrame()
        self.ui = LoginAmministratore()
        self.ui.setupUi(self.login)
        self.login.show()
        self.frame.close()

    # Metodo che permette di aprire all'interfaccia InserisciDataVendite.
    def openInserisciDataVendite(self):
        from Grafica.GestioneVendite.InserisciDataVendite import InserisciDataVendite
        self.inserisciDataVendite = QtWidgets.QFrame()
        self.ui = InserisciDataVendite()
        self.ui.setupUi(self.inserisciDataVendite)
        self.inserisciDataVendite.show()
        self.frame.close()

    # Metodo che fa visualizzare a schermo l'interfaccia IncassoGiornaliero.
    def openIncassoGiornaliero(self):
        from Grafica.GestioneVendite.IncassoGiornaliero import IncassoGiornaliero
        self.incassoGiornaliero = QtWidgets.QFrame()
        self.ui = IncassoGiornaliero()
        self.ui.setupUi(self.incassoGiornaliero, self.dataImmessa, self.gestoreVendite)
        self.incassoGiornaliero.show()
        self.frame.close()

