# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\calibration.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CalibrationWindow(object):
    def setupUi(self, CalibrationWindow):
        CalibrationWindow.setObjectName("CalibrationWindow")
        CalibrationWindow.resize(780, 480)
        CalibrationWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(CalibrationWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 2, 2, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 2, 2, 1)
        self.amount_plus = QtWidgets.QPushButton(self.centralwidget)
        self.amount_plus.setMinimumSize(QtCore.QSize(60, 40))
        self.amount_plus.setMaximumSize(QtCore.QSize(150, 150))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.amount_plus.setFont(font)
        self.amount_plus.setObjectName("amount_plus")
        self.gridLayout.addWidget(self.amount_plus, 3, 1, 1, 1)
        self.amount_minus = QtWidgets.QPushButton(self.centralwidget)
        self.amount_minus.setMinimumSize(QtCore.QSize(60, 40))
        self.amount_minus.setMaximumSize(QtCore.QSize(150, 150))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.amount_minus.setFont(font)
        self.amount_minus.setObjectName("amount_minus")
        self.gridLayout.addWidget(self.amount_minus, 4, 1, 1, 1)
        self.PB_start = QtWidgets.QPushButton(self.centralwidget)
        self.PB_start.setMinimumSize(QtCore.QSize(0, 150))
        self.PB_start.setMaximumSize(QtCore.QSize(16777215, 500))
        font = QtGui.QFont()
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.PB_start.setFont(font)
        self.PB_start.setObjectName("PB_start")
        self.gridLayout.addWidget(self.PB_start, 6, 0, 1, 3)
        self.channel_plus = QtWidgets.QPushButton(self.centralwidget)
        self.channel_plus.setMinimumSize(QtCore.QSize(100, 40))
        self.channel_plus.setMaximumSize(QtCore.QSize(150, 150))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.channel_plus.setFont(font)
        self.channel_plus.setObjectName("channel_plus")
        self.gridLayout.addWidget(self.channel_plus, 1, 1, 1, 1)
        self.channel_minus = QtWidgets.QPushButton(self.centralwidget)
        self.channel_minus.setMinimumSize(QtCore.QSize(60, 40))
        self.channel_minus.setMaximumSize(QtCore.QSize(150, 150))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.channel_minus.setFont(font)
        self.channel_minus.setObjectName("channel_minus")
        self.gridLayout.addWidget(self.channel_minus, 2, 1, 1, 1)
        self.amount = QtWidgets.QLabel(self.centralwidget)
        self.amount.setMinimumSize(QtCore.QSize(0, 100))
        self.amount.setMaximumSize(QtCore.QSize(16777215, 300))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.amount.setFont(font)
        self.amount.setAlignment(QtCore.Qt.AlignCenter)
        self.amount.setObjectName("amount")
        self.gridLayout.addWidget(self.amount, 3, 0, 2, 1)
        self.channel = QtWidgets.QLabel(self.centralwidget)
        self.channel.setMinimumSize(QtCore.QSize(0, 100))
        self.channel.setMaximumSize(QtCore.QSize(16777215, 300))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.channel.setFont(font)
        self.channel.setAlignment(QtCore.Qt.AlignCenter)
        self.channel.setObjectName("channel")
        self.gridLayout.addWidget(self.channel, 1, 0, 2, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setMinimumSize(QtCore.QSize(0, 30))
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.button_exit = QtWidgets.QPushButton(self.centralwidget)
        self.button_exit.setMinimumSize(QtCore.QSize(100, 40))
        self.button_exit.setMaximumSize(QtCore.QSize(150, 150))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.button_exit.setFont(font)
        self.button_exit.setObjectName("button_exit")
        self.horizontalLayout.addWidget(self.button_exit)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 3)
        self.verticalLayout.addLayout(self.gridLayout)
        CalibrationWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(CalibrationWindow)
        QtCore.QMetaObject.connectSlotsByName(CalibrationWindow)

    def retranslateUi(self, CalibrationWindow):
        _translate = QtCore.QCoreApplication.translate
        CalibrationWindow.setWindowTitle(_translate("CalibrationWindow", "Calibration"))
        self.label_2.setText(_translate("CalibrationWindow", "Amount"))
        self.label_2.setProperty("cssClass", _translate("CalibrationWindow", "bold"))
        self.label.setText(_translate("CalibrationWindow", "Channel"))
        self.label.setProperty("cssClass", _translate("CalibrationWindow", "bold"))
        self.amount_plus.setText(_translate("CalibrationWindow", "+"))
        self.amount_plus.setProperty("cssClass", _translate("CalibrationWindow", "btn-inverted"))
        self.amount_minus.setText(_translate("CalibrationWindow", "-"))
        self.amount_minus.setProperty("cssClass", _translate("CalibrationWindow", "btn-inverted"))
        self.PB_start.setText(_translate("CalibrationWindow", "Start"))
        self.PB_start.setProperty("cssClass", _translate("CalibrationWindow", "btn-inverted"))
        self.channel_plus.setText(_translate("CalibrationWindow", "+"))
        self.channel_plus.setProperty("cssClass", _translate("CalibrationWindow", "btn-inverted"))
        self.channel_minus.setText(_translate("CalibrationWindow", "-"))
        self.channel_minus.setProperty("cssClass", _translate("CalibrationWindow", "btn-inverted"))
        self.amount.setText(_translate("CalibrationWindow", "10"))
        self.amount.setProperty("cssClass", _translate("CalibrationWindow", "bold"))
        self.channel.setText(_translate("CalibrationWindow", "1"))
        self.channel.setProperty("cssClass", _translate("CalibrationWindow", "bold"))
        self.label_4.setText(_translate("CalibrationWindow", "Pump Calibration Program"))
        self.button_exit.setText(_translate("CalibrationWindow", "exit"))
        self.button_exit.setProperty("cssClass", _translate("CalibrationWindow", "btn-inverted"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CalibrationWindow = QtWidgets.QMainWindow()
    ui = Ui_CalibrationWindow()
    ui.setupUi(CalibrationWindow)
    CalibrationWindow.show()
    sys.exit(app.exec_())
