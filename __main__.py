import sys

from PyQt5.QtWidgets import QApplication

from Grafica.GestioneLogin.LoginAmministratore import Ui_Login

if __name__ == "__main__":
    app = QApplication(sys.argv)
    login = Ui_Login()
    app.exec()
