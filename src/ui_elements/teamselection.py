# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\teamselection.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
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
        Teamselection.setStyleSheet("")
        Teamselection.setModal(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(Teamselection)
        self.verticalLayout.setObjectName("verticalLayout")
        self.LHeader = QtWidgets.QLabel(Teamselection)
        self.LHeader.setMinimumSize(QtCore.QSize(0, 100))
        self.LHeader.setMaximumSize(QtCore.QSize(16777215, 110))
        font = QtGui.QFont()
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)
        self.LHeader.setFont(font)
        self.LHeader.setAlignment(QtCore.Qt.AlignCenter)
        self.LHeader.setObjectName("LHeader")
        self.verticalLayout.addWidget(self.LHeader)
        self.person_label = QtWidgets.QLabel(Teamselection)
        self.person_label.setMinimumSize(QtCore.QSize(0, 40))
        self.person_label.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.person_label.setFont(font)
        self.person_label.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.person_label.setObjectName("person_label")
        self.verticalLayout.addWidget(self.person_label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.PBteamone = QtWidgets.QPushButton(Teamselection)
        self.PBteamone.setMinimumSize(QtCore.QSize(300, 300))
        self.PBteamone.setMaximumSize(QtCore.QSize(1000, 1000))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.PBteamone.setFont(font)
        self.PBteamone.setObjectName("PBteamone")
        self.horizontalLayout.addWidget(self.PBteamone)
        self.PBteamtwo = QtWidgets.QPushButton(Teamselection)
        self.PBteamtwo.setMinimumSize(QtCore.QSize(300, 300))
        self.PBteamtwo.setMaximumSize(QtCore.QSize(1000, 1000))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.PBteamtwo.setFont(font)
        self.PBteamtwo.setFlat(False)
        self.PBteamtwo.setObjectName("PBteamtwo")
        self.horizontalLayout.addWidget(self.PBteamtwo)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Teamselection)
        QtCore.QMetaObject.connectSlotsByName(Teamselection)

    def retranslateUi(self, Teamselection):
        _translate = QtCore.QCoreApplication.translate
        Teamselection.setWindowTitle(_translate("Teamselection", "~~ Teamwahl ~~"))
        self.LHeader.setText(_translate("Teamselection", "Team auswählen"))
        self.LHeader.setProperty("cssClass", _translate("Teamselection", "neutral bold"))
        self.person_label.setText(_translate("Teamselection", "Scanned Name"))
        self.PBteamone.setText(_translate("Teamselection", "Team #1"))
        self.PBteamone.setProperty("cssClass", _translate("Teamselection", "btn-teamone"))
        self.PBteamtwo.setText(_translate("Teamselection", "Team #2"))
        self.PBteamtwo.setProperty("cssClass", _translate("Teamselection", "btn-teamtwo"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Teamselection = QtWidgets.QDialog()
    ui = Ui_Teamselection()
    ui.setupUi(Teamselection)
    Teamselection.show()
    sys.exit(app.exec_())
