from PyQt5 import QtCore, QtGui, QtWidgets


class RicercaAbbonamentoSuccesso(object):

    def setupUi(self, Frame, abbonamento):
        self.abbonamentoTrovato = abbonamento
        Frame.setObjectName("Frame")
        Frame.resize(403, 380)
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
        self.pushButtonLogout.setGeometry(QtCore.QRect(10, 340, 141, 31))
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
        self.pushButtonLogout.setObjectName("pushButton_5")
        self.pushButtonModificaCliente = QtWidgets.QPushButton(Frame)
        self.pushButtonModificaCliente.setGeometry(QtCore.QRect(20, 280, 361, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonModificaCliente.setFont(font)
        self.pushButtonModificaCliente.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButtonModificaCliente.setStyleSheet("QPushButton{\n"
                                                     "border: 2px solid black;\n"
                                                     "border-radius: 10px;\n"
                                                     "}\n"
                                                     "QPushButton:hover{\n"
                                                     "\n"
                                                     "background-color: #14626c;\n"
                                                     "color:white;\n"
                                                     "}")
        self.pushButtonModificaCliente.setCheckable(False)
        self.pushButtonModificaCliente.setObjectName("pushButton_6")
        self.pushButtonRicerca = QtWidgets.QPushButton(Frame)
        self.pushButtonRicerca.setGeometry(QtCore.QRect(160, 340, 141, 31))
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
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Images\\left.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonRicerca.setIcon(icon1)
        self.pushButtonRicerca.setObjectName("pushButton_4")
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
        self.listWidget.setGeometry(QtCore.QRect(20, 130, 361, 141))
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
        item.setFlags(
            QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsTristate)
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
        self.pushButtonRicerca.clicked.connect(self.openRicercaAbbonamento)
        self.pushButtonLogout.clicked.connect(self.openLogin)
        self.pushButtonModificaCliente.clicked.connect(self.openModificaClientePrincipale)

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Fumetteria - Abbonamento Trovato"))
        self.label_4.setText(_translate("Frame", "ABBONAMENTO TROVATO"))
        self.pushButtonLogout.setText(_translate("Frame", " Logout"))
        self.pushButtonModificaCliente.setText(_translate("Frame", "Modifica"))
        self.pushButtonRicerca.setText(_translate("Frame", " Indietro"))
        self.label.setText(_translate("Frame", "La ricerca è andata a buon fine. Cliccare il pulsante\n"
                                               "modifica per modificare le informazioni del cliente."))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("Frame", "Nome: " + self.abbonamentoTrovato.getCliente().getNome()))
        item = self.listWidget.item(1)
        item.setText(_translate("Frame", "Cognome " + self.abbonamentoTrovato.getCliente().getCognome()))
        item = self.listWidget.item(2)
        item.setText(_translate("Frame", "Codice Fiscale: " + self.abbonamentoTrovato.getCliente().getCodiceFiscale()))
        item = self.listWidget.item(3)
        item.setText(_translate("Frame", "Telefono: " + self.abbonamentoTrovato.getCliente().getTelefono()))
        item = self.listWidget.item(4)
        item.setText(_translate("Frame", "Email: " + self.abbonamentoTrovato.getCliente().getEmail()))
        item = self.listWidget.item(5)
        item.setText(_translate("Frame", "Data Emissione Abbonamento: " + self.abbonamentoTrovato.getDataEmissione()))
        item = self.listWidget.item(6)
        item.setText(_translate("Frame", "Data Scadenza Abbonamento: " + self.abbonamentoTrovato.getDataScadenza()))
        item = self.listWidget.item(7)
        item.setText(_translate("Frame", "Codice Abbonamento: " + self.abbonamentoTrovato.getCodiceIdentificativo()))
        self.listWidget.setSortingEnabled(__sortingEnabled)

    # Metodo che permette di ritornare all'interfaccia RicercaAbbonamento.
    def openRicercaAbbonamento(self):
        from Grafica.GestioneAbbonamenti.RicercaAbbonamento import RicercaAbbonamento
        self.ricercaAbbonamento = QtWidgets.QFrame()
        self.ui = RicercaAbbonamento()
        self.ui.setupUi(self.ricercaAbbonamento)
        self.ricercaAbbonamento.show()
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

    # Metodo che permette di aprire l'interfaccia sulla quale si
    # possono cambiare gli attributi dei clienti.
    # L'interfaccia è : ModificaClientePrincipale
    def openModificaClientePrincipale(self):
        from Grafica.GestioneAbbonamenti.ModificaCliente.ModificaClientePrincipale import ModificaClientePrincipale
        self.modificaClientePrincipale = QtWidgets.QFrame()
        self.ui = ModificaClientePrincipale()
        self.ui.setupUi(self.modificaClientePrincipale, self.abbonamentoTrovato)
        self.modificaClientePrincipale.show()
        self.frame.close()
