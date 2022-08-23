from pathlib import Path

from PyQt5 import QtCore, QtGui, QtWidgets


class EliminaProdotto(object):

    def setupUi(self, Frame, prodotto):
        self.prodottoTrovato = prodotto
        Frame.setObjectName("Frame")
        Frame.resize(387, 246)
        Frame.setStyleSheet("QFrame{\n"
                            "background-color: rgb(255, 255, 255);\n"
                            "}")
        Frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame = Frame
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
        self.pushButtonLogout.setGeometry(QtCore.QRect(10, 200, 141, 31))
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
        self.pushButtonModificaPrincipale = QtWidgets.QPushButton(Frame)
        self.pushButtonModificaPrincipale.setGeometry(QtCore.QRect(160, 200, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonModificaPrincipale.setFont(font)
        self.pushButtonModificaPrincipale.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButtonModificaPrincipale.setStyleSheet("QPushButton{\n"
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
        self.pushButtonModificaPrincipale.setIcon(icon1)
        self.pushButtonModificaPrincipale.setObjectName("pushButton_4")
        self.label_5 = QtWidgets.QLabel(Frame)
        self.label_5.setGeometry(QtCore.QRect(10, 70, 371, 61))
        self.label_5.setStyleSheet("QLabel{\n"
                                   "font-family: Helvetica, sans-serif;\n"
                                   "font-weight: 400;\n"
                                   "font-size: 16px\n"
                                   "}")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.pushButtonElimina = QtWidgets.QPushButton(Frame)
        self.pushButtonElimina.setGeometry(QtCore.QRect(10, 130, 361, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonElimina.setFont(font)
        self.pushButtonElimina.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButtonElimina.setStyleSheet("QPushButton{\n"
                                             "border: 2px solid black;\n"
                                             "border-radius: 10px;\n"
                                             "}\n"
                                             "QPushButton:hover{\n"
                                             "\n"
                                             "background-color: #14626c;\n"
                                             "color:white;\n"
                                             "}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Images\\delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonElimina.setIcon(icon2)
        self.pushButtonElimina.setCheckable(False)
        self.pushButtonElimina.setObjectName("pushButton_7")
        self.pushButtonLogout.clicked.connect(self.openLogin)
        self.pushButtonModificaPrincipale.clicked.connect(self.openModificaPrincipaleProdotto)
        self.pushButtonElimina.clicked.connect(self.clickElimina)

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Fumetteria - Elimina Prodotto"))
        self.label_4.setText(_translate("Frame", "ELIMINA PRODOTTO"))
        self.pushButtonLogout.setText(_translate("Frame", " Logout"))
        self.pushButtonModificaPrincipale.setText(_translate("Frame", " Indietro"))
        self.label_5.setText(_translate("Frame", "Sei sicuro di voler eliminare il prodotto in modo\n"
                                                 " definitivo dal magazzino ?"))
        self.pushButtonElimina.setText(_translate("Frame", " Elimina il prodotto"))

    # Metodo che riporta l'utente all'interno della schermata ModificaPrincipalePrincipale
    def openModificaPrincipaleProdotto(self):
        from Grafica.GestioneMagazzino.ModificaProdotto.ModificaPrincipaleProdotto import ModificaPrincipaleProdotto
        self.modificaPrincipaleProdotto = QtWidgets.QFrame()
        self.ui = ModificaPrincipaleProdotto()
        self.ui.setupUi(self.modificaPrincipaleProdotto, self.prodottoTrovato)
        self.modificaPrincipaleProdotto.show()
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

    # Metodo che permette di eliminare il prodotto trovato
    # dalla lista dei prodotti in "Magazzino.txt".
    # Il metodo consiste nel salvare una nuova lista formata
    # da tutti i prodotti della lista primaria senza il prodotto
    # trovato e salvare la nuova lista all'interno del file di testo
    # "Magazzino.txt".
    # Una volta eliminato viene richiamato il metodo
    # "self.openEliminazioneEffettuata".
    def clickElimina(self):

        pathRelativo = Path("Magazzino")
        pathAssoluto = pathRelativo.absolute()

        data = self.prodottoTrovato.getProdotto()

        rimpiazzo = []
        stringaAppoggio = str()

        with open(pathAssoluto, "r") as f:
            lines = f.readlines()
            lista = lines

        with open(pathAssoluto, 'w') as f:
            for index in range(0, len(lista)):
                line = str(lista[index].rstrip())
                if line != data:
                    rimpiazzo.append(line)

            for index in range(0, len(rimpiazzo)):
                if index == 0:
                    stringaAppoggio = rimpiazzo[index]
                else:
                    stringaAppoggio += "\n" + rimpiazzo[index]

            f.write(stringaAppoggio)

        self.openEliminazioneEffettuata()

    # Metodo che fa visualizzare a schermo l'interfaccia EliminazioneEffettuata.
    def openEliminazioneEffettuata(self):
        from Grafica.GestioneMagazzino.ModificaProdotto.EliminazioneEffetuata import EliminazioneEffettuata
        self.eliminazioneEffettuata = QtWidgets.QFrame()
        self.ui = EliminazioneEffettuata()
        self.ui.setupUi(self.eliminazioneEffettuata)
        self.eliminazioneEffettuata.show()
        self.frame.close()
