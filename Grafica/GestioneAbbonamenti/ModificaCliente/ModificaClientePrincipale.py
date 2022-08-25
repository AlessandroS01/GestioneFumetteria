from PyQt5 import QtCore, QtGui, QtWidgets


class ModificaClientePrincipale(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(448, 309)
        Frame.setStyleSheet("QFrame{\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        Frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_4 = QtWidgets.QLabel(Frame)
        self.label_4.setGeometry(QtCore.QRect(10, 20, 431, 31))
        self.label_4.setStyleSheet("QLabel{\n"
"font-family: impact, sans-serif;\n"
"font-size:30px;\n"
"\n"
"}")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.line = QtWidgets.QFrame(Frame)
        self.line.setGeometry(QtCore.QRect(50, 50, 321, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.pushButton_5 = QtWidgets.QPushButton(Frame)
        self.pushButton_5.setGeometry(QtCore.QRect(10, 270, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_5.setStyleSheet("QPushButton{\n"
"border: 2px solid black;\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton:hover{\n"
"\n"
"background-color: #14626c;\n"
"color:white;\n"
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:\\Users\\dsant\\Desktop\\Mockup\\log.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_5.setIcon(icon)
        self.pushButton_5.setCheckable(False)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_4 = QtWidgets.QPushButton(Frame)
        self.pushButton_4.setGeometry(QtCore.QRect(160, 270, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_4.setStyleSheet("QPushButton{\n"
"border: 2px solid black;\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton:hover{\n"
"\n"
"background-color: #14626c;\n"
"color:white;\n"
"}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:\\Users\\dsant\\Desktop\\Mockup\\left.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon1)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_8 = QtWidgets.QPushButton(Frame)
        self.pushButton_8.setGeometry(QtCore.QRect(20, 120, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_8.setStyleSheet("QPushButton{\n"
"border: 2px solid black;\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton:hover{\n"
"\n"
"background-color: #14626c;\n"
"color:white;\n"
"}")
        self.pushButton_8.setCheckable(False)
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(Frame)
        self.pushButton_9.setGeometry(QtCore.QRect(20, 180, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_9.setStyleSheet("QPushButton{\n"
"border: 2px solid black;\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton:hover{\n"
"\n"
"background-color: #14626c;\n"
"color:white;\n"
"}")
        self.pushButton_9.setCheckable(False)
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_12 = QtWidgets.QPushButton(Frame)
        self.pushButton_12.setGeometry(QtCore.QRect(230, 120, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_12.setStyleSheet("QPushButton{\n"
"border: 2px solid black;\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton:hover{\n"
"\n"
"background-color: #14626c;\n"
"color:white;\n"
"}")
        self.pushButton_12.setCheckable(False)
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_13 = QtWidgets.QPushButton(Frame)
        self.pushButton_13.setGeometry(QtCore.QRect(230, 180, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_13.setFont(font)
        self.pushButton_13.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_13.setStyleSheet("QPushButton{\n"
"border: 2px solid black;\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton:hover{\n"
"\n"
"background-color: #14626c;\n"
"color:white;\n"
"}")
        self.pushButton_13.setCheckable(False)
        self.pushButton_13.setObjectName("pushButton_13")
        self.label = QtWidgets.QLabel(Frame)
        self.label.setGeometry(QtCore.QRect(10, 60, 431, 41))
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setStyleSheet("QLabel{\n"
"font-family: Helvetica, sans-serif;\n"
"font-weight: 400;\n"
"font-size: 16px\n"
"}")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Fumetteria - Modifica Cliente"))
        self.label_4.setText(_translate("Frame", "MODIFICA CLIENTE"))
        self.pushButton_5.setText(_translate("Frame", " Logout"))
        self.pushButton_4.setText(_translate("Frame", " Indietro"))
        self.pushButton_8.setText(_translate("Frame", "Modifica Nome/\n"
                                            "Cognome Cliente"))
        self.pushButton_9.setText(_translate("Frame", "Modifica\n"
                                            "Email"))
        self.pushButton_12.setText(_translate("Frame", "Modifica \n"
                                            "Codice Fiscale"))
        self.pushButton_13.setText(_translate("Frame", "Modifica \n"
                                                " Telefono"))
        self.label.setText(_translate("Frame", "Seleziona una delle opzioni per modificare il le informazioni\n"
                                    "relative al cliente"))