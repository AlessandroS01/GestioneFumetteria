from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

from Amministratore.Amministratore import Amministratore
from Grafica.GestioneAccount.ModificaEffettuata import ModificaEffetuata


class ModificaPassword(object):

    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(390, 362)
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
        self.lineEditNomeUtente = QtWidgets.QLineEdit(Frame)
        self.lineEditNomeUtente.setGeometry(QtCore.QRect(10, 100, 371, 31))
        self.lineEditNomeUtente.setStyleSheet("QLineEdit{\n"
                                              "border: 2px solid black;\n"
                                              "border-radius: 6px;\n"
                                              "}")
        self.lineEditNomeUtente.setObjectName("lineEdit")
        self.lineEditPasswordVecchia = QtWidgets.QLineEdit(Frame)
        self.lineEditPasswordVecchia.setGeometry(QtCore.QRect(10, 160, 371, 31))
        self.lineEditPasswordVecchia.setStyleSheet("QLineEdit{\n"
                                                   "border: 2px solid black;\n"
                                                   "border-radius: 6px;\n"
                                                   "}")
        self.lineEditPasswordVecchia.setObjectName("lineEdit_2")
        self.lineEditPasswordNuova = QtWidgets.QLineEdit(Frame)
        self.lineEditPasswordNuova.setGeometry(QtCore.QRect(10, 220, 371, 31))
        self.lineEditPasswordNuova.setStyleSheet("QLineEdit{\n"
                                                 "border: 2px solid black;\n"
                                                 "border-radius: 6px;\n"
                                                 "}")
        self.lineEditPasswordNuova.setObjectName("lineEdit_3")
        self.label_4 = QtWidgets.QLabel(Frame)
        self.label_4.setGeometry(QtCore.QRect(20, 20, 381, 31))
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
        self.pushButtonModifica = QtWidgets.QPushButton(Frame)
        self.pushButtonModifica.setGeometry(QtCore.QRect(10, 260, 371, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonModifica.setFont(font)
        self.pushButtonModifica.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButtonModifica.setStyleSheet("QPushButton{\n"
                                              "border: 2px solid black;\n"
                                              "border-radius: 10px;\n"
                                              "}\n"
                                              "QPushButton:hover{\n"
                                              "\n"
                                              "background-color: #14626c;\n"
                                              "color:white;\n"
                                              "}")
        self.pushButtonModifica.setCheckable(False)
        self.pushButtonModifica.setObjectName("pushButton_6")
        self.pushButtonLogout = QtWidgets.QPushButton(Frame)
        self.pushButtonLogout.setGeometry(QtCore.QRect(10, 320, 141, 31))
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
        self.pushButtonLogout.setObjectName("pushButton_7")
        self.pushButtonGestioneAccountPrincipale = QtWidgets.QPushButton(Frame)
        self.pushButtonGestioneAccountPrincipale.setGeometry(QtCore.QRect(160, 320, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonGestioneAccountPrincipale.setFont(font)
        self.pushButtonGestioneAccountPrincipale.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButtonGestioneAccountPrincipale.setStyleSheet("QPushButton{\n"
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
        self.pushButtonGestioneAccountPrincipale.setIcon(icon1)
        self.pushButtonGestioneAccountPrincipale.setObjectName("pushButton_5")
        self.pushButtonModifica.clicked.connect(self.clickModifica)
        self.pushButtonLogout.clicked.connect(self.openLogin)
        self.pushButtonGestioneAccountPrincipale.clicked.connect(self.openGestioneAccountPrincipale)

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Fumetteria - Modifica Password"))
        self.label.setText(_translate("Frame", "Inserisci nome utente:"))
        self.label_2.setText(_translate("Frame", "Inserisci password attuale:"))
        self.label_3.setText(_translate("Frame", "Inserisci la nuova password:"))
        self.label_4.setText(_translate("Frame", "MODIFICA PASSWORD"))
        self.pushButtonModifica.setText(_translate("Frame", "Modifica"))
        self.pushButtonLogout.setText(_translate("Frame", " Logout"))
        self.pushButtonGestioneAccountPrincipale.setText(_translate("Frame", " Indietro"))

    # Metodo che permette a un utente di modificare la
    # password dell'amministratore.
    # Una volta inserite le vecchie credenziali e la nuova
    # password, viene effettuato un controllo sulle vecchie credenziali.
    # Nel caso in cui le credenziale immesse fossero sbagliate,
    # si apre una finestra di errore.
    # Nel caso in cui invece le credenziali risultano corrette,
    # queste vengono salvate sul file "CredenzialiAmministratore.txt" e alla fine
    # si apre una nuova interfaccia grazie al metodo "self.openModificaEffettuata".
    def clickModifica(self):
        amministratore = Amministratore()

        nomeUtente = self.lineEditNomeUtente.text()
        passwordVecchia = self.lineEditPasswordVecchia.text()
        passwordNuova = self.lineEditPasswordNuova.text()

        controllo = False

        for char in passwordNuova:
            if char.isupper():
                controllo = True

        if amministratore.controlloCredenziali(nomeUtente, passwordVecchia):
            if len(passwordNuova) >= 8:
                if controllo is True:
                        amministratore.setPassword(passwordNuova)
                        self.openModificaEffettuata()
                else:
                    self.ErrorMaiuscola()
            else:
                self.ErrorLunghezza()
        else:
            self.ErrorMessageCambioPassword()

    # Metodo richiamato da "self.clickModifica" che serve ad aprire
    # l'interfaccia ModificaEffettuata.
    def openModificaEffettuata(self):
        self.modificaEffettuata = QtWidgets.QFrame()
        self.ui = ModificaEffetuata()
        self.ui.setupUi(self.modificaEffettuata)
        self.modificaEffettuata.show()
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

    # Metodo che permette di ritornare all'interfaccia GestioneAccountPrincipale.
    def openGestioneAccountPrincipale(self):
        from Grafica.GestioneAccount.GestioneAccountPrincipale import GestioneAccountPrincipale
        self.gestioneAccountPrincipale = QtWidgets.QFrame()
        self.ui = GestioneAccountPrincipale()
        self.ui.setupUi(self.gestioneAccountPrincipale)
        self.gestioneAccountPrincipale.show()
        self.frame.close()

    def ErrorMessageCambioPassword(self):
        self.ErrorBox = QMessageBox()
        self.ErrorBox.setWindowTitle("Errore")
        self.ErrorBox.setText("Nome utente o password errati")
        self.ErrorBox.setStyleSheet(
            "QLabel{min-width:200 px; font-size: 14px; font-family: Helvetica, Sans-Serif; } QPushButton:hover{"
            "background-color: #14626c;color:white; }QPushButton{ width:40px; height:20px; font-size: 10px; "
            "font-family: Helvetica, Sans-Serif; border: 1px solid black; border-radius: 5px; }")
        self.ErrorBox.exec()

    def ErrorLunghezza(self):
        self.ErrorBox = QMessageBox()
        self.ErrorBox.setWindowTitle("Errore")
        self.ErrorBox.setText("La password deve contenere almeno\n8 caratteri")
        self.ErrorBox.setStyleSheet(
            "QLabel{min-width:300 px; font-size: 14px; font-family: Helvetica, Sans-Serif; } QPushButton:hover{"
            "background-color: #14626c;color:white; }QPushButton{ width:40px; height:20px; font-size: 10px; "
            "font-family: Helvetica, Sans-Serif; border: 1px solid black; border-radius: 5px; }")
        self.ErrorBox.exec()

    def ErrorMaiuscola(self):
        self.ErrorBox = QMessageBox()
        self.ErrorBox.setWindowTitle("Errore")
        self.ErrorBox.setText("La password deve contenere almeno\nuna maiuscola.")
        self.ErrorBox.setStyleSheet(
            "QLabel{min-width:300 px; font-size: 14px; font-family: Helvetica, Sans-Serif; } QPushButton:hover{"
            "background-color: #14626c;color:white; }QPushButton{ width:40px; height:20px; font-size: 10px; "
            "font-family: Helvetica, Sans-Serif; border: 1px solid black; border-radius: 5px; }")
        self.ErrorBox.exec()

