# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\datepicker.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Datepicker(object):
    def setupUi(self, Datepicker):
        Datepicker.setObjectName("Datepicker")
        Datepicker.resize(800, 480)
        Datepicker.setMinimumSize(QtCore.QSize(800, 480))
        Datepicker.setMaximumSize(QtCore.QSize(800, 480))
        self.centralwidget = QtWidgets.QWidget(Datepicker)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.header = QtWidgets.QLabel(self.centralwidget)
        self.header.setMinimumSize(QtCore.QSize(0, 100))
        self.header.setMaximumSize(QtCore.QSize(16777215, 150))
        font = QtGui.QFont()
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)
        self.header.setFont(font)
        self.header.setAlignment(QtCore.Qt.AlignCenter)
        self.header.setObjectName("header")
        self.verticalLayout_2.addWidget(self.header)
        self.selected_date = QtWidgets.QDateEdit(self.centralwidget)
        self.selected_date.setMinimumSize(QtCore.QSize(0, 50))
        self.selected_date.setMaximumSize(QtCore.QSize(16777215, 200))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.selected_date.setFont(font)
        self.selected_date.setCalendarPopup(False)
        self.selected_date.setObjectName("selected_date")
        self.verticalLayout_2.addWidget(self.selected_date)
        self.selected_time = QtWidgets.QTimeEdit(self.centralwidget)
        self.selected_time.setMinimumSize(QtCore.QSize(0, 50))
        self.selected_time.setMaximumSize(QtCore.QSize(16777215, 200))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.selected_time.setFont(font)
        self.selected_time.setCalendarPopup(False)
        self.selected_time.setObjectName("selected_time")
        self.verticalLayout_2.addWidget(self.selected_time)
        self.pb_ok = QtWidgets.QPushButton(self.centralwidget)
        self.pb_ok.setMinimumSize(QtCore.QSize(0, 70))
        self.pb_ok.setMaximumSize(QtCore.QSize(16777215, 200))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.pb_ok.setFont(font)
        self.pb_ok.setObjectName("pb_ok")
        self.verticalLayout_2.addWidget(self.pb_ok)
        Datepicker.setCentralWidget(self.centralwidget)

        self.retranslateUi(Datepicker)
        QtCore.QMetaObject.connectSlotsByName(Datepicker)

    def retranslateUi(self, Datepicker):
        _translate = QtCore.QCoreApplication.translate
        Datepicker.setWindowTitle(_translate("Datepicker", "datepicker"))
        self.header.setText(_translate("Datepicker", "Select Date and Time"))
        self.header.setProperty("cssClass", _translate("Datepicker", "neutral bold"))
        self.selected_date.setProperty("cssClass", _translate("Datepicker", "bold"))
        self.selected_time.setProperty("cssClass", _translate("Datepicker", "bold"))
        self.pb_ok.setText(_translate("Datepicker", "Ok"))
        self.pb_ok.setProperty("cssClass", _translate("Datepicker", "btn-inverted"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Datepicker = QtWidgets.QMainWindow()
    ui = Ui_Datepicker()
    ui.setupUi(Datepicker)
    Datepicker.show()
    sys.exit(app.exec_())
