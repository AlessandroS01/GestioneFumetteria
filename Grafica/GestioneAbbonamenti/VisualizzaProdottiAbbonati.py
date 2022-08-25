from PyQt5 import QtCore, QtGui, QtWidgets

from GestioneAbbonamenti.GestioneAbbonamenti import GestioneAbbonamenti


class VisualizzaProdottiAbbonati(object):

    def setupUi(self, Frame):
        self.prodottiAbbonati = GestioneAbbonamenti()
        Frame.setObjectName("Frame")
        Frame.resize(872, 631)
        Frame.setStyleSheet("QFrame{\n"
                            "background-color: rgb(255, 255, 255);\n"
                            "}")
        Frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame = Frame
        self.label_4 = QtWidgets.QLabel(Frame)
        self.label_4.setGeometry(QtCore.QRect(10, 10, 841, 41))
        self.label_4.setStyleSheet("QLabel{\n"
                                   "font-family: impact, sans-serif;\n"
                                   "font-size:40px;\n"
                                   "\n"
                                   "}")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.line = QtWidgets.QFrame(Frame)
        self.line.setGeometry(QtCore.QRect(175, 50, 511, 20))
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
        self.pushButtonGestioneAbbonamentiPrincipale = QtWidgets.QPushButton(Frame)
        self.pushButtonGestioneAbbonamentiPrincipale.setGeometry(QtCore.QRect(160, 590, 141, 31))
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
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(
            "Images\\left.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonGestioneAbbonamentiPrincipale.setIcon(icon)
        self.pushButtonGestioneAbbonamentiPrincipale.setObjectName("pushButton_4")
        self.pushButtonLogout = QtWidgets.QPushButton(Frame)
        self.pushButtonLogout.setGeometry(QtCore.QRect(10, 590, 141, 31))
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
        icon1.addPixmap(QtGui.QPixmap(
            "Images\\log.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonLogout.setIcon(icon1)
        self.pushButtonLogout.setCheckable(False)
        self.pushButtonLogout.setObjectName("pushButton_8")
        self.tableWidget = QtWidgets.QTableWidget(Frame)
        self.tableWidget.setGeometry(QtCore.QRect(50, 150, 771, 401))
        self.tableWidget.setStyleSheet("QWidget {\n"
                                       "    \n"
                                       "}\n"
                                       "\n"
                                       "QHeaderView::section {\n"
                                       "    background-color: #14626c;\n"
                                       "color:white;\n"
                                       "font-weight:bold;\n"
                                       "\n"
                                       "}\n"
                                       "\n"
                                       "QTableWidget {\n"
                                       "    gridline-color: black;\n"
                                       "    font-size: 14px;\n"
                                       "font-family:Helvetica,sans-serif;\n"
                                       "}\n"
                                       "\n"
                                       "QTableWidget QTableCornerButton::section {\n"
                                       "}")
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        # Setta un numero di righe pari al numero dei prodotti in offerta
        # per gli abbonati.
        self.tableWidget.setRowCount(self.leggiNumeroProdottiAbbonati())
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)

        # Utilizzato per creare la tabella su cui inserire i vari
        # prodotti con la relativa offerta per abbonati salvati all'interno del
        # file di testo "Magazzino.txt".
        for riga in range(0, self.leggiNumeroProdottiAbbonati()):
            for colonna in range(0, 6):
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget.setItem(riga, colonna, item)

        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget.verticalHeader().setVisible(False)
        self.pushButtonLogout.clicked.connect(self.openLogin)
        self.pushButtonGestioneAbbonamentiPrincipale.clicked.connect(self.openGestioneAbbonamentiPrincipale)

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Fumetteria - Gestione Abbonamenti"))
        self.label_4.setText(_translate("Frame", "VISUALIZZA PRODOTTI ABBONATI"))
        self.label_5.setText(_translate("Frame",
                                        "Di seguito sono riportati tutti i prodotti con un\'offerta esclusiva per gli "
                                        "abbonati presenti in magazzino.\n "
                                        " Cliccare sul pulsante Indietro per tornare alla gestione degli abbonamenti."))
        self.pushButtonGestioneAbbonamentiPrincipale.setText(_translate("Frame", " Indietro"))
        self.pushButtonLogout.setText(_translate("Frame", " Logout"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Frame", "Prodotto"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Frame", "Quantità"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Frame", "Codice Seriale"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Frame", "Tipo Offerta"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Frame", "Prezzo Offerta"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Frame", "Data Scadenza Offerta"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)

        # Utilizzato per popolare la tabella con i vari
        # prodotti e i propri attributi che sono salvati all'interno del
        # file di testo "Magazzino.txt".
        for riga in range(0, self.leggiNumeroProdottiAbbonati()):
            prodottoTrovato = self.prodottiAbbonati.getProdottiOffertaAbbonati()[riga]
            item = self.tableWidget.item(riga, 0)
            item.setText(_translate("Frame", prodottoTrovato.getNomeProdotto()))
            item = self.tableWidget.item(riga, 1)
            item.setText(_translate("Frame", prodottoTrovato.getQuantitaMagazzino()))
            item = self.tableWidget.item(riga, 2)
            item.setText(_translate("Frame", prodottoTrovato.getCodiceSeriale()))
            item = self.tableWidget.item(riga, 3)
            item.setText(_translate("Frame", prodottoTrovato.getTipoOfferta()))
            item = self.tableWidget.item(riga, 4)
            item.setText(_translate("Frame", prodottoTrovato.getPrezzoOfferta()))
            item = self.tableWidget.item(riga, 5)
            item.setText(_translate("Frame", prodottoTrovato.getDataScadenzaOfferta()))

        self.tableWidget.setSortingEnabled(__sortingEnabled)

    # Metodo che permette di ritornare all'interfaccia GestioneAbbonamentiPrincipale.
    def openGestioneAbbonamentiPrincipale(self):
        from Grafica.GestioneAbbonamenti.GestioneAbbonamentiPrincipale import GestioneAbbonamentiPrincipale
        self.gestioneAbbonamentiPrincipale = QtWidgets.QFrame()
        self.ui = GestioneAbbonamentiPrincipale()
        self.ui.setupUi(self.gestioneAbbonamentiPrincipale)
        self.gestioneAbbonamentiPrincipale.show()
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

    # Metodo che viene utilizzato per calcolare il numero dei prodotti
    # che hanno un'offerta per gli abbonati.
    def leggiNumeroProdottiAbbonati(self):

        from GestioneAbbonamenti.GestioneAbbonamenti import GestioneAbbonamenti
        gestioneAbbonamenti = GestioneAbbonamenti()

        return len(gestioneAbbonamenti.getProdottiOffertaAbbonati())
