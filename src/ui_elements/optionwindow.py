# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\optionwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Optionwindow(object):
    def setupUi(self, Optionwindow):
        Optionwindow.setObjectName("Optionwindow")
        Optionwindow.resize(800, 480)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Optionwindow.sizePolicy().hasHeightForWidth())
        Optionwindow.setSizePolicy(sizePolicy)
        Optionwindow.setMinimumSize(QtCore.QSize(800, 480))
        Optionwindow.setMaximumSize(QtCore.QSize(800, 480))
        Optionwindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        Optionwindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(Optionwindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.button_back = QtWidgets.QPushButton(self.centralwidget)
        self.button_back.setMaximumSize(QtCore.QSize(5000, 300))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.button_back.setFont(font)
        self.button_back.setObjectName("button_back")
        self.gridLayout.addWidget(self.button_back, 5, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.button_reboot = QtWidgets.QPushButton(self.centralwidget)
        self.button_reboot.setMaximumSize(QtCore.QSize(5000, 300))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.button_reboot.setFont(font)
        self.button_reboot.setObjectName("button_reboot")
        self.horizontalLayout.addWidget(self.button_reboot)
        self.button_shutdown = QtWidgets.QPushButton(self.centralwidget)
        self.button_shutdown.setMaximumSize(QtCore.QSize(5000, 300))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.button_shutdown.setFont(font)
        self.button_shutdown.setObjectName("button_shutdown")
        self.horizontalLayout.addWidget(self.button_shutdown)
        self.gridLayout.addLayout(self.horizontalLayout, 4, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.button_clean = QtWidgets.QPushButton(self.centralwidget)
        self.button_clean.setMaximumSize(QtCore.QSize(5000, 300))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.button_clean.setFont(font)
        self.button_clean.setObjectName("button_clean")
        self.horizontalLayout_2.addWidget(self.button_clean)
        self.button_calibration = QtWidgets.QPushButton(self.centralwidget)
        self.button_calibration.setMaximumSize(QtCore.QSize(5000, 300))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.button_calibration.setFont(font)
        self.button_calibration.setObjectName("button_calibration")
        self.horizontalLayout_2.addWidget(self.button_calibration)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.button_backup = QtWidgets.QPushButton(self.centralwidget)
        self.button_backup.setMaximumSize(QtCore.QSize(5000, 300))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.button_backup.setFont(font)
        self.button_backup.setObjectName("button_backup")
        self.horizontalLayout_3.addWidget(self.button_backup)
        self.button_restore = QtWidgets.QPushButton(self.centralwidget)
        self.button_restore.setMaximumSize(QtCore.QSize(5000, 300))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.button_restore.setFont(font)
        self.button_restore.setObjectName("button_restore")
        self.horizontalLayout_3.addWidget(self.button_restore)
        self.gridLayout.addLayout(self.horizontalLayout_3, 3, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.button_config = QtWidgets.QPushButton(self.centralwidget)
        self.button_config.setMaximumSize(QtCore.QSize(5000, 300))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.button_config.setFont(font)
        self.button_config.setObjectName("button_config")
        self.horizontalLayout_4.addWidget(self.button_config)
        self.button_export = QtWidgets.QPushButton(self.centralwidget)
        self.button_export.setMaximumSize(QtCore.QSize(5000, 300))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.button_export.setFont(font)
        self.button_export.setObjectName("button_export")
        self.horizontalLayout_4.addWidget(self.button_export)
        self.gridLayout.addLayout(self.horizontalLayout_4, 2, 0, 1, 1)
        Optionwindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(Optionwindow)
        QtCore.QMetaObject.connectSlotsByName(Optionwindow)

    def retranslateUi(self, Optionwindow):
        _translate = QtCore.QCoreApplication.translate
        Optionwindow.setWindowTitle(_translate("Optionwindow", "Options"))
        self.button_back.setText(_translate("Optionwindow", "< Back"))
        self.button_reboot.setText(_translate("Optionwindow", "Reboot"))
        self.button_shutdown.setText(_translate("Optionwindow", "Shutdown"))
        self.button_clean.setText(_translate("Optionwindow", "Cleaning"))
        self.button_calibration.setText(_translate("Optionwindow", "Calibration"))
        self.button_backup.setText(_translate("Optionwindow", "Backup"))
        self.button_restore.setText(_translate("Optionwindow", "Restore"))
        self.button_config.setText(_translate("Optionwindow", "Change Config"))
        self.button_export.setText(_translate("Optionwindow", "Export"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Optionwindow = QtWidgets.QMainWindow()
    ui = Ui_Optionwindow()
    ui.setupUi(Optionwindow)
    Optionwindow.show()
    sys.exit(app.exec_())
