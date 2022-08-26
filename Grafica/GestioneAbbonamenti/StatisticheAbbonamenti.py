from PyQt5 import QtCore, QtGui, QtWidgets

from GestioneAbbonamenti.GestioneAbbonamenti import GestioneAbbonamenti


class StatisticheAbbonamenti(object):

    def setupUi(self, Frame, numeroRigheTabella, dataEmissione):
        self.dataEmissione = dataEmissione
        self.numeroRighe = numeroRigheTabella
        self.gestoreAbbonamenti = GestioneAbbonamenti()
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
        self.label_5.setGeometry(QtCore.QRect(10, 70, 851, 81))
        self.label_5.setStyleSheet("QLabel{\n"
                                   "font-family: Helvetica, sans-serif;\n"
                                   "font-weight: 400;\n"
                                   "font-size: 18px\n"
                                   "}")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.pushButton_4 = QtWidgets.QPushButton(Frame)
        self.pushButton_4.setGeometry(QtCore.QRect(160, 610, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_4.setStyleSheet("QPushButton{\n"
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
        self.pushButton_4.setIcon(icon)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_8 = QtWidgets.QPushButton(Frame)
        self.pushButton_8.setGeometry(QtCore.QRect(10, 610, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_8.setStyleSheet("QPushButton{\n"
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
        self.pushButton_8.setIcon(icon1)
        self.pushButton_8.setCheckable(False)
        self.pushButton_8.setObjectName("pushButton_8")
        self.tableWidget = QtWidgets.QTableWidget(Frame)
        self.tableWidget.setGeometry(QtCore.QRect(50, 160, 771, 401))
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
        self.tableWidget.setRowCount(self.numeroRighe)
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

        # Utilizzato per creare la tabella su cui inserire i vari
        # clienti abbonati salvati all'interno del
        # file di testo "Abbonamenti.txt".
        for riga in range(0, self.numeroRighe):
            for colonna in range(0, 8):
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget.setItem(riga, colonna, item)

        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget.verticalHeader().setVisible(False)
        self.pushButton_5 = QtWidgets.QPushButton(Frame)
        self.pushButton_5.setGeometry(QtCore.QRect(670, 570, 151, 31))
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
        icon2.addPixmap(QtGui.QPixmap("Images\\magnifying-glass.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_5.setIcon(icon2)
        self.pushButton_5.setObjectName("pushButton_5")

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Fumetteria - Gestione Magazzino"))
        self.label_4.setText(_translate("Frame", "ABBONAMENTI EMESSI"))
        self.label_5.setText(_translate("Frame",
                                        "Di seguito sono riportate le informazioni relative ai clienti che dispongono "
                                        "di un abbonamento che hanno\n "
                                        "come data di emissione la data inserita. Per tornare indietro o effettuare "
                                        "il logout utilizzare i pulsanti\n "
                                        "in basso a sinistra. Utilizza il pulsante ricerca per effettuare la ricerca "
                                        "di un abbonamento\n "
                                        " e modificare le informazioni relative al cliente."))
        self.pushButton_4.setText(_translate("Frame", " Indietro"))
        self.pushButton_8.setText(_translate("Frame", " Logout"))
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

        # Utilizzato per popolare la tabella con i vari
        # clienti che sono salvati all'interno del
        # file di testo "Abbonamenti.txt".
        for riga in range(0, self.numeroRighe):
            abbonamentiEmessi = self.gestoreAbbonamenti.getAbbonamentiEmessi(self.dataEmissione)[riga]
            item = self.tableWidget.item(riga, 0)
            item.setText(_translate("Frame", abbonamentiEmessi.getCliente().getNome()))
            item = self.tableWidget.item(riga, 1)
            item.setText(_translate("Frame", abbonamentiEmessi.getCliente().getCognome()))
            item = self.tableWidget.item(riga, 2)
            item.setText(_translate("Frame", abbonamentiEmessi.getCliente().getCodiceFiscale()))
            item = self.tableWidget.item(riga, 3)
            item.setText(_translate("Frame", abbonamentiEmessi.getCliente().getTelefono()))
            item = self.tableWidget.item(riga, 4)
            item.setText(_translate("Frame", abbonamentiEmessi.getCliente().getEmail()))
            item = self.tableWidget.item(riga, 5)
            item.setText(_translate("Frame", abbonamentiEmessi.getDataEmissione()))
            item = self.tableWidget.item(riga, 6)
            item.setText(_translate("Frame", abbonamentiEmessi.getDataScadenza()))
            item = self.tableWidget.item(riga, 7)
            item.setText(_translate("Frame", abbonamentiEmessi.getCodiceIdentificativo()))
        self.pushButton_5.setText(_translate("Frame", " Ricerca"))

