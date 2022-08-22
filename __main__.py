import sys
from pathlib import Path

from PyQt5 import QtWidgets

from Amministratore.Amministratore import Amministratore
from GestioneMagazzino.Magazzino import Magazzino
from Grafica.GestioneLogin.LoginAmministratore import LoginAmministratore

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Frame = QtWidgets.QFrame()
    ui = LoginAmministratore()
    ui.setupUi(Frame)
    Frame.show()
    sys.exit(app.exec_())