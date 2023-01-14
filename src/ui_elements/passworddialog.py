# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\passworddialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PasswordDialog(object):
    def setupUi(self, PasswordDialog):
        PasswordDialog.setObjectName("PasswordDialog")
        PasswordDialog.resize(800, 480)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(PasswordDialog.sizePolicy().hasHeightForWidth())
        PasswordDialog.setSizePolicy(sizePolicy)
        PasswordDialog.setMinimumSize(QtCore.QSize(800, 480))
        PasswordDialog.setMaximumSize(QtCore.QSize(800, 480))
        PasswordDialog.setStyleSheet("")
        PasswordDialog.setModal(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(PasswordDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.LHeader = QtWidgets.QLabel(PasswordDialog)
        self.LHeader.setMinimumSize(QtCore.QSize(0, 50))
        self.LHeader.setMaximumSize(QtCore.QSize(16777215, 60))
        font = QtGui.QFont()
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)
        self.LHeader.setFont(font)
        self.LHeader.setAlignment(QtCore.Qt.AlignCenter)
        self.LHeader.setObjectName("LHeader")
        self.verticalLayout.addWidget(self.LHeader)
        self.password_field = ClickableLineEdit(PasswordDialog)
        self.password_field.setMinimumSize(QtCore.QSize(0, 40))
        self.password_field.setMaximumSize(QtCore.QSize(200000, 60))
        self.password_field.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_field.setObjectName("password_field")
        self.verticalLayout.addWidget(self.password_field)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout.addItem(spacerItem)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.PB2 = QtWidgets.QPushButton(PasswordDialog)
        self.PB2.setMinimumSize(QtCore.QSize(110, 70))
        self.PB2.setMaximumSize(QtCore.QSize(110, 80))
        font = QtGui.QFont()
        font.setPointSize(40)
        font.setBold(True)
        font.setWeight(75)
        self.PB2.setFont(font)
        self.PB2.setObjectName("PB2")
        self.gridLayout.addWidget(self.PB2, 0, 1, 1, 1)
        self.PB1 = QtWidgets.QPushButton(PasswordDialog)
        self.PB1.setMinimumSize(QtCore.QSize(110, 70))
        self.PB1.setMaximumSize(QtCore.QSize(110, 80))
        font = QtGui.QFont()
        font.setPointSize(40)
        font.setBold(True)
        font.setWeight(75)
        self.PB1.setFont(font)
        self.PB1.setObjectName("PB1")
        self.gridLayout.addWidget(self.PB1, 0, 0, 1, 1)
        self.PB0 = QtWidgets.QPushButton(PasswordDialog)
        self.PB0.setMinimumSize(QtCore.QSize(110, 70))
        self.PB0.setMaximumSize(QtCore.QSize(110, 80))
        font = QtGui.QFont()
        font.setPointSize(40)
        font.setBold(True)
        font.setWeight(75)
        self.PB0.setFont(font)
        self.PB0.setObjectName("PB0")
        self.gridLayout.addWidget(self.PB0, 1, 4, 1, 1)
        self.PB9 = QtWidgets.QPushButton(PasswordDialog)
        self.PB9.setMinimumSize(QtCore.QSize(110, 70))
        self.PB9.setMaximumSize(QtCore.QSize(110, 80))
        font = QtGui.QFont()
        font.setPointSize(40)
        font.setBold(True)
        font.setWeight(75)
        self.PB9.setFont(font)
        self.PB9.setObjectName("PB9")
        self.gridLayout.addWidget(self.PB9, 1, 3, 1, 1)
        self.PB4 = QtWidgets.QPushButton(PasswordDialog)
        self.PB4.setMinimumSize(QtCore.QSize(110, 70))
        self.PB4.setMaximumSize(QtCore.QSize(110, 80))
        font = QtGui.QFont()
        font.setPointSize(40)
        font.setBold(True)
        font.setWeight(75)
        self.PB4.setFont(font)
        self.PB4.setObjectName("PB4")
        self.gridLayout.addWidget(self.PB4, 0, 3, 1, 1)
        self.PB3 = QtWidgets.QPushButton(PasswordDialog)
        self.PB3.setMinimumSize(QtCore.QSize(110, 70))
        self.PB3.setMaximumSize(QtCore.QSize(110, 80))
        font = QtGui.QFont()
        font.setPointSize(40)
        font.setBold(True)
        font.setWeight(75)
        self.PB3.setFont(font)
        self.PB3.setObjectName("PB3")
        self.gridLayout.addWidget(self.PB3, 0, 2, 1, 1)
        self.PB8 = QtWidgets.QPushButton(PasswordDialog)
        self.PB8.setMinimumSize(QtCore.QSize(110, 70))
        self.PB8.setMaximumSize(QtCore.QSize(110, 80))
        font = QtGui.QFont()
        font.setPointSize(40)
        font.setBold(True)
        font.setWeight(75)
        self.PB8.setFont(font)
        self.PB8.setObjectName("PB8")
        self.gridLayout.addWidget(self.PB8, 1, 2, 1, 1)
        self.PB7 = QtWidgets.QPushButton(PasswordDialog)
        self.PB7.setMinimumSize(QtCore.QSize(110, 70))
        self.PB7.setMaximumSize(QtCore.QSize(110, 80))
        font = QtGui.QFont()
        font.setPointSize(40)
        font.setBold(True)
        font.setWeight(75)
        self.PB7.setFont(font)
        self.PB7.setObjectName("PB7")
        self.gridLayout.addWidget(self.PB7, 1, 1, 1, 1)
        self.PB6 = QtWidgets.QPushButton(PasswordDialog)
        self.PB6.setMinimumSize(QtCore.QSize(110, 70))
        self.PB6.setMaximumSize(QtCore.QSize(110, 80))
        font = QtGui.QFont()
        font.setPointSize(40)
        font.setBold(True)
        font.setWeight(75)
        self.PB6.setFont(font)
        self.PB6.setObjectName("PB6")
        self.gridLayout.addWidget(self.PB6, 1, 0, 1, 1)
        self.PB5 = QtWidgets.QPushButton(PasswordDialog)
        self.PB5.setMinimumSize(QtCore.QSize(110, 70))
        self.PB5.setMaximumSize(QtCore.QSize(110, 80))
        font = QtGui.QFont()
        font.setPointSize(40)
        font.setBold(True)
        font.setWeight(75)
        self.PB5.setFont(font)
        self.PB5.setObjectName("PB5")
        self.gridLayout.addWidget(self.PB5, 0, 4, 1, 1)
        self.enter_button = QtWidgets.QPushButton(PasswordDialog)
        self.enter_button.setMinimumSize(QtCore.QSize(110, 70))
        self.enter_button.setMaximumSize(QtCore.QSize(300, 80))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.enter_button.setFont(font)
        self.enter_button.setObjectName("enter_button")
        self.gridLayout.addWidget(self.enter_button, 2, 3, 1, 2)
        self.PBdel = QtWidgets.QPushButton(PasswordDialog)
        self.PBdel.setMinimumSize(QtCore.QSize(110, 70))
        self.PBdel.setMaximumSize(QtCore.QSize(110, 80))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.PBdel.setFont(font)
        self.PBdel.setObjectName("PBdel")
        self.gridLayout.addWidget(self.PBdel, 2, 2, 1, 1)
        self.cancel_button = QtWidgets.QPushButton(PasswordDialog)
        self.cancel_button.setMinimumSize(QtCore.QSize(110, 70))
        self.cancel_button.setMaximumSize(QtCore.QSize(300, 80))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.cancel_button.setFont(font)
        self.cancel_button.setObjectName("cancel_button")
        self.gridLayout.addWidget(self.cancel_button, 2, 0, 1, 2)
        self.verticalLayout.addLayout(self.gridLayout)

        self.retranslateUi(PasswordDialog)
        QtCore.QMetaObject.connectSlotsByName(PasswordDialog)

    def retranslateUi(self, PasswordDialog):
        _translate = QtCore.QCoreApplication.translate
        PasswordDialog.setWindowTitle(_translate("PasswordDialog", "~~ Enter Password ~~"))
        self.LHeader.setText(_translate("PasswordDialog", "Enter Password:"))
        self.LHeader.setProperty("cssClass", _translate("PasswordDialog", "neutral bold"))
        self.password_field.setProperty("cssClass", _translate("PasswordDialog", "bold"))
        self.PB2.setText(_translate("PasswordDialog", "2"))
        self.PB1.setText(_translate("PasswordDialog", "1"))
        self.PB0.setText(_translate("PasswordDialog", "0"))
        self.PB9.setText(_translate("PasswordDialog", "9"))
        self.PB4.setText(_translate("PasswordDialog", "4"))
        self.PB3.setText(_translate("PasswordDialog", "3"))
        self.PB8.setText(_translate("PasswordDialog", "8"))
        self.PB7.setText(_translate("PasswordDialog", "7"))
        self.PB6.setText(_translate("PasswordDialog", "6"))
        self.PB5.setText(_translate("PasswordDialog", "5"))
        self.enter_button.setText(_translate("PasswordDialog", "OK"))
        self.enter_button.setProperty("cssClass", _translate("PasswordDialog", "btn-inverted"))
        self.PBdel.setText(_translate("PasswordDialog", "del"))
        self.cancel_button.setText(_translate("PasswordDialog", "Cancel"))
        self.cancel_button.setProperty("cssClass", _translate("PasswordDialog", "btn-inverted"))
from src.ui_elements.clickablelineedit import ClickableLineEdit


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PasswordDialog = QtWidgets.QDialog()
    ui = Ui_PasswordDialog()
    ui.setupUi(PasswordDialog)
    PasswordDialog.show()
    sys.exit(app.exec_())
