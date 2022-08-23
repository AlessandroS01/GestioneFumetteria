from PyQt5 import QtCore, QtGui, QtWidgets

from Grafica.GestioneAccount.GestioneAccountPrincipale import GestioneAccountPrincipale
from Grafica.GestioneMagazzino.GestioneMagazzinoPrincipale import GestioneMagazzinoPrincipale


class VistaHome(object):

    def setupUi(self, Frame):
        Frame.setObjectName("frame")
        Frame.resize(413, 364)
        Frame.setStyleSheet("QFrame{\n"
                            "background-color: rgb(255, 255, 255);\n"
                            "}")
        self.pushButtonGestioneMagazzino = QtWidgets.QPushButton(Frame)
        self.frame = Frame
        self.pushButtonGestioneMagazzino.setGeometry(QtCore.QRect(30, 140, 161, 51))
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
        self.pushButtonGestioneMagazzino.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Frame)
        self.pushButton_2.setGeometry(QtCore.QRect(220, 140, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_2.setStyleSheet("QPushButton{\n"
                                        "border: 2px solid black;\n"
                                        "border-radius: 10px;\n"
                                        "}\n"
                                        "QPushButton:hover{\n"
                                        "\n"
                                        "background-color: #14626c;\n"
                                        "color:white;\n"
                                        "}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Frame)
        self.pushButton_3.setGeometry(QtCore.QRect(30, 220, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_3.setStyleSheet("QPushButton{\n"
                                        "border: 2px solid black;\n"
                                        "border-radius: 10px;\n"
                                        "}\n"
                                        "QPushButton:hover{\n"
                                        "\n"
                                        "background-color: #14626c;\n"
                                        "color:white;\n"
                                        "}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButtonGestioneAccount = QtWidgets.QPushButton(Frame)
        self.pushButtonGestioneAccount.setGeometry(QtCore.QRect(220, 220, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonGestioneAccount.setFont(font)
        self.pushButtonGestioneAccount.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButtonGestioneAccount.setStyleSheet("QPushButton{\n"
                                                     "border: 2px solid black;\n"
                                                     "border-radius: 10px;\n"
                                                     "}\n"
                                                     "QPushButton:hover{\n"
                                                     "\n"
                                                     "background-color: #14626c;\n"
                                                     "color:white;\n"
                                                     "}")
        self.pushButtonGestioneAccount.setObjectName("pushButton_4")
        self.label = QtWidgets.QLabel(Frame)
        self.label.setGeometry(QtCore.QRect(20, 70, 381, 41))
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setStyleSheet("QLabel{\n"
                                 "font-family: Helvetica, sans-serif;\n"
                                 "font-weight: 400;\n"
                                 "font-size: 16px\n"
                                 "}")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Frame)
        self.label_2.setGeometry(QtCore.QRect(160, 10, 71, 31))
        self.label_2.setStyleSheet("QLabel{\n"
                                   "font-family: impact, sans-serif;\n"
                                   "font-size:30px;\n"
                                   "\n"
                                   "}")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.line = QtWidgets.QFrame(Frame)
        self.line.setGeometry(QtCore.QRect(80, 40, 221, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.pushButtonLogout = QtWidgets.QPushButton(Frame)
        self.pushButtonLogout.setGeometry(QtCore.QRect(120, 300, 161, 41))
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
        self.pushButtonLogout.clicked.connect(self.openLogin)
        self.pushButtonGestioneAccount.clicked.connect(self.openGestioneAccount)
        self.pushButtonGestioneMagazzino.clicked.connect(self.openGestioneMagazzino)

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, frame):
        _translate = QtCore.QCoreApplication.translate
        frame.setWindowTitle(_translate("frame", "Fumetteria - Home"))
        self.pushButtonGestioneMagazzino.setText(_translate("frame", "Gestione\n"
                                                                     "  Magazzino"))
        self.pushButton_2.setText(_translate("frame", "Gestione \n"
                                                      " Abbonamenti"))
        self.pushButton_3.setText(_translate("frame", "Gestione \n"
                                                      " Vendite"))
        self.pushButtonGestioneAccount.setText(_translate("frame", "Gestione \n"
                                                                   " Account"))
        self.label.setText(_translate("frame", "Naviga tra le varie sezioni utilizzando il menu in basso\n"
                                               "e scegli l\'attività che vuoi eseguirei"))
        self.label_2.setText(_translate("frame", "HOME"))
        self.pushButtonLogout.setText(_translate("frame", " Logout"))

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
    # possono gestire le informazioni dell'amministratore.
    # L'interfaccia è : GestioneAccountPrincipale
    def openGestioneAccount(self):
        self.gestioneAccount = QtWidgets.QFrame()
        self.ui = GestioneAccountPrincipale()
        self.ui.setupUi(self.gestioneAccount)
        self.gestioneAccount.show()
        self.frame.close()

    # Metodo che permette di aprire l'interfaccia sulla quale si
    # può gestire interamente il magazzino.
    # L'interfaccia è : GestioneMagazzinoPrincipale
    def openGestioneMagazzino(self):
        self.gestioneMagazzino = QtWidgets.QFrame()
        self.ui = GestioneMagazzinoPrincipale()
        self.ui.setupUi(self.gestioneMagazzino)
        self.gestioneMagazzino.show()
        self.frame.close()
