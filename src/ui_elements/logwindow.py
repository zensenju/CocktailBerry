# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\logwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LogWindow(object):
    def setupUi(self, LogWindow):
        LogWindow.setObjectName("LogWindow")
        LogWindow.resize(800, 480)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(LogWindow.sizePolicy().hasHeightForWidth())
        LogWindow.setSizePolicy(sizePolicy)
        LogWindow.setMinimumSize(QtCore.QSize(800, 480))
        LogWindow.setMaximumSize(QtCore.QSize(800, 480))
        LogWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        LogWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(LogWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setFrameShadow(QtWidgets.QFrame.Plain)
        self.scrollArea.setLineWidth(0)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 782, 401))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setContentsMargins(0, 0, 4, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.text_display = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents)
        self.text_display.setObjectName("text_display")
        self.verticalLayout.addWidget(self.text_display)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_2.addWidget(self.scrollArea)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.button_back = QtWidgets.QPushButton(self.centralwidget)
        self.button_back.setMaximumSize(QtCore.QSize(5000, 300))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.button_back.setFont(font)
        self.button_back.setObjectName("button_back")
        self.horizontalLayout.addWidget(self.button_back)
        self.selection_logs = QtWidgets.QComboBox(self.centralwidget)
        self.selection_logs.setMinimumSize(QtCore.QSize(105, 38))
        self.selection_logs.setMaximumSize(QtCore.QSize(300, 100))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.selection_logs.setFont(font)
        self.selection_logs.setMaxVisibleItems(11)
        self.selection_logs.setObjectName("selection_logs")
        self.horizontalLayout.addWidget(self.selection_logs)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        LogWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(LogWindow)
        QtCore.QMetaObject.connectSlotsByName(LogWindow)

    def retranslateUi(self, LogWindow):
        _translate = QtCore.QCoreApplication.translate
        LogWindow.setWindowTitle(_translate("LogWindow", "Logs"))
        self.button_back.setText(_translate("LogWindow", "< Back"))
        self.button_back.setProperty("cssClass", _translate("LogWindow", "btn-inverted"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LogWindow = QtWidgets.QMainWindow()
    ui = Ui_LogWindow()
    ui.setupUi(LogWindow)
    LogWindow.show()
    sys.exit(app.exec_())
