from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

from GestioneMagazzino.Magazzino import Magazzino


class AggiungiProdotto(object):

    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(387, 415)
        Frame.setStyleSheet("QFrame{\n"
                            "background-color: rgb(255, 255, 255);\n"
                            "}")
        Frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame = Frame
        self.label = QtWidgets.QLabel(Frame)
        self.label.setGeometry(QtCore.QRect(10, 70, 391, 31))
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setStyleSheet("QLabel{\n"
                                 "font-family: Helvetica, sans-serif;\n"
                                 "font-weight: 400;\n"
                                 "font-size: 16px\n"
                                 "}")
        self.label.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Frame)
        self.label_2.setGeometry(QtCore.QRect(10, 130, 391, 31))
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setStyleSheet("QLabel{\n"
                                   "font-family: Helvetica, sans-serif;\n"
                                   "font-weight: 400;\n"
                                   "font-size: 16px\n"
                                   "}")
        self.label_2.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Frame)
        self.label_3.setGeometry(QtCore.QRect(10, 190, 391, 31))
        self.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_3.setStyleSheet("QLabel{\n"
                                   "font-family: Helvetica, sans-serif;\n"
                                   "font-weight: 400;\n"
                                   "font-size: 16px\n"
                                   "}")
        self.label_3.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.lineEditNomeProdotto = QtWidgets.QLineEdit(Frame)
        self.lineEditNomeProdotto.setGeometry(QtCore.QRect(10, 100, 371, 31))
        self.lineEditNomeProdotto.setStyleSheet("QLineEdit{\n"
                                                "border: 2px solid black;\n"
                                                "border-radius: 6px;\n"
                                                "}")
        self.lineEditNomeProdotto.setObjectName("lineEdit")
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
        self.pushButtonLogout.setGeometry(QtCore.QRect(10, 380, 141, 31))
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
        icon.addPixmap(QtGui.QPixmap(
            "Images\\log.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonLogout.setIcon(icon)
        self.pushButtonLogout.setCheckable(False)
        self.pushButtonLogout.setObjectName("pushButton_5")
        self.pushButtonInserisci = QtWidgets.QPushButton(Frame)
        self.pushButtonInserisci.setGeometry(QtCore.QRect(10, 320, 371, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonInserisci.setFont(font)
        self.pushButtonInserisci.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButtonInserisci.setStyleSheet("QPushButton{\n"
                                               "border: 2px solid black;\n"
                                               "border-radius: 10px;\n"
                                               "}\n"
                                               "QPushButton:hover{\n"
                                               "\n"
                                               "background-color: #14626c;\n"
                                               "color:white;\n"
                                               "}")
        self.pushButtonInserisci.setCheckable(False)
        self.pushButtonInserisci.setObjectName("pushButton_6")
        self.pushButtonGestioneMagazzino = QtWidgets.QPushButton(Frame)
        self.pushButtonGestioneMagazzino.setGeometry(QtCore.QRect(160, 380, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonGestioneMagazzino.setFont(font)
        self.pushButtonGestioneMagazzino.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButtonGestioneMagazzino.setStyleSheet("QPushButton{\n"
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
            "Images\\left.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonGestioneMagazzino.setIcon(icon1)
        self.pushButtonGestioneMagazzino.setObjectName("pushButton_4")
        self.label_5 = QtWidgets.QLabel(Frame)
        self.label_5.setGeometry(QtCore.QRect(10, 250, 391, 31))
        self.label_5.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_5.setStyleSheet("QLabel{\n"
                                   "font-family: Helvetica, sans-serif;\n"
                                   "font-weight: 400;\n"
                                   "font-size: 16px\n"
                                   "}")
        self.label_5.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.lineEditCodiceSeriale = QtWidgets.QLineEdit(Frame)
        self.lineEditCodiceSeriale.setGeometry(QtCore.QRect(10, 280, 371, 31))
        self.lineEditCodiceSeriale.setStyleSheet("QLineEdit{\n"
                                                 "border: 2px solid black;\n"
                                                 "border-radius: 6px;\n"
                                                 "}")
        self.lineEditCodiceSeriale.setObjectName("lineEdit_4")
        self.spinBoxQuantita = QtWidgets.QSpinBox(Frame)
        self.spinBoxQuantita.setGeometry(QtCore.QRect(330, 160, 51, 31))
        self.spinBoxQuantita.setStyleSheet("QSpinBox{\n"
                                           "border: 2px solid black;\n"
                                           "border-radius: 6px;\n"
                                           "}\n"
                                           "\n"
                                           "\n"
                                           "")
        self.spinBoxQuantita.setWrapping(False)
        self.spinBoxQuantita.setFrame(True)
        self.spinBoxQuantita.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBoxQuantita.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.spinBoxQuantita.setSpecialValueText("")
        self.spinBoxQuantita.setObjectName("spinBox")
        self.doubleSpinBoxPrezzo = QtWidgets.QDoubleSpinBox(Frame)
        self.doubleSpinBoxPrezzo.setGeometry(QtCore.QRect(330, 220, 51, 31))
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
        self.horizontalSlider = QtWidgets.QSlider(Frame)
        self.horizontalSlider.setGeometry(QtCore.QRect(10, 160, 301, 31))
        self.horizontalSlider.setStyleSheet("QSlider::groove:horizontal {\n"
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
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalSlider_2 = QtWidgets.QSlider(Frame)
        self.horizontalSlider_2.setGeometry(QtCore.QRect(10, 220, 301, 31))
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
        self.pushButtonInserisci.clicked.connect(self.clickInserisci)
        self.pushButtonLogout.clicked.connect(self.openLogin)
        self.pushButtonGestioneMagazzino.clicked.connect(self.openGestioneMagazzinoPrincipale)

        self.retranslateUi(Frame)
        self.horizontalSlider.sliderMoved['int'].connect(self.spinBoxQuantita.setValue)
        self.spinBoxQuantita.valueChanged['int'].connect(self.horizontalSlider.setValue)
        self.horizontalSlider_2.sliderMoved['int'].connect(self.doubleSpinBoxPrezzo.setValue)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Fumetteria - Inserisci Prodotto"))
        self.label.setText(_translate("Frame", "Inserisci nome prodotto da aggiungere:"))
        self.label_2.setText(_translate("Frame", "Inserisci quantità prodotto:"))
        self.label_3.setText(_translate("Frame", "Inserisci prezzo: "))
        self.label_4.setText(_translate("Frame", "INSERISCI PRODOTTO"))
        self.pushButtonLogout.setText(_translate("Frame", " Logout"))
        self.pushButtonInserisci.setText(_translate("Frame", "Inserisci"))
        self.pushButtonGestioneMagazzino.setText(_translate("Frame", " Indietro"))
        self.label_5.setText(_translate("Frame", "Inserisci codice seriale:"))

    # Metodo che serve ad aggiungere un nuovo prodotto all'interno della
    # lista nel file di testo "Magazzino.txt" dopo aver cliccato il pulsante
    # Inserisci Prodotto.
    # Nel caso in cui il nome e/o il codice immessi siano già utilizzati da altri
    # prodotti viene visualizzata una finestra di errore.
    # Nel caso in cui il prezzo e/o la quantità del prodotto siano lasciati a zero,
    # viene visualizzata una finestra di errore.
    # Nel caso in cui non si verificano gli errori sopra citati,
    # viene richiamato il metodo "aggiungiProdotto" della classe Magazzino,
    # utilizzato per aggiungere all'interno del file di testo
    # "Magazzino.txt" il prodotto con gli attributi settati ai valori
    # immessi tramite interfaccia. Una volta aggiunto il prodotto
    # viene richiamato il metodo "self.openAggiungiProdottoEffettuato".
    def clickInserisci(self):
        magazzino = Magazzino()

        nome = self.lineEditNomeProdotto.text()
        quantita = self.spinBoxQuantita.text()
        prezzo = self.doubleSpinBoxPrezzo.text()
        codiceSeriale = self.lineEditCodiceSeriale.text()

        # Risolve un problema d'incompatibilità dello spinBox
        # tra le versione di Windows10 e Windows11.
        if "," in prezzo:
            prezzoVector = prezzo.split(",")
            prezzo = prezzoVector[0] + "." + prezzoVector[1]

        if codiceSeriale.isnumeric() is True:
            if nome != "":
                if quantita != "0":
                    if prezzo != "0.00":
                        if magazzino.aggiungiProdotto(nome, quantita, prezzo, codiceSeriale) is True:
                            self.openAggiungiProdottoEffettuato()
                        else:
                            self.ErrorProdottoEsistente()
                    else:
                        self.ErrorPrezzo()
                else:
                    self.ErrorQuantita()
            else:
                self.ErrorNome()
        else:
            self.ErrorCodice()

    # Metodo che permette di aprire all'interfaccia AggiungiProdottoEffettuato.
    def openAggiungiProdottoEffettuato(self):
        from Grafica.GestioneMagazzino.AggiungiProdottoEffettuato import AggiungiProdottoEffettuato
        self.aggiungiProdottoFunzionante = QtWidgets.QFrame()
        self.ui = AggiungiProdottoEffettuato()
        self.ui.setupUi(self.aggiungiProdottoFunzionante)
        self.aggiungiProdottoFunzionante.show()
        self.frame.close()

    # Metodo che permette di ritornare all'interfaccia GestioneMagazzinoPrincipale.
    def openGestioneMagazzinoPrincipale(self):
        from Grafica.GestioneMagazzino.GestioneMagazzinoPrincipale import GestioneMagazzinoPrincipale
        self.gestioneMagazzinoPrincipale = QtWidgets.QFrame()
        self.ui = GestioneMagazzinoPrincipale()
        self.ui.setupUi(self.gestioneMagazzinoPrincipale)
        self.gestioneMagazzinoPrincipale.show()
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

    def ErrorProdottoEsistente(self):
        self.ErrorBox = QMessageBox()
        self.ErrorBox.setWindowTitle("Errore")
        self.ErrorBox.setText("Il prodotto è già presente")
        self.ErrorBox.setStyleSheet(
            "QLabel{min-width:200 px; font-size: 14px; font-family: Helvetica, Sans-Serif; } QPushButton:hover{"
            "background-color: #14626c;color:white; }QPushButton{ width:40px; height:20px; font-size: 10px; "
            "font-family: Helvetica, Sans-Serif; border: 1px solid black; border-radius: 5px; }")
        self.ErrorBox.exec()

    def ErrorQuantita(self):
        self.ErrorBox = QMessageBox()
        self.ErrorBox.setWindowTitle("Errore")
        self.ErrorBox.setText("La quantità non può essere 0")
        self.ErrorBox.setStyleSheet(
            "QLabel{min-width:200 px; font-size: 14px; font-family: Helvetica, Sans-Serif; } QPushButton:hover{"
            "background-color: #14626c;color:white; }QPushButton{ width:40px; height:20px; font-size: 10px; "
            "font-family: Helvetica, Sans-Serif; border: 1px solid black; border-radius: 5px; }")
        self.ErrorBox.exec()

    def ErrorNome(self):
        self.ErrorBox = QMessageBox()
        self.ErrorBox.setWindowTitle("Errore")
        self.ErrorBox.setText("Inserisci il nome del prodotto")
        self.ErrorBox.setStyleSheet(
            "QLabel{min-width:200 px; font-size: 14px; font-family: Helvetica, Sans-Serif; } QPushButton:hover{"
            "background-color: #14626c;color:white; }QPushButton{ width:40px; height:20px; font-size: 10px; "
            "font-family: Helvetica, Sans-Serif; border: 1px solid black; border-radius: 5px; }")
        self.ErrorBox.exec()

    def ErrorPrezzo(self):
        self.ErrorBox = QMessageBox()
        self.ErrorBox.setWindowTitle("Errore")
        self.ErrorBox.setText("Il prezzo non può essere 0")
        self.ErrorBox.setStyleSheet(
            "QLabel{min-width:200 px; font-size: 14px; font-family: Helvetica, Sans-Serif; } QPushButton:hover{"
            "background-color: #14626c;color:white; }QPushButton{ width:40px; height:20px; font-size: 10px; "
            "font-family: Helvetica, Sans-Serif; border: 1px solid black; border-radius: 5px; }")
        self.ErrorBox.exec()

    def ErrorCodice(self):
        self.ErrorBox = QMessageBox()
        self.ErrorBox.setWindowTitle("Errore")
        self.ErrorBox.setText("Il codice deve avere solo cifre")
        self.ErrorBox.setStyleSheet(
            "QLabel{min-width:200 px; font-size: 14px; font-family: Helvetica, Sans-Serif; } QPushButton:hover{"
            "background-color: #14626c;color:white; }QPushButton{ width:40px; height:20px; font-size: 10px; "
            "font-family: Helvetica, Sans-Serif; border: 1px solid black; border-radius: 5px; }")
        self.ErrorBox.exec()

