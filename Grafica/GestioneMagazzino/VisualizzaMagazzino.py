import os

from PyQt5 import QtCore, QtGui, QtWidgets

from GestioneMagazzino.Magazzino import Magazzino


class VisualizzaMagazzino(object):

    def setupUi(self, Frame):
        self.magazzino = Magazzino()
        Frame.setObjectName("Frame")
        Frame.resize(872, 647)
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
        self.line.setGeometry(QtCore.QRect(225, 50, 401, 20))
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
        self.pushButtonGestioneMagazzinoPrincipale = QtWidgets.QPushButton(Frame)
        self.pushButtonGestioneMagazzinoPrincipale.setGeometry(QtCore.QRect(160, 610, 141, 31))
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
        icon.addPixmap(QtGui.QPixmap(
            "Images\\left.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonGestioneMagazzinoPrincipale.setIcon(icon)
        self.pushButtonGestioneMagazzinoPrincipale.setObjectName("pushButton_4")
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
                                       "border: 2px solid black;\n"
                                       "border-radius:6px;"
                                       "}")
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setRowCount(self.leggiNumeroRighe())
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
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
        # prodotti e con i corrispettivi attributi che sono salvati all'interno del
        # file di testo "Magazzino.txt".
        for riga in range(0, self.leggiNumeroRighe()):
            for colonna in range(0, 8):
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget.setItem(riga, colonna, item)


        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget.verticalHeader().setVisible(False)
        self.pushButtonRicerca = QtWidgets.QPushButton(Frame)
        self.pushButtonRicerca.setGeometry(QtCore.QRect(670, 560, 151, 31))
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
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(
            "Images\\magnifying-glass.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonRicerca.setIcon(icon2)
        self.pushButtonRicerca.setObjectName("pushButton_5")
        self.pushButtonLogout.clicked.connect(self.openLogin)
        self.pushButtonGestioneMagazzinoPrincipale.clicked.connect(self.openGestioneMagazzinoPrincipale)
        self.pushButtonRicerca.clicked.connect(self.openRicerca)

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Fumetteria - Gestione Magazzino"))
        self.label_4.setText(_translate("Frame", "VISUALIZZA MAGAZZINO"))
        self.label_5.setText(_translate("Frame",
                                        "Di seguito sono riportate tutte le informazioni relative ai prodotti "
                                        "presenti in magazzino. Se si vuole\n "
                                        "effettuare una ricerca cliccare sul pulsante Ricerca. Cliccare sul pulsante "
                                        "Indietro per tornare \n "
                                        " alla gestione del magazzino"))
        self.pushButtonGestioneMagazzinoPrincipale.setText(_translate("Frame", " Indietro"))
        self.pushButtonLogout.setText(_translate("Frame", " Logout"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("Frame", "prodo"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Frame", "Prodotto"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Frame", "Quantità"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Frame", "Prezzo"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Frame", "Codice Seriale"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Frame", "Offerta"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Frame", "Tipo Offerta"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Frame", "Prezzo Offerta"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("Frame", "Data Scadenza Offerta"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)

        # Utilizzato per popolare la tabella con i vari
        # prodotti e i propri attributi che sono salvati all'interno del
        # file di testo "Magazzino.txt".
        for riga in range(0, self.leggiNumeroRighe()):
            prodottoTrovato = self.magazzino.getMagazzino()[riga]
            item = self.tableWidget.item(riga, 0)
            item.setText(_translate("Frame", prodottoTrovato.getNomeProdotto()))
            item = self.tableWidget.item(riga, 1)
            item.setText(_translate("Frame", prodottoTrovato.getQuantitaMagazzino()))
            item = self.tableWidget.item(riga, 2)
            item.setText(_translate("Frame", prodottoTrovato.getPrezzo()))
            item = self.tableWidget.item(riga, 3)
            item.setText(_translate("Frame", prodottoTrovato.getCodiceSeriale()))
            item = self.tableWidget.item(riga, 4)
            item.setText(_translate("Frame", prodottoTrovato.getOfferta()))
            item = self.tableWidget.item(riga, 5)
            item.setText(_translate("Frame", prodottoTrovato.getTipoOfferta()))
            item = self.tableWidget.item(riga, 6)
            item.setText(_translate("Frame", prodottoTrovato.getPrezzoOfferta()))
            item = self.tableWidget.item(riga, 7)
            item.setText(_translate("Frame", prodottoTrovato.getDataScadenzaOfferta()))


        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.pushButtonRicerca.setText(_translate("Frame", " Ricerca"))

    # Metodo che permette di ritornare all'interfaccia GestioneMagazzinoPrincipale.
    def openGestioneMagazzinoPrincipale(self):
        from Grafica.GestioneMagazzino.GestioneMagazzinoPrincipale import GestioneMagazzinoPrincipale
        self.gestioneMagazzino = QtWidgets.QFrame()
        self.ui = GestioneMagazzinoPrincipale()
        self.ui.setupUi(self.gestioneMagazzino)
        self.gestioneMagazzino.show()
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

    # Metodo che serve ad aprire l'interfaccia relativa alla
    # ricerca del prodotto andata a buon fine, ovvero RicercaProdotto
    # in cui si può ricercare un prodotto.
    def openRicerca(self):
        from Grafica.GestioneMagazzino.RicercaProdotto import RicercaProdotto
        self.ricercaProdotto = QtWidgets.QFrame()
        self.ui = RicercaProdotto()
        self.ui.setupUi(self.ricercaProdotto)
        self.ricercaProdotto.show()
        self.frame.close()

    # Metodo usato per leggere il numero delle righe all'interno
    # del file "Magazzino.txt" per creare un numero di righe pari
    # al numero dei prodotti salvati.
    def leggiNumeroRighe(self):

        stringa = os.getcwd().split("\\")
        path = ""
        for index in range(0, len(stringa)):
            if index == 0:
                path = stringa[index]
            else:
                path += "\\" + stringa[index]

        pathMagazzino = path + "\\Magazzino"

        with open(pathMagazzino, 'r') as file:
            lista = file.readlines()
            file.close()

        return len(lista)

