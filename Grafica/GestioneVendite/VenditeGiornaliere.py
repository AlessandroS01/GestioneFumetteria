from PyQt5 import QtCore, QtGui, QtWidgets


class VenditeGiornaliere(object):

    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(872, 651)
        Frame.setStyleSheet("QFrame{\n"
                            "background-color: rgb(255, 255, 255);\n"
                            "}")
        Frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame = Frame
        self.label_4 = QtWidgets.QLabel(Frame)
        self.label_4.setGeometry(QtCore.QRect(10, 10, 851, 41))
        self.label_4.setStyleSheet("QLabel{\n"
                                   "font-family: impact, sans-serif;\n"
                                   "font-size:40px;\n"
                                   "\n"
                                   "}")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.line = QtWidgets.QFrame(Frame)
        self.line.setGeometry(QtCore.QRect(175, 50, 521, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_5 = QtWidgets.QLabel(Frame)
        self.label_5.setGeometry(QtCore.QRect(10, 70, 851, 71))
        self.label_5.setStyleSheet("QLabel{\n"
                                   "font-family: Helvetica, sans-serif;\n"
                                   "font-weight: 400;\n"
                                   "font-size: 18px\n"
                                   "}")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.pushButton_4 = QtWidgets.QPushButton(Frame)
        self.pushButton_4.setGeometry(QtCore.QRect(160, 610, 141, 31))
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
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:\\Users\\Lenovo\\Downloads\\../AppData/Downloads/left.png"), QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_8 = QtWidgets.QPushButton(Frame)
        self.pushButton_8.setGeometry(QtCore.QRect(10, 610, 141, 31))
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
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Images\\log.png"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.pushButton_8.setIcon(icon1)
        self.pushButton_8.setCheckable(False)
        self.pushButton_8.setObjectName("pushButton_8")
        self.tableWidget = QtWidgets.QTableWidget(Frame)
        self.tableWidget.setGeometry(QtCore.QRect(130, 150, 601, 401))
        self.tableWidget.setStyleSheet("\n"
                                       "QHeaderView::section {\n"
                                       "background-color: #14626c;\n"
                                       "color:white;\n"
                                       "font-weight:bold;\n"
                                       "\n"
                                       "}\n"
                                       "\n"
                                       "QTableWidget {\n"
                                       "gridline-color: black;\n"
                                       "font-size: 14px;\n"
                                       "font-family:Helvetica,sans-serif;\n"
                                       "border: 2px solid black;\n"
                                       "border-radius:6px;\n"
                                       "}\n"
                                       "")
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget.verticalHeader().setVisible(False)
        self.pushButtonIncasso = QtWidgets.QPushButton(Frame)
        self.pushButtonIncasso.setGeometry(QtCore.QRect(590, 560, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonIncasso.setFont(font)
        self.pushButtonIncasso.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButtonIncasso.setStyleSheet("QPushButton{\n"
                                             "border: 2px solid black;\n"
                                             "border-radius: 10px;\n"
                                             "}\n"
                                             "QPushButton:hover{\n"
                                             "\n"
                                             "background-color: #14626c;\n"
                                             "color:white;\n"
                                             "}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Images\\wallet.png"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.pushButtonIncasso.setIcon(icon1)
        self.pushButtonIncasso.setObjectName("pushButton_5")

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Fumetteria - Gestione Magazzino"))
        self.label_4.setText(_translate("Frame", "VISUALIZZA VENDITE"))
        self.label_5.setText(_translate("Frame",
                                        "Di seguito sono riportate le informazioni relative alle vendite avvenute "
                                        "durante la giornata immessa.\n "
                                        "Per tornare indietro o effettuare il logout utilizzare i pulsanti in basso a "
                                        "sinistra. "))
        self.pushButton_4.setText(_translate("Frame", " Indietro"))
        self.pushButton_8.setText(_translate("Frame", " Logout"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Frame", "Nome"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Frame", "Quantita Acquistate"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Frame", "Prezzo Vendita"))
        self.pushButtonIncasso.setText(_translate("Frame", "Incasso"))
