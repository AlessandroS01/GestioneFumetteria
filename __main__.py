import sys

from PyQt5 import QtWidgets

from Grafica.GestioneLogin.LoginAmministratore import LoginAmministratore

if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    Frame = QtWidgets.QFrame()
    ui = LoginAmministratore()
    ui.setupUi(Frame)
    Frame.show()
    sys.exit(app.exec_())



