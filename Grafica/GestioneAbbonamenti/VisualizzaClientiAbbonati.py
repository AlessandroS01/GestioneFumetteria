from PyQt5 import QtCore, QtGui, QtWidgets

from GestioneAbbonamenti.GestioneAbbonamenti import GestioneAbbonamenti


class VisualizzaClientiAbbonati(object):

    def setupUi(self, Frame):
        self.clientiabbonati = GestioneAbbonamenti()
        Frame.setObjectName("Frame")
        Frame.resize(872, 651)
        Frame.setStyleSheet("QFrame{\n"
                        "background-color: rgb(255, 255, 255);\n"
                        "}")
        Frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame=Frame
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
        self.pushButtonGestioneAbbonamentiPrincipale = QtWidgets.QPushButton(Frame)
        self.pushButtonGestioneAbbonamentiPrincipale.setGeometry(QtCore.QRect(160, 610, 141, 31))
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
        icon.addPixmap(QtGui.QPixmap("Images\\left.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonGestioneAbbonamentiPrincipale.setIcon(icon)
        self.pushButtonGestioneAbbonamentiPrincipale.setObjectName("pushButton_4")
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
        icon1.addPixmap(QtGui.QPixmap("Images\\log.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonLogout.setIcon(icon1)
        self.pushButtonLogout.setCheckable(False)
        self.pushButtonLogout.setObjectName("pushButton_8")
        self.tableWidget = QtWidgets.QTableWidget(Frame)
        self.tableWidget.setGeometry(QtCore.QRect(50, 150, 771, 401))
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
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setRowCount(self.leggiNumeroClientiAbbonati())
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
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget.verticalHeader().setVisible(False)
        self.pushButton_5 = QtWidgets.QPushButton(Frame)
        self.pushButton_5.setGeometry(QtCore.QRect(670, 560, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_5.setStyleSheet("QPushButton{\n"
                                        "border: 2px solid black;\n"
                                        "border-radius: 10px;\n"
                                        "}\n"
                                        "QPushButton:hover{\n"
                                        "\n"
                                        "background-color: #14626c;\n"
                                        "color:white;\n"
                                        "}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Images\\magnifying-glass.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_5.setIcon(icon2)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButtonLogout.clicked.connect(self.openLogin)
        self.pushButtonGestioneAbbonamentiPrincipale.clicked.connect(self.openGestioneAbbonamentiPrincipale)

        for riga in range(0, self.leggiNumeroClientiAbbonati()):
            for colonna in range(0, 8):
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget.setItem(riga, colonna, item)


        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Fumetteria - Gestione Magazzino"))
        self.label_4.setText(_translate("Frame", "VISUALIZZA CLIENTI ABBONATI"))
        self.label_5.setText(_translate("Frame", "Di seguito sono riportate le informazioni relative ai clienti abbonati. Per tornare indietro o effettuare il\n"
                                        " logout utilizzare i pulsanti in basso a sinistra. Utilizza il pulsante ricerca per effettuare la ricerca di un\n"
                                        "abbonamento e modificare le informazioni relative al cliente."))
        self.pushButtonGestioneAbbonamentiPrincipale.setText(_translate("Frame", " Indietro"))
        self.pushButtonLogout.setText(_translate("Frame", " Logout"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Frame", "Nome:"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Frame", "Cognome:"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Frame", "Codice Fiscale:"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Frame", "Telefono:"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Frame", "Email:"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Frame", "Data Emissione Abbonamento:"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Frame", "Data Scadenza Abbonamento:"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("Frame", "Codice Abbonamento"))
        self.pushButton_5.setText(_translate("Frame", " Ricerca"))

        for riga in range(0, self.leggiNumeroClientiAbbonati()):

            clienteAbbonato = self.clientiabbonati.getAbbonamenti()[riga]
            print(clienteAbbonato.getCliente().getNome())
            print(clienteAbbonato.getDataScadenza())
            item = self.tableWidget.item(riga, 0)
            item.setText(_translate("Frame", clienteAbbonato.getCliente().getNome()))
            item = self.tableWidget.item(riga, 1)
            item.setText(_translate("Frame", clienteAbbonato.getCliente().getCognome()))
            item = self.tableWidget.item(riga, 2)
            item.setText(_translate("Frame", clienteAbbonato.getCliente().getCodiceFiscale()))
            item = self.tableWidget.item(riga, 3)
            item.setText(_translate("Frame", clienteAbbonato.getCliente().getTelefono()))
            item = self.tableWidget.item(riga, 4)
            item.setText(_translate("Frame", clienteAbbonato.getCliente().getEmail()))
            item = self.tableWidget.item(riga, 5)
            item.setText(_translate("Frame", clienteAbbonato.getDataEmissione()))
            item = self.tableWidget.item(riga, 6)
            item.setText(_translate("Frame", clienteAbbonato.getDataScadenza()))
            item = self.tableWidget.item(riga, 7)
            item.setText(_translate("Frame", clienteAbbonato.getCodiceIdentificativo()))


    def openLogin(self):
        from Grafica.GestioneLogin.LoginAmministratore import LoginAmministratore
        self.login = QtWidgets.QFrame()
        self.ui = LoginAmministratore()
        self.ui.setupUi(self.login)
        self.login.show()
        self.frame.close()

    def openGestioneAbbonamentiPrincipale(self):
        from Grafica.GestioneAbbonamenti.GestioneAbbonamentiPrincipale import GestioneAbbonamentiPrincipale
        self.gestioneAbbonamentiPrincipale = QtWidgets.QFrame()
        self.ui = GestioneAbbonamentiPrincipale()
        self.ui.setupUi(self.gestioneAbbonamentiPrincipale)
        self.gestioneAbbonamentiPrincipale.show()
        self.frame.close()

    def leggiNumeroClientiAbbonati(self):

        return len(self.clientiabbonati.listaAbbonamenti)
