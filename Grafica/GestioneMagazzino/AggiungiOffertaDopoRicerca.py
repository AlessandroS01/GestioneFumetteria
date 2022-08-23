from datetime import datetime

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

from Amministratore.Amministratore import Amministratore


class AggiungiOffertaDopoRicerca(object):

    def setupUi(self, Frame, prodotto):
        self.prodottoTrovato = prodotto
        Frame.setObjectName("Frame")
        Frame.resize(387, 386)
        Frame.setStyleSheet("QFrame{\n"
                            "background-color: rgb(255, 255, 255);\n"
                            "}")
        Frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame = Frame
        self.label = QtWidgets.QLabel(Frame)
        self.label.setGeometry(QtCore.QRect(10, 70, 371, 31))
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setStyleSheet("QLabel{\n"
                                 "font-family: Helvetica, sans-serif;\n"
                                 "font-weight: 400;\n"
                                 "font-size: 16px\n"
                                 "}")
        self.label.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
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
        self.pushButtonLogout = QtWidgets.QPushButton(Frame)
        self.pushButtonLogout.setGeometry(QtCore.QRect(10, 350, 141, 31))
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
        self.pushButtonRicercaProdottoSuccesso = QtWidgets.QPushButton(Frame)
        self.pushButtonRicercaProdottoSuccesso.setGeometry(QtCore.QRect(160, 350, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonRicercaProdottoSuccesso.setFont(font)
        self.pushButtonRicercaProdottoSuccesso.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButtonRicercaProdottoSuccesso.setStyleSheet("QPushButton{\n"
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
        self.pushButtonRicercaProdottoSuccesso.setIcon(icon1)
        self.pushButtonRicercaProdottoSuccesso.setObjectName("pushButton_4")
        self.radioButtonGenerale = QtWidgets.QRadioButton(Frame)
        self.radioButtonGenerale.setGeometry(QtCore.QRect(10, 106, 82, 21))
        self.radioButtonGenerale.setStyleSheet("QRadioButton{\n"
                                               "font-family: Helvetica, sans-serif;\n"
                                               "font-size:13px;\n"
                                               "}")
        self.radioButtonGenerale.setChecked(True)
        self.radioButtonGenerale.setObjectName("radioButton")
        self.TipoOfferta = QtWidgets.QButtonGroup(Frame)
        self.TipoOfferta.setObjectName("TipoOfferta")
        self.TipoOfferta.addButton(self.radioButtonGenerale)
        self.radioButtonAbbonati = QtWidgets.QRadioButton(Frame)
        self.radioButtonAbbonati.setGeometry(QtCore.QRect(10, 130, 82, 21))
        self.radioButtonAbbonati.setStyleSheet("QRadioButton{\n"
                                               "font-family: Helvetica, sans-serif;\n"
                                               "font-size:13px;\n"
                                               "}")
        self.radioButtonAbbonati.setObjectName("radioButton_2")
        self.TipoOfferta.addButton(self.radioButtonAbbonati)
        self.label_2 = QtWidgets.QLabel(Frame)
        self.label_2.setGeometry(QtCore.QRect(10, 150, 371, 31))
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setStyleSheet("QLabel{\n"
                                   "font-family: Helvetica, sans-serif;\n"
                                   "font-weight: 400;\n"
                                   "font-size: 16px\n"
                                   "}")
        self.label_2.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.doubleSpinBoxPrezzo = QtWidgets.QDoubleSpinBox(Frame)
        self.doubleSpinBoxPrezzo.setGeometry(QtCore.QRect(330, 180, 51, 31))
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
        self.horizontalSlider_2.setGeometry(QtCore.QRect(10, 180, 301, 31))
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
        self.label_3 = QtWidgets.QLabel(Frame)
        self.label_3.setGeometry(QtCore.QRect(10, 220, 371, 21))
        self.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_3.setStyleSheet("QLabel{\n"
                                   "font-family: Helvetica, sans-serif;\n"
                                   "font-weight: 400;\n"
                                   "font-size: 16px\n"
                                   "}")
        self.label_3.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.dateEditDataScadenzaOfferta = QtWidgets.QDateEdit(Frame)
        self.dateEditDataScadenzaOfferta.setGeometry(QtCore.QRect(10, 250, 371, 31))
        self.dateEditDataScadenzaOfferta.setStyleSheet("QDateEdit{\n"
                                                       "border: 2px solid black;\n"
                                                       "border-radius: 6px;\n"
                                                       "}")
        self.dateEditDataScadenzaOfferta.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.dateEditDataScadenzaOfferta.setCalendarPopup(False)
        self.dateEditDataScadenzaOfferta.setDate(QtCore.QDate(2023, 1, 1))
        self.dateEditDataScadenzaOfferta.setObjectName("dateEdit")
        self.pushButtonAggiungiOfferta = QtWidgets.QPushButton(Frame)
        self.pushButtonAggiungiOfferta.setGeometry(QtCore.QRect(10, 290, 371, 31))
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
        self.pushButtonAggiungiOfferta.setObjectName("pushButton_6")
        self.pushButtonAggiungiOfferta.clicked.connect(self.clickAggiungiOfferta)
        self.pushButtonLogout.clicked.connect(self.openLogin)
        self.pushButtonRicercaProdottoSuccesso.clicked.connect(self.openRicercaProdottoSuccesso)

        self.horizontalSlider_2.sliderMoved['int'].connect(self.doubleSpinBoxPrezzo.setValue)
        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Fumetteria - Aggiungi Offerta"))
        self.label.setText(_translate("Frame", "Seleziona il tipo di offerta da aggiungere:"))
        self.label_4.setText(_translate("Frame", "AGGIUNGI OFFERTA"))
        self.pushButtonLogout.setText(_translate("Frame", " Logout"))
        self.pushButtonRicercaProdottoSuccesso.setText(_translate("Frame", " Indietro"))
        self.radioButtonGenerale.setText(_translate("Frame", "Generale"))
        self.radioButtonAbbonati.setText(_translate("Frame", "Abbonati"))
        self.label_2.setText(_translate("Frame", "Prezzo imposto dall\'offerta:"))
        self.label_3.setText(_translate("Frame", "Data scadenza offerta:"))
        self.pushButtonAggiungiOfferta.setText(_translate("Frame", "Aggiungi Offerta"))

    # Metodo che serve ad aggiungere un'offerta a un prodotto
    # precedentemente sprovvisto.
    # Nel caso in cui il prezzo dell'offerta venga settato a zero
    # o maggiore del prezzo di base del prodotto viene visualizzata
    # una finestra d'errore.
    # Nel caso in cui la data immessa è precedente alla data dell'utilizzo
    # del programma viene visualizzata una finestra d'errore.
    # Nel caso in cui invece non si commettano gli errori precedenti,
    # viene richiamato il metodo "aggiungiOffertaProdotto" di Amministratore
    # per settare l'offerta al prodotto.
    # In seguito viene richiamato il metodo "self.openAggiungiOffertaSuccesso".
    def clickAggiungiOfferta(self):
        amministratore = Amministratore()

        tipoOfferta = self.TipoOfferta.checkedButton().text()
        prezzoOfferta = self.doubleSpinBoxPrezzo.text()
        dataScadenzaOffertaText = self.dateEditDataScadenzaOfferta.text()

        dataScadenzaOffertaDatetime = datetime.strptime(dataScadenzaOffertaText, '%d/%m/%Y').date()
        today = datetime.now().date()

        # Risolve un problema d'incompatibilità dello spinBox
        # tra le versione di Windows10 e Windows11.
        if "," in prezzoOfferta:
            prezzoVector = prezzoOfferta.split(",")
            prezzoOfferta = prezzoVector[0] + "." + prezzoVector[1]

        if prezzoOfferta != "0.00":
            if float(prezzoOfferta) < float(self.prodottoTrovato.getPrezzo()):
                if dataScadenzaOffertaDatetime > today:
                    amministratore.aggiungiOffertaProdotto(self.prodottoTrovato.getCodiceSeriale(),
                                                           tipoOfferta, prezzoOfferta,
                                                           dataScadenzaOffertaText)
                    self.openAggiungiOffertaSuccesso()
                else:
                    self.ErrorData()
            else:
                self.ErrorPrezzoOfferta()
        else:
            self.ErrorPrezzo()

    # Metodo che fa visualizzare a schermo l'interfaccia AggiungiOffertaDopoRicercaSuccesso.
    def openAggiungiOffertaSuccesso(self):
        from Grafica.GestioneMagazzino.AggiungiOffertaDopoRicercaSuccesso import AggiungiOffertaDopoRicercaSuccesso
        self.aggiungiOffertaSuccesso = QtWidgets.QFrame()
        self.ui = AggiungiOffertaDopoRicercaSuccesso()
        self.ui.setupUi(self.aggiungiOffertaSuccesso)
        self.aggiungiOffertaSuccesso.show()
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

    # Metodo che riporta l'utente all'interno della schermata RicercaProdottoSuccesso
    # dopo aver cliccato indietro.
    def openRicercaProdottoSuccesso(self):
        from Grafica.GestioneMagazzino.RicercaProdottoSuccesso import RicercaProdottoSuccesso
        self.ricercaProdottoSuccesso = QtWidgets.QFrame()
        self.ui = RicercaProdottoSuccesso()
        self.ui.setupUi(self.ricercaProdottoSuccesso, self.prodottoTrovato)
        self.ricercaProdottoSuccesso.show()
        self.frame.close()

    def ErrorPrezzo(self):
        self.ErrorBox = QMessageBox()
        self.ErrorBox.setWindowTitle("Errore")
        self.ErrorBox.setText("Aggiungere il prezzo dell'offerta")
        self.ErrorBox.setStyleSheet(
            "QLabel{min-width:200 px; font-size: 14px; font-family: Helvetica, Sans-Serif; } QPushButton:hover{"
            "background-color: #14626c;color:white; }QPushButton{ width:40px; height:20px; font-size: 10px; "
            "font-family: Helvetica, Sans-Serif; border: 1px solid black; border-radius: 5px; }")
        self.ErrorBox.exec()

    def ErrorPrezzoOfferta(self):
        self.ErrorBox = QMessageBox()
        self.ErrorBox.setWindowTitle("Errore")
        self.ErrorBox.setText("Il prezzo dell'offerta non può \nessere maggiore del prezzo \nstandard.")
        self.ErrorBox.setStyleSheet(
            "QLabel{min-width:200 px; font-size: 14px; font-family: Helvetica, Sans-Serif; } QPushButton:hover{"
            "background-color: #14626c;color:white; }QPushButton{ width:40px; height:20px; font-size: 10px; "
            "font-family: Helvetica, Sans-Serif; border: 1px solid black; border-radius: 5px; }")
        self.ErrorBox.exec()

    def ErrorData(self):
        self.ErrorBox = QMessageBox()
        self.ErrorBox.setWindowTitle("Errore")
        self.ErrorBox.setText("Re-inserire la data")
        self.ErrorBox.setStyleSheet(
            "QLabel{min-width:200 px; font-size: 14px; font-family: Helvetica, Sans-Serif; } QPushButton:hover{"
            "background-color: #14626c;color:white; }QPushButton{ width:40px; height:20px; font-size: 10px; "
            "font-family: Helvetica, Sans-Serif; border: 1px solid black; border-radius: 5px; }")
        self.ErrorBox.exec()
