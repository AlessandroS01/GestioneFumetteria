from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

from Amministratore.Amministratore import Amministratore
from Grafica.GestioneGeneraleProgramma.VistaHome import VistaHome


class LoginAmministratore(object):

    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(484, 333)
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        Frame.setFont(font)
        Frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame = Frame
        self.lineEditNomeUtente = QtWidgets.QLineEdit(Frame)
        self.lineEditNomeUtente.setGeometry(QtCore.QRect(20, 150, 451, 31))
        self.lineEditNomeUtente.setStyleSheet("border: 1px solid black;\n"
                                    "border-radius: 10px;")
        self.lineEditNomeUtente.setObjectName("lineEdit")
        self.lineEditPassword = QtWidgets.QLineEdit(Frame)
        self.lineEditPassword.setGeometry(QtCore.QRect(20, 220, 451, 31))
        self.lineEditPassword.setStyleSheet("border: 1px solid black;\n"
                                      "border-radius: 10px;")
        self.lineEditPassword.setObjectName("lineEdit_2")
        self.label = QtWidgets.QLabel(Frame)
        self.label.setGeometry(QtCore.QRect(20, 120, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Frame)
        self.label_2.setGeometry(QtCore.QRect(20, 190, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Frame)
        self.label_3.setGeometry(QtCore.QRect(180, 10, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.line = QtWidgets.QFrame(Frame)
        self.line.setGeometry(QtCore.QRect(40, 50, 391, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_4 = QtWidgets.QLabel(Frame)
        self.label_4.setGeometry(QtCore.QRect(27, 70, 428, 31))
        self.label_4.setStyleSheet("border: 1px solid black;\n"
                                   "border-radius:10px;")
        self.label_4.setObjectName("label_4")
        self.pushButtonLogin = QtWidgets.QPushButton(Frame)
        self.pushButtonLogin.setGeometry(QtCore.QRect(20, 270, 451, 41))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonLogin.setFont(font)
        self.pushButtonLogin.setStyleSheet(
            "QPushButton{border: 2px solid black; border-radius: 10px;}QPushButton:hover{background-color: "
            "#14626c;color:white;}")
        self.pushButtonLogin.setObjectName("pushButton")
        self.pushButtonLogin.clicked.connect(self.clickLogin)
        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Fumetteria"))
        self.label.setText(_translate("Frame", "USERNAME:"))
        self.label_2.setText(_translate("Frame", "PASSWORD:"))
        self.label_3.setText(_translate("Frame", "FUMETTERIA"))
        self.label_4.setText(
            _translate("Frame",
                       "Inserisci le credenziali per effettuare e iniziare ad utilizzare il programma"))
        self.pushButtonLogin.setText(_translate("Frame", "Login"))

    # Metodo che permette a un utente di entrare all'interno
    # del software tramite le credenziali di accesso salvate dentro al
    # file "CredenzialiAmministratore.txt".
    # Solo a seguito di un controllo delle credenziali, effettuato tramite
    # il metodo ".controlloCredenziali" istanziato all'interno di Amministratore
    # è possibile l'accesso al servizio.
    # Nel caso in cui le credenziali inserite risultano sbagliate viene
    # aperta una finestra di errore.
    # Nel caso in cui invece le credenziali risultano corrette,
    # viene aperta la successiva interfaccia tramite al metodo "self.openHome".
    def clickLogin(self):
        amministratore = Amministratore()

        nomeUtente = self.lineEditNomeUtente.text()
        password = self.lineEditPassword.text()

        if amministratore.controlloCredenziali(nomeUtente, password):
            self.openHome()

        else:
            self.ErrorLogin()

    # Metodo richiamato da "self.clickLogin" che serve ad aprire
    # l'interfaccia VistaHome.
    # Il "self.frame.close()" permette a LoginAmministratore di
    # chiudersi non appena compare l'interfaccia successiva.
    def openHome(self):
        self.home = QtWidgets.QFrame()
        self.ui = VistaHome()
        self.ui.setupUi(self.home)
        self.home.show()
        self.frame.close()

    def ErrorLogin(self):
        self.ErrorBox = QMessageBox()
        self.ErrorBox.setWindowTitle("Errore")
        self.ErrorBox.setText("Nome utente o password errati")
        self.ErrorBox.setStyleSheet(
            "QLabel{min-width:200 px; font-size: 14px; font-family: Helvetica, Sans-Serif; } QPushButton:hover{"
            "background-color: #14626c;color:white; }QPushButton{ width:40px; height:20px; font-size: 10px; "
            "font-family: Helvetica, Sans-Serif; border: 1px solid black; border-radius: 5px; }")
        self.ErrorBox.exec()

