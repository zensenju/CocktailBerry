# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\config_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ConfigWindow(object):
    def setupUi(self, ConfigWindow):
        ConfigWindow.setObjectName("ConfigWindow")
        ConfigWindow.resize(800, 502)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ConfigWindow.sizePolicy().hasHeightForWidth())
        ConfigWindow.setSizePolicy(sizePolicy)
        ConfigWindow.setMinimumSize(QtCore.QSize(800, 480))
        ConfigWindow.setMaximumSize(QtCore.QSize(800, 700))
        ConfigWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        ConfigWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(ConfigWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabs_option = QtWidgets.QTabWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.tabs_option.setFont(font)
        self.tabs_option.setDocumentMode(False)
        self.tabs_option.setObjectName("tabs_option")
        self.tab_ui = QtWidgets.QWidget()
        self.tab_ui.setObjectName("tab_ui")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab_ui)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.scrollArea_ui = QtWidgets.QScrollArea(self.tab_ui)
        self.scrollArea_ui.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea_ui.setFrameShadow(QtWidgets.QFrame.Plain)
        self.scrollArea_ui.setLineWidth(1)
        self.scrollArea_ui.setWidgetResizable(True)
        self.scrollArea_ui.setObjectName("scrollArea_ui")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 794, 413))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.vbox_ui = QtWidgets.QVBoxLayout()
        self.vbox_ui.setContentsMargins(9, 3, 6, 15)
        self.vbox_ui.setSpacing(6)
        self.vbox_ui.setObjectName("vbox_ui")
        self.verticalLayout_4.addLayout(self.vbox_ui)
        self.scrollArea_ui.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_3.addWidget(self.scrollArea_ui)
        self.tabs_option.addTab(self.tab_ui, "")
        self.tab_maker = QtWidgets.QWidget()
        self.tab_maker.setObjectName("tab_maker")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.tab_maker)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.scrollArea_maker = QtWidgets.QScrollArea(self.tab_maker)
        self.scrollArea_maker.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea_maker.setFrameShadow(QtWidgets.QFrame.Plain)
        self.scrollArea_maker.setLineWidth(1)
        self.scrollArea_maker.setWidgetResizable(True)
        self.scrollArea_maker.setObjectName("scrollArea_maker")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 794, 423))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.vbox_maker = QtWidgets.QVBoxLayout()
        self.vbox_maker.setContentsMargins(9, 3, 6, 15)
        self.vbox_maker.setObjectName("vbox_maker")
        self.verticalLayout_5.addLayout(self.vbox_maker)
        self.scrollArea_maker.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout_6.addWidget(self.scrollArea_maker)
        self.tabs_option.addTab(self.tab_maker, "")
        self.tab_hardware = QtWidgets.QWidget()
        self.tab_hardware.setObjectName("tab_hardware")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.tab_hardware)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.scrollArea_hardware = QtWidgets.QScrollArea(self.tab_hardware)
        self.scrollArea_hardware.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea_hardware.setFrameShadow(QtWidgets.QFrame.Plain)
        self.scrollArea_hardware.setLineWidth(1)
        self.scrollArea_hardware.setWidgetResizable(True)
        self.scrollArea_hardware.setObjectName("scrollArea_hardware")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 794, 423))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.vbox_hardware = QtWidgets.QVBoxLayout()
        self.vbox_hardware.setContentsMargins(9, 3, 6, 15)
        self.vbox_hardware.setObjectName("vbox_hardware")
        self.verticalLayout_7.addLayout(self.vbox_hardware)
        self.scrollArea_hardware.setWidget(self.scrollAreaWidgetContents_3)
        self.verticalLayout_8.addWidget(self.scrollArea_hardware)
        self.tabs_option.addTab(self.tab_hardware, "")
        self.tab_software = QtWidgets.QWidget()
        self.tab_software.setObjectName("tab_software")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.tab_software)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.scrollArea_software = QtWidgets.QScrollArea(self.tab_software)
        self.scrollArea_software.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea_software.setFrameShadow(QtWidgets.QFrame.Plain)
        self.scrollArea_software.setLineWidth(1)
        self.scrollArea_software.setWidgetResizable(True)
        self.scrollArea_software.setObjectName("scrollArea_software")
        self.scrollAreaWidgetContents_4 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_4.setGeometry(QtCore.QRect(0, 0, 794, 423))
        self.scrollAreaWidgetContents_4.setObjectName("scrollAreaWidgetContents_4")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_4)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.vbox_software = QtWidgets.QVBoxLayout()
        self.vbox_software.setContentsMargins(9, 3, 6, 15)
        self.vbox_software.setObjectName("vbox_software")
        self.verticalLayout_9.addLayout(self.vbox_software)
        self.scrollArea_software.setWidget(self.scrollAreaWidgetContents_4)
        self.verticalLayout_10.addWidget(self.scrollArea_software)
        self.tabs_option.addTab(self.tab_software, "")
        self.tab_other = QtWidgets.QWidget()
        self.tab_other.setObjectName("tab_other")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.tab_other)
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.scrollArea_other = QtWidgets.QScrollArea(self.tab_other)
        self.scrollArea_other.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea_other.setFrameShadow(QtWidgets.QFrame.Plain)
        self.scrollArea_other.setLineWidth(1)
        self.scrollArea_other.setWidgetResizable(True)
        self.scrollArea_other.setObjectName("scrollArea_other")
        self.scrollAreaWidgetContents_5 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_5.setGeometry(QtCore.QRect(0, 0, 794, 423))
        self.scrollAreaWidgetContents_5.setObjectName("scrollAreaWidgetContents_5")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_5)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.vbox_other = QtWidgets.QVBoxLayout()
        self.vbox_other.setContentsMargins(9, 3, 6, 15)
        self.vbox_other.setObjectName("vbox_other")
        self.verticalLayout_11.addLayout(self.vbox_other)
        self.scrollArea_other.setWidget(self.scrollAreaWidgetContents_5)
        self.verticalLayout_12.addWidget(self.scrollArea_other)
        self.tabs_option.addTab(self.tab_other, "")
        self.verticalLayout.addWidget(self.tabs_option)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.button_back = QtWidgets.QPushButton(self.centralwidget)
        self.button_back.setMinimumSize(QtCore.QSize(0, 60))
        self.button_back.setMaximumSize(QtCore.QSize(16777215, 80))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.button_back.setFont(font)
        self.button_back.setProperty("cssClass", "")
        self.button_back.setObjectName("button_back")
        self.horizontalLayout.addWidget(self.button_back)
        self.button_save = QtWidgets.QPushButton(self.centralwidget)
        self.button_save.setMinimumSize(QtCore.QSize(0, 60))
        self.button_save.setMaximumSize(QtCore.QSize(16777215, 80))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.button_save.setFont(font)
        self.button_save.setObjectName("button_save")
        self.horizontalLayout.addWidget(self.button_save)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tabs_option.raise_()
        ConfigWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(ConfigWindow)
        self.tabs_option.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(ConfigWindow)

    def retranslateUi(self, ConfigWindow):
        _translate = QtCore.QCoreApplication.translate
        ConfigWindow.setWindowTitle(_translate("ConfigWindow", "~~ Change Configuration ~~"))
        self.tabs_option.setProperty("cssClass", _translate("ConfigWindow", "tabs-padded"))
        self.tab_ui.setProperty("cssClass", _translate("ConfigWindow", "tabs-padded"))
        self.tabs_option.setTabText(self.tabs_option.indexOf(self.tab_ui), _translate("ConfigWindow", "    UI    "))
        self.tab_maker.setProperty("cssClass", _translate("ConfigWindow", "tabs-padded"))
        self.tabs_option.setTabText(self.tabs_option.indexOf(self.tab_maker), _translate("ConfigWindow", "    Maker    "))
        self.tab_hardware.setProperty("cssClass", _translate("ConfigWindow", "tabs-padded"))
        self.tabs_option.setTabText(self.tabs_option.indexOf(self.tab_hardware), _translate("ConfigWindow", "    Hardware    "))
        self.tab_software.setProperty("cssClass", _translate("ConfigWindow", "tabs-padded"))
        self.tabs_option.setTabText(self.tabs_option.indexOf(self.tab_software), _translate("ConfigWindow", "    Software    "))
        self.tab_other.setProperty("cssClass", _translate("ConfigWindow", "tabs-padded"))
        self.tabs_option.setTabText(self.tabs_option.indexOf(self.tab_other), _translate("ConfigWindow", "    Other    "))
        self.button_back.setText(_translate("ConfigWindow", "< Back"))
        self.button_save.setText(_translate("ConfigWindow", "Save"))
        self.button_save.setProperty("cssClass", _translate("ConfigWindow", "btn-inverted"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ConfigWindow = QtWidgets.QMainWindow()
    ui = Ui_ConfigWindow()
    ui.setupUi(ConfigWindow)
    ConfigWindow.show()
    sys.exit(app.exec_())
