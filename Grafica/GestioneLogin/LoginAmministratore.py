# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Lenovo\Desktop\University\MATERIE\2°ANNO 2° SEMESTRE\INGEGNERIA DEL SOFTWARE\Mockup\LoginAmministratore.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


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
        self.lineEdit = QtWidgets.QLineEdit(Frame)
        self.lineEdit.setGeometry(QtCore.QRect(20, 150, 451, 31))
        self.lineEdit.setStyleSheet("border: 1px solid black;\n"
"border-radius: 10px;")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(20, 220, 451, 31))
        self.lineEdit_2.setStyleSheet("border: 1px solid black;\n"
"border-radius: 10px;")
        self.lineEdit_2.setObjectName("lineEdit_2")
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
        self.label_4.setGeometry(QtCore.QRect(50, 70, 371, 31))
        self.label_4.setStyleSheet("border: 1px solid black;\n"
"border-radius:10px;")
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(Frame)
        self.pushButton.setGeometry(QtCore.QRect(20, 270, 451, 41))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("border: 2px solid black;\n"
"border-radius: 10px;\n"
"")
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Fumetteria"))
        self.label.setText(_translate("Frame", "USERNAME:"))
        self.label_2.setText(_translate("Frame", "PASSWORD:"))
        self.label_3.setText(_translate("Frame", "FUMETTERIA"))
        self.label_4.setText(_translate("Frame", "Iserisci le credenziali per effettuare il login e inizare a utilizzare il programma"))
        self.pushButton.setText(_translate("Frame", "Login"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Frame = QtWidgets.QFrame()
    ui = LoginAmministratore()
    ui.setupUi(Frame)
    Frame.show()
    sys.exit(app.exec_())
