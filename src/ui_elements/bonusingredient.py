# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\bonusingredient.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_addingredient(object):
    def setupUi(self, addingredient):
        addingredient.setObjectName("addingredient")
        addingredient.resize(400, 400)
        addingredient.setMinimumSize(QtCore.QSize(400, 400))
        addingredient.setMaximumSize(QtCore.QSize(2000, 1200))
        addingredient.setStyleSheet("")
        addingredient.setModal(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(addingredient)
        self.verticalLayout.setObjectName("verticalLayout")
        self.LHeader = QtWidgets.QLabel(addingredient)
        self.LHeader.setMaximumSize(QtCore.QSize(16777215, 80))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.LHeader.setFont(font)
        self.LHeader.setAlignment(QtCore.Qt.AlignCenter)
        self.LHeader.setObjectName("LHeader")
        self.verticalLayout.addWidget(self.LHeader)
        self.CBingredient = QtWidgets.QComboBox(addingredient)
        self.CBingredient.setMinimumSize(QtCore.QSize(103, 29))
        self.CBingredient.setMaximumSize(QtCore.QSize(20000, 120))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.CBingredient.setFont(font)
        self.CBingredient.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.CBingredient.setMaxVisibleItems(10)
        self.CBingredient.setObjectName("CBingredient")
        self.verticalLayout.addWidget(self.CBingredient)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.PBminus = QtWidgets.QPushButton(addingredient)
        self.PBminus.setMinimumSize(QtCore.QSize(60, 18))
        self.PBminus.setMaximumSize(QtCore.QSize(1000, 1000))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.PBminus.setFont(font)
        self.PBminus.setObjectName("PBminus")
        self.horizontalLayout.addWidget(self.PBminus)
        self.LAmount = QtWidgets.QLabel(addingredient)
        self.LAmount.setMinimumSize(QtCore.QSize(150, 0))
        self.LAmount.setMaximumSize(QtCore.QSize(175, 1000))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.LAmount.setFont(font)
        self.LAmount.setLineWidth(1)
        self.LAmount.setAlignment(QtCore.Qt.AlignCenter)
        self.LAmount.setObjectName("LAmount")
        self.horizontalLayout.addWidget(self.LAmount)
        self.PBplus = QtWidgets.QPushButton(addingredient)
        self.PBplus.setMinimumSize(QtCore.QSize(60, 18))
        self.PBplus.setMaximumSize(QtCore.QSize(1000, 1000))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.PBplus.setFont(font)
        self.PBplus.setObjectName("PBplus")
        self.horizontalLayout.addWidget(self.PBplus)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.PBAbbrechen = QtWidgets.QPushButton(addingredient)
        self.PBAbbrechen.setMinimumSize(QtCore.QSize(0, 70))
        self.PBAbbrechen.setMaximumSize(QtCore.QSize(16777215, 200))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.PBAbbrechen.setFont(font)
        self.PBAbbrechen.setObjectName("PBAbbrechen")
        self.verticalLayout.addWidget(self.PBAbbrechen)
        self.PBAusgeben = QtWidgets.QPushButton(addingredient)
        self.PBAusgeben.setMinimumSize(QtCore.QSize(0, 70))
        self.PBAusgeben.setMaximumSize(QtCore.QSize(16777215, 200))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.PBAusgeben.setFont(font)
        self.PBAusgeben.setObjectName("PBAusgeben")
        self.verticalLayout.addWidget(self.PBAusgeben)

        self.retranslateUi(addingredient)
        QtCore.QMetaObject.connectSlotsByName(addingredient)

    def retranslateUi(self, addingredient):
        _translate = QtCore.QCoreApplication.translate
        addingredient.setWindowTitle(_translate("addingredient", "Zutatenausgabe auswählen"))
        self.LHeader.setText(_translate("addingredient", "Select output ingredient"))
        self.LHeader.setProperty("cssClass", _translate("addingredient", "secondary bold"))
        self.PBminus.setText(_translate("addingredient", "-"))
        self.LAmount.setText(_translate("addingredient", "50"))
        self.LAmount.setProperty("cssClass", _translate("addingredient", "secondary bold"))
        self.PBplus.setText(_translate("addingredient", "+"))
        self.PBAbbrechen.setText(_translate("addingredient", "Abbrechen"))
        self.PBAusgeben.setText(_translate("addingredient", "Ausgeben"))
        self.PBAusgeben.setProperty("cssClass", _translate("addingredient", "btn-inverted"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    addingredient = QtWidgets.QDialog()
    ui = Ui_addingredient()
    ui.setupUi(addingredient)
    addingredient.show()
    sys.exit(app.exec_())
