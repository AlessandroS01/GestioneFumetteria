from PyQt5 import QtCore, QtGui, QtWidgets

from Grafica.GestioneAccount.ModificaPassword import ModificaPassword
from Grafica.GestioneAccount.ModificaUtente import ModificaUtente


class GestioneAccountPrincipale(object):

    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(414, 362)
        Frame.setStyleSheet("QFrame{\n"
                            "background-color: rgb(255, 255, 255);\n"
                            "}")
        self.frame = Frame
        self.label_2 = QtWidgets.QLabel(Frame)
        self.label_2.setGeometry(QtCore.QRect(70, 20, 261, 31))
        self.label_2.setStyleSheet("QLabel{\n"
                                   "font-family: impact, sans-serif;\n"
                                   "font-size:30px;\n"
                                   "\n"
                                   "}")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.line = QtWidgets.QFrame(Frame)
        self.line.setGeometry(QtCore.QRect(40, 50, 321, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.pushButtonModificaUtente = QtWidgets.QPushButton(Frame)
        self.pushButtonModificaUtente.setGeometry(QtCore.QRect(30, 150, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonModificaUtente.setFont(font)
        self.pushButtonModificaUtente.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButtonModificaUtente.setStyleSheet("QPushButton{\n"
                                                    "border: 2px solid black;\n"
                                                    "border-radius: 10px;\n"
                                                    "}\n"
                                                    "QPushButton:hover{\n"
                                                    "\n"
                                                    "background-color: #14626c;\n"
                                                    "color:white;\n"
                                                    "}")
        self.pushButtonModificaUtente.setObjectName("pushButton_2")
        self.pushButtonModificaPassword = QtWidgets.QPushButton(Frame)
        self.pushButtonModificaPassword.setGeometry(QtCore.QRect(230, 150, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonModificaPassword.setFont(font)
        self.pushButtonModificaPassword.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButtonModificaPassword.setStyleSheet("QPushButton{\n"
                                                      "border: 2px solid black;\n"
                                                      "border-radius: 10px;\n"
                                                      "}\n"
                                                      "QPushButton:hover{\n"
                                                      "\n"
                                                      "background-color: #14626c;\n"
                                                      "color:white;\n"
                                                      "}")
        self.pushButtonModificaPassword.setObjectName("pushButton_3")
        self.label = QtWidgets.QLabel(Frame)
        self.label.setGeometry(QtCore.QRect(20, 70, 371, 41))
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setStyleSheet("QLabel{\n"
                                 "font-family: Helvetica, sans-serif;\n"
                                 "font-weight: 400;\n"
                                 "font-size: 16px\n"
                                 "}")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButtonVistaHome = QtWidgets.QPushButton(Frame)
        self.pushButtonVistaHome.setGeometry(QtCore.QRect(120, 220, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonVistaHome.setFont(font)
        self.pushButtonVistaHome.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButtonVistaHome.setStyleSheet("QPushButton{\n"
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
            "Images\\home.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonVistaHome.setIcon(icon)
        self.pushButtonVistaHome.setObjectName("pushButton_4")
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
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(
            "Images\\log.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonLogout.setIcon(icon1)
        self.pushButtonLogout.setCheckable(False)
        self.pushButtonLogout.setObjectName("pushButton_5")
        self.pushButtonModificaUtente.clicked.connect(self.openModificaUtente)
        self.pushButtonModificaPassword.clicked.connect(self.openModificaPassword)
        self.pushButtonLogout.clicked.connect(self.openLogin)
        self.pushButtonVistaHome.clicked.connect(self.openVistaHome)

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Fumetteria - Gestione Account"))
        self.label_2.setText(_translate("Frame", "GESTIONE ACCOUNT"))
        self.pushButtonModificaUtente.setText(_translate("Frame", "Modifica \n"
                                                                  " Nome Utente"))
        self.pushButtonModificaPassword.setText(_translate("Frame", "Modifica \n"
                                                                    " Password"))
        self.label.setText(_translate("Frame", "Scegli una delle due opzioni disponibili o clicca \n"
                                               "il tasto home per tornare alla Home"))
        self.pushButtonVistaHome.setText(_translate("Frame", " Home"))
        self.pushButtonLogout.setText(_translate("Frame", " Logout"))

    # Metodo che permette di aprire l'interfaccia sulla quale si
    # può modificare il nome utente dell'amministratore.
    # L'interfaccia è : ModificaUtente
    def openModificaUtente(self):
        self.modificaUtente = QtWidgets.QFrame()
        self.ui = ModificaUtente()
        self.ui.setupUi(self.modificaUtente)
        self.modificaUtente.show()
        self.frame.close()

    # Metodo che permette di aprire l'interfaccia sulla quale si
    # può modificare la password dell'amministratore.
    # L'interfaccia è : ModificaPassword
    def openModificaPassword(self):
        self.modificaPassword = QtWidgets.QFrame()
        self.ui = ModificaPassword()
        self.ui.setupUi(self.modificaPassword)
        self.modificaPassword.show()
        self.frame.close()

    # Metodo che permette di ritornare all'interfaccia VistaHome.
    def openVistaHome(self):
        from Grafica.GestioneGeneraleProgramma.VistaHome import VistaHome
        self.home = QtWidgets.QFrame()
        self.ui = VistaHome()
        self.ui.setupUi(self.home)
        self.home.show()
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
