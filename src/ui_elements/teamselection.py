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
        self.person_label.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.person_label.setFont(font)
        self.person_label.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.person_label.setObjectName("person_label")
        self.verticalLayout.addWidget(self.person_label)
        self.scrollArea = QtWidgets.QScrollArea(Teamselection)
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setFrameShadow(QtWidgets.QFrame.Plain)
        self.scrollArea.setLineWidth(1)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 782, 309))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setContentsMargins(0, 0, 4, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.button_container = QtWidgets.QVBoxLayout()
        self.button_container.setObjectName("button_container")
        self.gridLayout.addLayout(self.button_container, 0, 0, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)

        self.retranslateUi(Teamselection)
        QtCore.QMetaObject.connectSlotsByName(Teamselection)

    def retranslateUi(self, Teamselection):
        _translate = QtCore.QCoreApplication.translate
        Teamselection.setWindowTitle(_translate("Teamselection", "~~ Select Team ~~"))
        self.LHeader.setText(_translate("Teamselection", "Team auswählen"))
        self.LHeader.setProperty("cssClass", _translate("Teamselection", "neutral bold"))
        self.person_label.setText(_translate("Teamselection", "Scanned Name"))
        self.person_label.setProperty("cssClass", _translate("Teamselection", "bold"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Teamselection = QtWidgets.QDialog()
    ui = Ui_Teamselection()
    ui.setupUi(Teamselection)
    Teamselection.show()
    sys.exit(app.exec_())
