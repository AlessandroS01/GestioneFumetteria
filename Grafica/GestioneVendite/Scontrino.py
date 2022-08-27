from datetime import datetime

from PyQt5 import QtCore, QtGui, QtWidgets


class Scontrino(object):

    def setupUi(self, Frame, acquisti, frameDaAprire):
        self.frameDaAprire = frameDaAprire
        self.acquisti = acquisti
        Frame.setObjectName("Frame")
        Frame.resize(398, 571)
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
        self.pushButton_5 = QtWidgets.QPushButton(Frame)
        self.pushButton_5.setGeometry(QtCore.QRect(10, 530, 141, 31))
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
        icon.addPixmap(QtGui.QPixmap("Images\\log.png"), QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        self.pushButton_5.setIcon(icon)
        self.pushButton_5.setCheckable(False)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(Frame)
        self.pushButton_6.setGeometry(QtCore.QRect(20, 440, 361, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_6.setStyleSheet("QPushButton{\n"
                                        "border: 2px solid black;\n"
                                        "border-radius: 10px;\n"
                                        "}\n"
                                        "QPushButton:hover{\n"
                                        "\n"
                                        "background-color: #14626c;\n"
                                        "color:white;\n"
                                        "}")
        self.pushButton_6.setCheckable(False)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButtonAggiungiAcquisto = QtWidgets.QPushButton(Frame)
        self.pushButtonAggiungiAcquisto.setGeometry(QtCore.QRect(20, 480, 361, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonAggiungiAcquisto.setFont(font)
        self.pushButtonAggiungiAcquisto.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButtonAggiungiAcquisto.setStyleSheet("QPushButton{\n"
                                                      "border: 2px solid black;\n"
                                                      "border-radius: 10px;\n"
                                                      "}\n"
                                                      "QPushButton:hover{\n"
                                                      "\n"
                                                      "background-color: #14626c;\n"
                                                      "color:white;\n"
                                                      "}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Images\\left.png"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.pushButtonAggiungiAcquisto.setIcon(icon1)
        self.pushButtonAggiungiAcquisto.setObjectName("pushButton_4")
        self.label = QtWidgets.QLabel(Frame)
        self.label.setGeometry(QtCore.QRect(10, 60, 391, 61))
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setStyleSheet("QLabel{\n"
                                 "font-family: Helvetica, sans-serif;\n"
                                 "font-weight: 400;\n"
                                 "font-size: 16px\n"
                                 "}")
        self.label.setText("")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.listWidget = QtWidgets.QListWidget(Frame)
        self.listWidget.setGeometry(QtCore.QRect(20, 80, 361, 341))
        self.listWidget.setStyleSheet("QScrollBar:vertical {\n"
                                      "            border: 0px solid #999999;\n"
                                      "            background:transparent;\n"
                                      "            width:10px;    \n"
                                      "            margin: 0px 0px 0px 0px;\n"
                                      "        }\n"
                                      "        QScrollBar::handle:vertical {         \n"
                                      "       \n"
                                      "            min-height: 0px;\n"
                                      "              border: 0px solid red;\n"
                                      "            border-radius: 4px;\n"
                                      "            background-color: #14626c;\n"
                                      "        }\n"
                                      "        QScrollBar::add-line:vertical {       \n"
                                      "            height: 0px;\n"
                                      "            subcontrol-position: bottom;\n"
                                      "            subcontrol-origin: margin;\n"
                                      "        }\n"
                                      "        QScrollBar::sub-line:vertical {\n"
                                      "            height: 0 px;\n"
                                      "            subcontrol-position: top;\n"
                                      "            subcontrol-origin: margin;\n"
                                      "        }\n"
                                      "\n"
                                      "QListView{\n"
                                      "border-radius:8px;\n"
                                      "border:2px solid black;\n"
                                      "} \n"
                                      "\n"
                                      "\n"
                                      "QListView::item:selected\n"
                                      "{\n"
                                      "border : 0px;\n"
                                      "background : transparent;\n"
                                      "}\n"
                                      "\n"
                                      " QListView::item::hover\n"
                                      "{\n"
                                      "background : transparent;\n"
                                      "}")
        self.listWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.listWidget.setDefaultDropAction(QtCore.Qt.IgnoreAction)
        self.listWidget.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.listWidget.setObjectName("listWidget")

        for index in range(len(self.acquisti) + 3):
            item = QtWidgets.QListWidgetItem()
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setItalic(False)
            font.setUnderline(False)
            item.setFont(font)
            self.listWidget.addItem(item)

        self.pushButtonAggiungiAcquisto.clicked.connect(self.openModificaAcquisto)

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Fumetteria - Scontrino"))
        self.label_4.setText(_translate("Frame", "SCONTRINO"))
        self.pushButton_5.setText(_translate("Frame", " Logout"))
        self.pushButton_6.setText(_translate("Frame", "Registrazione Scontrino"))
        self.pushButtonAggiungiAcquisto.setText(_translate("Frame", " Modifica Scontrino"))

        item = self.listWidget.item(0)
        data = str(datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
        item.setText(_translate("Frame", "Data : " + data))

        for index in range(len(self.acquisti)):
            acquisto = self.acquisti[index]
            item = self.listWidget.item(index + 1)
            stringa = str(str(acquisto.getQuantitaAcquistate()) + "  " + acquisto.getAcquisto().getNomeProdotto() +
                          "  " + str(acquisto.getAcquisto().getPrezzo()) + "€")
            item.setText(_translate("Frame", stringa))

        item = self.listWidget.item(len(self.acquisti) + 1)
        item.setText(_translate("Frame", "------------------------------"))

        item = self.listWidget.item(len(self.acquisti) + 2)
        self.prezzoTotale = 0
        for index in range(len(self.acquisti)):
            self.prezzoTotale += float(float(self.acquisti[index].getQuantitaAcquistate())
                                       * float(self.acquisti[index].getAcquisto().getPrezzo()))
        item.setText(_translate("Frame", str("Spesa totale : " + str(self.prezzoTotale) + "€")))

    # Metodo che permette di aprire l'interfaccia per modificare
    # lo scontrino.
    def openModificaAcquisto(self):
        self.frameDaAprire.show()
        self.frame.close()
