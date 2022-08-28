from operator import contains

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMessageBox

from GestioneMagazzino.Magazzino import Magazzino
from GestioneVendite.Acquisto import Acquisto
from GestioneVendite.GestoreVendite import GestoreVendite


class AggiungiAcquisto(object):

    def setupUi(self, Frame, controllo):
        self.controllo = controllo
        self.gestoreVendite = GestoreVendite()
        self.magazzino = Magazzino()
        Frame.setObjectName("Frame")
        Frame.resize(872, 732)
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
        self.line.setGeometry(QtCore.QRect(225, 50, 401, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_5 = QtWidgets.QLabel(Frame)
        self.label_5.setGeometry(QtCore.QRect(10, 70, 851, 91))
        self.label_5.setStyleSheet("QLabel{\n"
                                   "font-family: Helvetica, sans-serif;\n"
                                   "font-weight: 400;\n"
                                   "font-size: 17px\n"
                                   "}")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.pushButtonInserisciCodiceAbbonamento = QtWidgets.QPushButton(Frame)
        self.pushButtonInserisciCodiceAbbonamento.setGeometry(QtCore.QRect(160, 690, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonInserisciCodiceAbbonamento.setFont(font)
        self.pushButtonInserisciCodiceAbbonamento.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButtonInserisciCodiceAbbonamento.setStyleSheet("QPushButton{\n"
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
        self.pushButtonInserisciCodiceAbbonamento.setIcon(icon)
        self.pushButtonInserisciCodiceAbbonamento.setObjectName("pushButton_4")
        self.pushButtonLogout = QtWidgets.QPushButton(Frame)
        self.pushButtonLogout.setGeometry(QtCore.QRect(10, 690, 141, 31))
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
        self.tableWidget.setGeometry(QtCore.QRect(140, 210, 604, 401))
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
                                       "}\n"
                                       "QTableView::item:selected {"
                                       "background-color: lightblue;"
                                       "}\n"
                                       "}")
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(self.leggiNumeroRighe())
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)

        # Utilizzato per creare la tabella su cui inserire i vari
        # prodotti e con i corrispettivi attributi che sono salvati all'interno del
        # file di testo "Magazzino.txt".
        for riga in range(0, self.leggiNumeroRighe()):
            for colonna in range(0, 3):
                if colonna == 0:
                    itemBox = QtWidgets.QTableWidgetItem()
                    itemBox.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
                    itemBox.setCheckState(QtCore.Qt.Unchecked)
                    self.tableWidget.setItem(riga, colonna, itemBox)
                else:
                    item = QtWidgets.QTableWidgetItem()
                    if colonna == 1:
                        item.setFlags(QtCore.Qt.ItemIsEnabled)
                    self.tableWidget.setItem(riga, colonna, item)

        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget.verticalHeader().setVisible(False)
        self.pushButtonAggiungiAcquisto = QtWidgets.QPushButton(Frame)
        self.pushButtonAggiungiAcquisto.setGeometry(QtCore.QRect(515, 620, 230, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonAggiungiAcquisto.setFont(font)
        self.pushButtonAggiungiAcquisto.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButtonAggiungiAcquisto.setStyleSheet("QPushButton{\n"
                                                      "border: 2px solid black;\n"
                                                      "border-radius: 10px;\n"
                                                      "}\n"
                                                      "QPushButton:hover{\n"
                                                      "\n"
                                                      "background-color: #14626c;\n"
                                                      "color:white;\n"
                                                      "}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Images\\check.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonAggiungiAcquisto.setIcon(icon2)
        self.pushButtonAggiungiAcquisto.setObjectName("pushButton_5")
        self.lineEditRicerca = QtWidgets.QLineEdit(Frame)
        self.lineEditRicerca.setGeometry(QtCore.QRect(140, 170, 265, 31))
        self.lineEditRicerca.setStyleSheet("QLineEdit{\n"
                                           "border: 2px solid black;\n"
                                           "border-radius: 6px;\n"
                                           "}")
        self.lineEditRicerca.setObjectName("lineEdit")
        self.lineEditRicerca.setPlaceholderText("Inserisci il nome del prodotto da ricercare...")
        self.lineEditRicerca.textChanged.connect(self.search)
        self.pushButtonAggiungiAcquisto.clicked.connect(self.clickAggiungiAcquisto)
        self.pushButtonLogout.clicked.connect(self.openLogin)
        self.pushButtonInserisciCodiceAbbonamento.clicked.connect(self.openInserisciCodiceAbbonamento)

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Fumetteria - Aggiungi Acquisto"))
        self.label_4.setText(_translate("Frame", "AGGIUNGI ACQUISTO"))
        self.label_5.setText(_translate("Frame",
                                        "Di seguito sono riportate le informazioni relative ai prodotti e le relative "
                                        "quantità in magazzino. E\' possibile\n "
                                        "effettuare una ricerca dinamica all\'interno della tabella scrivendo il nome "
                                        "del prodotto nel campo apposito.\n "
                                        "Selezionare i prodotti che sono stati acquistati utilizzando le checkbox e "
                                        "cliccare su Aggiungi Acquisto\n "
                                        "una volta terminata la selezione. Immettere nel campo Quantità il numero di "
                                        "pezzi acquistati."))
        self.pushButtonInserisciCodiceAbbonamento.setText(_translate("Frame", " Indietro"))
        self.pushButtonLogout.setText(_translate("Frame", " Logout"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Frame", "Prodotto"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Frame", "Quantità Magazzino"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Frame", "Quantità"))

        # Utilizzato per popolare la tabella con i vari
        # prodotti che sono salvati all'interno del
        # file di testo "Magazzino.txt".
        for riga in range(0, self.leggiNumeroRighe()):
            prodottoTrovato = self.magazzino.getMagazzino()[riga]
            item = self.tableWidget.item(riga, 0)
            item.setText(_translate("Frame", prodottoTrovato.getNomeProdotto()))
            item = self.tableWidget.item(riga, 1)
            item.setText(_translate("Frame", prodottoTrovato.getQuantitaMagazzino()))
            item = self.tableWidget.item(riga, 2)
            item.setText(_translate("Frame", ""))

        self.pushButtonAggiungiAcquisto.setText(_translate("Frame", "Aggiungi Acquisto"))

    # Metodo usato per leggere il numero delle righe all'interno
    # del file "Magazzino.txt" per creare un numero di righe pari
    # al numero dei prodotti salvati.
    def leggiNumeroRighe(self):
        return len(self.magazzino.getMagazzino())

    # Metodo che permette di ritornare all'interfaccia iniziale
    # del programma, ovvero LoginAmministratore.
    def openLogin(self):
        from Grafica.GestioneLogin.LoginAmministratore import LoginAmministratore
        self.login = QtWidgets.QFrame()
        self.ui = LoginAmministratore()
        self.ui.setupUi(self.login)
        self.login.show()
        self.frame.close()

    # Metodo che permette di ritornare all'interfaccia InserisciCodiceAbbonamento.
    def openInserisciCodiceAbbonamento(self):
        from Grafica.GestioneVendite.InserisciCodiceAbbonamento import InserisciCodiceAbbonamento
        self.inserisciCodiceAbbonamento = QtWidgets.QFrame()
        self.ui = InserisciCodiceAbbonamento()
        self.ui.setupUi(self.inserisciCodiceAbbonamento)
        self.inserisciCodiceAbbonamento.show()
        self.frame.close()

    # Metodo utilizzato per ritrovare all'interno della tabella
    # i prodotti che hanno la stessa parte di stringa s.
    def search(self, s):
        items = self.tableWidget.findItems(s, Qt.MatchContains)
        if items:  # we have found something
            item = items[0]  # take the first
            self.tableWidget.setCurrentItem(item)

    # Metodo utilizzato per vedere quali e quanti sono i prodotti
    # che sono stati venduti.
    def clickAggiungiAcquisto(self):
        self.gestoreVendite.getListaPrezziProdotti().clear()
        self.gestoreVendite.listaAcquisti().clear()
        numeroProdottiAcquistati = 0
        checkBoxChecked = 0

        for riga in range(self.leggiNumeroRighe()):

            if self.tableWidget.item(riga, 0).checkState() == QtCore.Qt.Checked:
                checkBoxChecked += 1
                quantitaAcquistate = self.tableWidget.item(riga, 2).text()
                prodotto = self.magazzino.getMagazzino()[riga]
                if quantitaAcquistate.isnumeric():
                    if int(quantitaAcquistate) != 0:
                        if int(quantitaAcquistate) <= int(prodotto.getQuantitaMagazzino()):
                            if self.controllo is True:
                                if prodotto.getTipoOfferta() == "Abbonati":
                                    numeroProdottiAcquistati += 1
                                    prezzo = prodotto.getPrezzoOfferta()
                                    self.gestoreVendite.aggiungiPrezzoProdotto(prezzo)
                                    acquistoAppoggio = Acquisto(prodotto, quantitaAcquistate)
                                    self.gestoreVendite.aggiungiAcquisto(acquistoAppoggio)
                                else:
                                    if prodotto.getTipoOfferta() == "Generale":
                                        numeroProdottiAcquistati += 1
                                        prezzo = prodotto.getPrezzoOfferta()
                                        self.gestoreVendite.aggiungiPrezzoProdotto(prezzo)
                                        acquistoAppoggio = Acquisto(prodotto, quantitaAcquistate)
                                        self.gestoreVendite.aggiungiAcquisto(acquistoAppoggio)
                                    else:
                                        numeroProdottiAcquistati += 1
                                        prezzo = prodotto.getPrezzo()
                                        self.gestoreVendite.aggiungiPrezzoProdotto(prezzo)
                                        acquistoAppoggio = Acquisto(prodotto, quantitaAcquistate)
                                        self.gestoreVendite.aggiungiAcquisto(acquistoAppoggio)
                            else:
                                if prodotto.getTipoOfferta() == "Generale":
                                    numeroProdottiAcquistati += 1
                                    prezzo = prodotto.getPrezzoOfferta()
                                    self.gestoreVendite.aggiungiPrezzoProdotto(prezzo)
                                    acquistoAppoggio = Acquisto(prodotto, quantitaAcquistate)
                                    self.gestoreVendite.aggiungiAcquisto(acquistoAppoggio)
                                else:
                                    numeroProdottiAcquistati += 1
                                    prezzo = prodotto.getPrezzo()
                                    self.gestoreVendite.aggiungiPrezzoProdotto(prezzo)
                                    acquistoAppoggio = Acquisto(prodotto, quantitaAcquistate)
                                    self.gestoreVendite.aggiungiAcquisto(acquistoAppoggio)
                        else:
                            self.ErrorQuantitaMagazzino()
                    else:
                        self.ErrorQuantita()
                else:
                    self.ErrorNumero()

        if numeroProdottiAcquistati != 0 and checkBoxChecked == numeroProdottiAcquistati:
            self.openScontrino(self.gestoreVendite.listaAcquisti(), self.gestoreVendite.getListaPrezziProdotti())
        else:
            self.ErrorAcquisti()
    # Metodo che permette di aprire l'interfaccia sulla quale
    # si può creare lo scontrino.
    def openScontrino(self, acquisti, listaPrezziProdotti):
        from Grafica.GestioneVendite.Scontrino import Scontrino
        self.scontrino = QtWidgets.QFrame()
        self.ui = Scontrino()
        self.ui.setupUi(self.scontrino, acquisti, listaPrezziProdotti, self.gestoreVendite, self.frame)
        self.scontrino.show()
        self.frame.hide()

    def ErrorQuantitaMagazzino(self):
        self.ErrorBox = QMessageBox()
        self.ErrorBox.setWindowTitle("Errore")
        self.ErrorBox.setText("Impossibile acquistare più prodotti\ndi quelli presenti in magazzino.")
        self.ErrorBox.setStyleSheet(
            "QLabel{min-width:300 px; font-size: 14px; font-family: Helvetica, Sans-Serif; } QPushButton:hover{"
            "background-color: #14626c;color:white; }QPushButton{ width:40px; height:20px; font-size: 10px; "
            "font-family: Helvetica, Sans-Serif; border: 1px solid black; border-radius: 5px; }")
        self.ErrorBox.exec()

    def ErrorQuantita(self):
        self.ErrorBox = QMessageBox()
        self.ErrorBox.setWindowTitle("Errore")
        self.ErrorBox.setText("La quantità da acquistare non può \nessere zero.")
        self.ErrorBox.setStyleSheet(
            "QLabel{min-width:300 px; font-size: 14px; font-family: Helvetica, Sans-Serif; } QPushButton:hover{"
            "background-color: #14626c;color:white; }QPushButton{ width:40px; height:20px; font-size: 10px; "
            "font-family: Helvetica, Sans-Serif; border: 1px solid black; border-radius: 5px; }")
        self.ErrorBox.exec()

    def ErrorNumero(self):
        self.ErrorBox = QMessageBox()
        self.ErrorBox.setWindowTitle("Errore")
        self.ErrorBox.setText("La quantità da acquistare può essere\nsolo un numero.")
        self.ErrorBox.setStyleSheet(
            "QLabel{min-width:300 px; font-size: 14px; font-family: Helvetica, Sans-Serif; } QPushButton:hover{"
            "background-color: #14626c;color:white; }QPushButton{ width:40px; height:20px; font-size: 10px; "
            "font-family: Helvetica, Sans-Serif; border: 1px solid black; border-radius: 5px; }")
        self.ErrorBox.exec()

    def ErrorAcquisti(self):
        self.ErrorBox = QMessageBox()
        self.ErrorBox.setWindowTitle("Errore")
        self.ErrorBox.setText("Per creare uno scontrino è necessario \n selezionare uno o più prodotti.")
        self.ErrorBox.setStyleSheet(
            "QLabel{min-width:300 px; font-size: 14px; font-family: Helvetica, Sans-Serif; } QPushButton:hover{"
            "background-color: #14626c;color:white; }QPushButton{ width:40px; height:20px; font-size: 10px; "
            "font-family: Helvetica, Sans-Serif; border: 1px solid black; border-radius: 5px; }")
        self.ErrorBox.exec()
