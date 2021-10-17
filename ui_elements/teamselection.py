# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\teamselection.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Teamselection(object):
    def setupUi(self, Teamselection):
        Teamselection.setObjectName("Teamselection")
        Teamselection.resize(800, 480)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Teamselection.sizePolicy().hasHeightForWidth())
        Teamselection.setSizePolicy(sizePolicy)
        Teamselection.setMinimumSize(QtCore.QSize(800, 480))
        Teamselection.setMaximumSize(QtCore.QSize(800, 480))
        Teamselection.setStyleSheet("QWidget {\n"
"    color: rgb(0, 123, 255);    \n"
"    background-color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    border-width: 1px;\n"
"    border-style: solid;\n"
"    border-radius: 40;\n"
"    padding: 3px;\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"}\n"
"\n"
"#PBteamone {\n"
"    background-color: rgb(235, 64, 52);\n"
"    border-color: rgb(235, 64, 52);\n"
"}\n"
"\n"
"#PBteamtwo {\n"
"    background-color: rgb(52, 76, 235);\n"
"    border-color: rgb(52, 76, 235);\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    color: rgb(255, 255, 255);    \n"
"    background-color: rgb(52, 235, 143);\n"
"}\n"
"\n"
"\n"
"")
        Teamselection.setModal(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(Teamselection)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Lheader = QtWidgets.QLabel(Teamselection)
        self.Lheader.setMinimumSize(QtCore.QSize(0, 100))
        self.Lheader.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)
        self.Lheader.setFont(font)
        self.Lheader.setAlignment(QtCore.Qt.AlignCenter)
        self.Lheader.setObjectName("Lheader")
        self.verticalLayout.addWidget(self.Lheader)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.PBteamone = QtWidgets.QPushButton(Teamselection)
        self.PBteamone.setMinimumSize(QtCore.QSize(300, 350))
        self.PBteamone.setMaximumSize(QtCore.QSize(450, 16777215))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.PBteamone.setFont(font)
        self.PBteamone.setObjectName("PBteamone")
        self.horizontalLayout.addWidget(self.PBteamone)
        self.PBteamtwo = QtWidgets.QPushButton(Teamselection)
        self.PBteamtwo.setMinimumSize(QtCore.QSize(300, 350))
        self.PBteamtwo.setMaximumSize(QtCore.QSize(450, 16777215))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.PBteamtwo.setFont(font)
        self.PBteamtwo.setObjectName("PBteamtwo")
        self.horizontalLayout.addWidget(self.PBteamtwo)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Teamselection)
        QtCore.QMetaObject.connectSlotsByName(Teamselection)

    def retranslateUi(self, Teamselection):
        _translate = QtCore.QCoreApplication.translate
        Teamselection.setWindowTitle(_translate("Teamselection", "~~ Teamwahl ~~"))
        self.Lheader.setText(_translate("Teamselection", "Team auswählen"))
        self.PBteamone.setText(_translate("Teamselection", "Team #1"))
        self.PBteamtwo.setText(_translate("Teamselection", "Team #2"))
