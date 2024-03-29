from PyQt5 import QtCore, QtGui, QtWidgets


class ModificaEffetuata(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(390, 201)
        Frame.setStyleSheet("QFrame{\n"
                            "background-color: rgb(255, 255, 255);\n"
                            "}")
        Frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame = Frame
        self.label_4 = QtWidgets.QLabel(Frame)
        self.label_4.setGeometry(QtCore.QRect(10, 20, 381, 31))
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
        self.pushButtonHome = QtWidgets.QPushButton(Frame)
        self.pushButtonHome.setGeometry(QtCore.QRect(120, 150, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonHome.setFont(font)
        self.pushButtonHome.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButtonHome.setStyleSheet("QPushButton{\n"
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
        self.pushButtonHome.setIcon(icon)
        self.pushButtonHome.setCheckable(False)
        self.pushButtonHome.setObjectName("pushButton_7")
        self.label_5 = QtWidgets.QLabel(Frame)
        self.label_5.setGeometry(QtCore.QRect(0, 60, 391, 61))
        self.label_5.setStyleSheet("QLabel{\n"
                                   "font-family: Helvetica, sans-serif;\n"
                                   "font-weight: 400;\n"
                                   "font-size: 15px\n"
                                   "}")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.pushButtonHome.clicked.connect(self.openVistaHome)

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Fumetteria - Modifica Effettuata"))
        self.label_4.setText(_translate("Frame", "CREDENZIALI MODIFICATE"))
        self.pushButtonHome.setText(_translate("Frame", "Home"))
        self.label_5.setText(_translate("Frame", "Le credenziali sono state modificate con successo.\n"
                                                 " Cliccare su Home per continuare ad utilizzare il programma "))

    # Metodo che permette di ritornare all'interfaccia VistaHome.
    def openVistaHome(self):
        from Grafica.GestioneGeneraleProgramma.VistaHome import VistaHome
        self.home = QtWidgets.QFrame()
        self.ui = VistaHome()
        self.ui.setupUi(self.home)
        self.home.show()
        self.frame.close()
