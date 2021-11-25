# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ui_elements\bottlewindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Bottlewindow(object):
    def setupUi(self, Bottlewindow):
        Bottlewindow.setObjectName("Bottlewindow")
        Bottlewindow.resize(800, 480)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Bottlewindow.sizePolicy().hasHeightForWidth())
        Bottlewindow.setSizePolicy(sizePolicy)
        Bottlewindow.setMinimumSize(QtCore.QSize(800, 480))
        Bottlewindow.setMaximumSize(QtCore.QSize(800, 480))
        Bottlewindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        Bottlewindow.setStyleSheet("QWidget\n"
"{\n"
"    color: rgb(0, 123, 255);    \n"
"    background-color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: rgb(0, 0, 0);\n"
"    color: (0, 123, 255);\n"
"    border-width: 3px;\n"
"    border-color: rgb(0, 123, 255);\n"
"    border-style: solid;\n"
"    border-radius: 7;\n"
"    padding: 3px;\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed, QPushButton:checked\n"
"{\n"
"    color: rgb(239, 151, 0);    \n"
"    border-color: rgb(239, 151, 0);\n"
"}\n"
"\n"
"QProgressBar\n"
"{\n"
"    background-color: rgb(166, 166, 166);\n"
"    color: rgb(0, 0, 0);\n"
"    border: 2px rgb(166, 166, 166);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    border: 2px rgb(166, 166, 166);\n"
"    border-top-left-radius: 5px;\n"
"    border-bottom-left-radius: 5px;\n"
"    border-top-right-radius: 5px;\n"
"    border-bottom-right-radius: 5px;\n"
"    background-color: rgb(0, 123, 255);\n"
"   /* width: 40px;\n"
"    margin: 0.5px;*/\n"
"}\n"
"\n"
"#Labbruch {\n"
"    color: rgb(239, 151, 0);\n"
"}\n"
"#LName1, #LName2, #LName3, #LName4, #LName5, #LName6, #LName7, #LName8, #LName9, #LName10 {\n"
"    color: rgb(239, 151, 0);\n"
"}\n"
"\n"
"/* Inverted button style */\n"
"#PBEintragen {\n"
"    background-color: rgb(0, 123, 255);  \n"
"    color: rgb(0, 0, 0);\n"
"    border-width: 3px;\n"
"    border-color: rgb(0, 123, 255);\n"
"    border-style: solid;\n"
"    border-radius: 7;\n"
"    padding: 3px;\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"}\n"
"\n"
"#PBEintragen:pressed {\n"
"    background-color: rgb(239, 151, 0);    \n"
"    border-color: rgb(239, 151, 0);    \n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(Bottlewindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.LAmount1 = QtWidgets.QLabel(self.centralwidget)
        self.LAmount1.setMinimumSize(QtCore.QSize(65, 0))
        self.LAmount1.setMaximumSize(QtCore.QSize(190, 200))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.LAmount1.setFont(font)
        self.LAmount1.setLineWidth(1)
        self.LAmount1.setAlignment(QtCore.Qt.AlignCenter)
        self.LAmount1.setObjectName("LAmount1")
        self.gridLayout.addWidget(self.LAmount1, 1, 2, 1, 1)
        self.LName6 = QtWidgets.QLabel(self.centralwidget)
        self.LName6.setMinimumSize(QtCore.QSize(400, 0))
        self.LName6.setMaximumSize(QtCore.QSize(1100, 200))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.LName6.setFont(font)
        self.LName6.setObjectName("LName6")
        self.gridLayout.addWidget(self.LName6, 6, 0, 1, 1)
        self.LName9 = QtWidgets.QLabel(self.centralwidget)
        self.LName9.setMinimumSize(QtCore.QSize(400, 0))
        self.LName9.setMaximumSize(QtCore.QSize(1100, 200))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.LName9.setFont(font)
        self.LName9.setObjectName("LName9")
        self.gridLayout.addWidget(self.LName9, 9, 0, 1, 1)
        self.LName7 = QtWidgets.QLabel(self.centralwidget)
        self.LName7.setMinimumSize(QtCore.QSize(400, 0))
        self.LName7.setMaximumSize(QtCore.QSize(1100, 200))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.LName7.setFont(font)
        self.LName7.setObjectName("LName7")
        self.gridLayout.addWidget(self.LName7, 7, 0, 1, 1)
        self.LName8 = QtWidgets.QLabel(self.centralwidget)
        self.LName8.setMinimumSize(QtCore.QSize(400, 0))
        self.LName8.setMaximumSize(QtCore.QSize(1100, 200))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.LName8.setFont(font)
        self.LName8.setObjectName("LName8")
        self.gridLayout.addWidget(self.LName8, 8, 0, 1, 1)
        self.LName3 = QtWidgets.QLabel(self.centralwidget)
        self.LName3.setMinimumSize(QtCore.QSize(400, 0))
        self.LName3.setMaximumSize(QtCore.QSize(1100, 200))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.LName3.setFont(font)
        self.LName3.setObjectName("LName3")
        self.gridLayout.addWidget(self.LName3, 3, 0, 1, 1)
        self.PBMminus2 = QtWidgets.QPushButton(self.centralwidget)
        self.PBMminus2.setMinimumSize(QtCore.QSize(60, 18))
        self.PBMminus2.setMaximumSize(QtCore.QSize(400, 200))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.PBMminus2.setFont(font)
        self.PBMminus2.setObjectName("PBMminus2")
        self.gridLayout.addWidget(self.PBMminus2, 2, 1, 1, 1)
        self.PBMplus1 = QtWidgets.QPushButton(self.centralwidget)
        self.PBMplus1.setMinimumSize(QtCore.QSize(60, 18))
        self.PBMplus1.setMaximumSize(QtCore.QSize(400, 200))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.PBMplus1.setFont(font)
        self.PBMplus1.setObjectName("PBMplus1")
        self.gridLayout.addWidget(self.PBMplus1, 1, 3, 1, 1)
        self.LName2 = QtWidgets.QLabel(self.centralwidget)
        self.LName2.setMinimumSize(QtCore.QSize(400, 0))
        self.LName2.setMaximumSize(QtCore.QSize(1100, 200))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.LName2.setFont(font)
        self.LName2.setObjectName("LName2")
        self.gridLayout.addWidget(self.LName2, 2, 0, 1, 1)
        self.LName5 = QtWidgets.QLabel(self.centralwidget)
        self.LName5.setMinimumSize(QtCore.QSize(400, 0))
        self.LName5.setMaximumSize(QtCore.QSize(1100, 200))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.LName5.setFont(font)
        self.LName5.setObjectName("LName5")
        self.gridLayout.addWidget(self.LName5, 5, 0, 1, 1)
        self.LName4 = QtWidgets.QLabel(self.centralwidget)
        self.LName4.setMinimumSize(QtCore.QSize(400, 0))
        self.LName4.setMaximumSize(QtCore.QSize(1100, 200))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.LName4.setFont(font)
        self.LName4.setObjectName("LName4")
        self.gridLayout.addWidget(self.LName4, 4, 0, 1, 1)
        self.LName10 = QtWidgets.QLabel(self.centralwidget)
        self.LName10.setMinimumSize(QtCore.QSize(400, 0))
        self.LName10.setMaximumSize(QtCore.QSize(1100, 200))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.LName10.setFont(font)
        self.LName10.setObjectName("LName10")
        self.gridLayout.addWidget(self.LName10, 10, 0, 1, 1)
        self.LName1 = QtWidgets.QLabel(self.centralwidget)
        self.LName1.setMinimumSize(QtCore.QSize(400, 0))
        self.LName1.setMaximumSize(QtCore.QSize(1100, 200))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.LName1.setFont(font)
        self.LName1.setObjectName("LName1")
        self.gridLayout.addWidget(self.LName1, 1, 0, 1, 1)
        self.PBMminus1 = QtWidgets.QPushButton(self.centralwidget)
        self.PBMminus1.setMinimumSize(QtCore.QSize(60, 18))
        self.PBMminus1.setMaximumSize(QtCore.QSize(400, 200))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.PBMminus1.setFont(font)
        self.PBMminus1.setObjectName("PBMminus1")
        self.gridLayout.addWidget(self.PBMminus1, 1, 1, 1, 1)
        self.PBMminus4 = QtWidgets.QPushButton(self.centralwidget)
        self.PBMminus4.setMinimumSize(QtCore.QSize(60, 18))
        self.PBMminus4.setMaximumSize(QtCore.QSize(400, 200))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.PBMminus4.setFont(font)
        self.PBMminus4.setObjectName("PBMminus4")
        self.gridLayout.addWidget(self.PBMminus4, 4, 1, 1, 1)
        self.PBMminus3 = QtWidgets.QPushButton(self.centralwidget)
        self.PBMminus3.setMinimumSize(QtCore.QSize(60, 18))
        self.PBMminus3.setMaximumSize(QtCore.QSize(400, 200))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.PBMminus3.setFont(font)
        self.PBMminus3.setObjectName("PBMminus3")
        self.gridLayout.addWidget(self.PBMminus3, 3, 1, 1, 1)
        self.LAmount9 = QtWidgets.QLabel(self.centralwidget)
        self.LAmount9.setMinimumSize(QtCore.QSize(65, 0))
        self.LAmount9.setMaximumSize(QtCore.QSize(190, 200))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.LAmount9.setFont(font)
        self.LAmount9.setLineWidth(1)
        self.LAmount9.setAlignment(QtCore.Qt.AlignCenter)
        self.LAmount9.setObjectName("LAmount9")
        self.gridLayout.addWidget(self.LAmount9, 9, 2, 1, 1)
        self.PBMminus5 = QtWidgets.QPushButton(self.centralwidget)
        self.PBMminus5.setMinimumSize(QtCore.QSize(60, 18))
        self.PBMminus5.setMaximumSize(QtCore.QSize(400, 200))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.PBMminus5.setFont(font)
        self.PBMminus5.setObjectName("PBMminus5")
        self.gridLayout.addWidget(self.PBMminus5, 5, 1, 1, 1)
        self.LAmount4 = QtWidgets.QLabel(self.centralwidget)
        self.LAmount4.setMinimumSize(QtCore.QSize(65, 0))
        self.LAmount4.setMaximumSize(QtCore.QSize(190, 200))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.LAmount4.setFont(font)
        self.LAmount4.setLineWidth(1)
        self.LAmount4.setAlignment(QtCore.Qt.AlignCenter)
        self.LAmount4.setObjectName("LAmount4")
        self.gridLayout.addWidget(self.LAmount4, 4, 2, 1, 1)
        self.PBMminus10 = QtWidgets.QPushButton(self.centralwidget)
        self.PBMminus10.setMinimumSize(QtCore.QSize(60, 18))
        self.PBMminus10.setMaximumSize(QtCore.QSize(400, 200))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.PBMminus10.setFont(font)
        self.PBMminus10.setObjectName("PBMminus10")
        self.gridLayout.addWidget(self.PBMminus10, 10, 1, 1, 1)
        self.LAmount2 = QtWidgets.QLabel(self.centralwidget)
        self.LAmount2.setMinimumSize(QtCore.QSize(65, 0))
        self.LAmount2.setMaximumSize(QtCore.QSize(190, 200))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.LAmount2.setFont(font)
        self.LAmount2.setLineWidth(1)
        self.LAmount2.setAlignment(QtCore.Qt.AlignCenter)
        self.LAmount2.setObjectName("LAmount2")
        self.gridLayout.addWidget(self.LAmount2, 2, 2, 1, 1)
        self.PBMminus9 = QtWidgets.QPushButton(self.centralwidget)
        self.PBMminus9.setMinimumSize(QtCore.QSize(60, 18))
        self.PBMminus9.setMaximumSize(QtCore.QSize(400, 200))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.PBMminus9.setFont(font)
        self.PBMminus9.setObjectName("PBMminus9")
        self.gridLayout.addWidget(self.PBMminus9, 9, 1, 1, 1)
        self.LAmount3 = QtWidgets.QLabel(self.centralwidget)
        self.LAmount3.setMinimumSize(QtCore.QSize(65, 0))
        self.LAmount3.setMaximumSize(QtCore.QSize(190, 200))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.LAmount3.setFont(font)
        self.LAmount3.setLineWidth(1)
        self.LAmount3.setAlignment(QtCore.Qt.AlignCenter)
        self.LAmount3.setObjectName("LAmount3")
        self.gridLayout.addWidget(self.LAmount3, 3, 2, 1, 1)
        self.LAmount10 = QtWidgets.QLabel(self.centralwidget)
        self.LAmount10.setMinimumSize(QtCore.QSize(65, 0))
        self.LAmount10.setMaximumSize(QtCore.QSize(190, 200))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.LAmount10.setFont(font)
        self.LAmount10.setLineWidth(1)
        self.LAmount10.setAlignment(QtCore.Qt.AlignCenter)
        self.LAmount10.setObjectName("LAmount10")
        self.gridLayout.addWidget(self.LAmount10, 10, 2, 1, 1)
        self.LAmount6 = QtWidgets.QLabel(self.centralwidget)
        self.LAmount6.setMinimumSize(QtCore.QSize(65, 0))
        self.LAmount6.setMaximumSize(QtCore.QSize(190, 200))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.LAmount6.setFont(font)
        self.LAmount6.setLineWidth(1)
        self.LAmount6.setAlignment(QtCore.Qt.AlignCenter)
        self.LAmount6.setObjectName("LAmount6")
        self.gridLayout.addWidget(self.LAmount6, 6, 2, 1, 1)
        self.LAmount5 = QtWidgets.QLabel(self.centralwidget)
        self.LAmount5.setMinimumSize(QtCore.QSize(65, 0))
        self.LAmount5.setMaximumSize(QtCore.QSize(190, 200))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.LAmount5.setFont(font)
        self.LAmount5.setLineWidth(1)
        self.LAmount5.setAlignment(QtCore.Qt.AlignCenter)
        self.LAmount5.setObjectName("LAmount5")
        self.gridLayout.addWidget(self.LAmount5, 5, 2, 1, 1)
        self.LAmount8 = QtWidgets.QLabel(self.centralwidget)
        self.LAmount8.setMinimumSize(QtCore.QSize(65, 0))
        self.LAmount8.setMaximumSize(QtCore.QSize(190, 200))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.LAmount8.setFont(font)
        self.LAmount8.setLineWidth(1)
        self.LAmount8.setAlignment(QtCore.Qt.AlignCenter)
        self.LAmount8.setObjectName("LAmount8")
        self.gridLayout.addWidget(self.LAmount8, 8, 2, 1, 1)
        self.PBMminus8 = QtWidgets.QPushButton(self.centralwidget)
        self.PBMminus8.setMinimumSize(QtCore.QSize(60, 18))
        self.PBMminus8.setMaximumSize(QtCore.QSize(400, 200))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.PBMminus8.setFont(font)
        self.PBMminus8.setObjectName("PBMminus8")
        self.gridLayout.addWidget(self.PBMminus8, 8, 1, 1, 1)
        self.PBMminus7 = QtWidgets.QPushButton(self.centralwidget)
        self.PBMminus7.setMinimumSize(QtCore.QSize(60, 18))
        self.PBMminus7.setMaximumSize(QtCore.QSize(400, 200))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.PBMminus7.setFont(font)
        self.PBMminus7.setObjectName("PBMminus7")
        self.gridLayout.addWidget(self.PBMminus7, 7, 1, 1, 1)
        self.PBMplus7 = QtWidgets.QPushButton(self.centralwidget)
        self.PBMplus7.setMinimumSize(QtCore.QSize(60, 18))
        self.PBMplus7.setMaximumSize(QtCore.QSize(400, 200))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.PBMplus7.setFont(font)
        self.PBMplus7.setObjectName("PBMplus7")
        self.gridLayout.addWidget(self.PBMplus7, 7, 3, 1, 1)
        self.PBMplus2 = QtWidgets.QPushButton(self.centralwidget)
        self.PBMplus2.setMinimumSize(QtCore.QSize(60, 18))
        self.PBMplus2.setMaximumSize(QtCore.QSize(400, 200))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.PBMplus2.setFont(font)
        self.PBMplus2.setObjectName("PBMplus2")
        self.gridLayout.addWidget(self.PBMplus2, 2, 3, 1, 1)
        self.PBMminus6 = QtWidgets.QPushButton(self.centralwidget)
        self.PBMminus6.setMinimumSize(QtCore.QSize(60, 18))
        self.PBMminus6.setMaximumSize(QtCore.QSize(400, 200))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.PBMminus6.setFont(font)
        self.PBMminus6.setObjectName("PBMminus6")
        self.gridLayout.addWidget(self.PBMminus6, 6, 1, 1, 1)
        self.PBMplus3 = QtWidgets.QPushButton(self.centralwidget)
        self.PBMplus3.setMinimumSize(QtCore.QSize(60, 18))
        self.PBMplus3.setMaximumSize(QtCore.QSize(400, 200))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.PBMplus3.setFont(font)
        self.PBMplus3.setObjectName("PBMplus3")
        self.gridLayout.addWidget(self.PBMplus3, 3, 3, 1, 1)
        self.PBMplus6 = QtWidgets.QPushButton(self.centralwidget)
        self.PBMplus6.setMinimumSize(QtCore.QSize(60, 18))
        self.PBMplus6.setMaximumSize(QtCore.QSize(400, 200))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.PBMplus6.setFont(font)
        self.PBMplus6.setObjectName("PBMplus6")
        self.gridLayout.addWidget(self.PBMplus6, 6, 3, 1, 1)
        self.PBMplus5 = QtWidgets.QPushButton(self.centralwidget)
        self.PBMplus5.setMinimumSize(QtCore.QSize(60, 18))
        self.PBMplus5.setMaximumSize(QtCore.QSize(400, 200))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.PBMplus5.setFont(font)
        self.PBMplus5.setObjectName("PBMplus5")
        self.gridLayout.addWidget(self.PBMplus5, 5, 3, 1, 1)
        self.PBMplus4 = QtWidgets.QPushButton(self.centralwidget)
        self.PBMplus4.setMinimumSize(QtCore.QSize(60, 18))
        self.PBMplus4.setMaximumSize(QtCore.QSize(400, 200))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.PBMplus4.setFont(font)
        self.PBMplus4.setObjectName("PBMplus4")
        self.gridLayout.addWidget(self.PBMplus4, 4, 3, 1, 1)
        self.PBMplus9 = QtWidgets.QPushButton(self.centralwidget)
        self.PBMplus9.setMinimumSize(QtCore.QSize(60, 18))
        self.PBMplus9.setMaximumSize(QtCore.QSize(400, 200))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.PBMplus9.setFont(font)
        self.PBMplus9.setObjectName("PBMplus9")
        self.gridLayout.addWidget(self.PBMplus9, 9, 3, 1, 1)
        self.PBMplus8 = QtWidgets.QPushButton(self.centralwidget)
        self.PBMplus8.setMinimumSize(QtCore.QSize(60, 18))
        self.PBMplus8.setMaximumSize(QtCore.QSize(400, 200))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.PBMplus8.setFont(font)
        self.PBMplus8.setObjectName("PBMplus8")
        self.gridLayout.addWidget(self.PBMplus8, 8, 3, 1, 1)
        self.LAmount7 = QtWidgets.QLabel(self.centralwidget)
        self.LAmount7.setMinimumSize(QtCore.QSize(65, 0))
        self.LAmount7.setMaximumSize(QtCore.QSize(190, 200))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.LAmount7.setFont(font)
        self.LAmount7.setLineWidth(1)
        self.LAmount7.setAlignment(QtCore.Qt.AlignCenter)
        self.LAmount7.setObjectName("LAmount7")
        self.gridLayout.addWidget(self.LAmount7, 7, 2, 1, 1)
        self.PBMplus10 = QtWidgets.QPushButton(self.centralwidget)
        self.PBMplus10.setMinimumSize(QtCore.QSize(60, 18))
        self.PBMplus10.setMaximumSize(QtCore.QSize(400, 200))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.PBMplus10.setFont(font)
        self.PBMplus10.setObjectName("PBMplus10")
        self.gridLayout.addWidget(self.PBMplus10, 10, 3, 1, 1)
        self.LHeader = QtWidgets.QLabel(self.centralwidget)
        self.LHeader.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.LHeader.setFont(font)
        self.LHeader.setAlignment(QtCore.Qt.AlignCenter)
        self.LHeader.setObjectName("LHeader")
        self.gridLayout.addWidget(self.LHeader, 0, 0, 1, 4)
        self.PBEintragen = QtWidgets.QPushButton(self.centralwidget)
        self.PBEintragen.setMinimumSize(QtCore.QSize(0, 50))
        self.PBEintragen.setMaximumSize(QtCore.QSize(1100, 300))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.PBEintragen.setFont(font)
        self.PBEintragen.setObjectName("PBEintragen")
        self.gridLayout.addWidget(self.PBEintragen, 11, 0, 1, 1)
        self.PBAbbrechen = QtWidgets.QPushButton(self.centralwidget)
        self.PBAbbrechen.setMinimumSize(QtCore.QSize(0, 50))
        self.PBAbbrechen.setMaximumSize(QtCore.QSize(1000, 300))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.PBAbbrechen.setFont(font)
        self.PBAbbrechen.setObjectName("PBAbbrechen")
        self.gridLayout.addWidget(self.PBAbbrechen, 11, 1, 1, 3)
        self.verticalLayout.addLayout(self.gridLayout)
        Bottlewindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(Bottlewindow)
        QtCore.QMetaObject.connectSlotsByName(Bottlewindow)

    def retranslateUi(self, Bottlewindow):
        _translate = QtCore.QCoreApplication.translate
        Bottlewindow.setWindowTitle(_translate("Bottlewindow", "~~ Füllstand der Flaschen auswählen ~~"))
        self.LAmount1.setText(_translate("Bottlewindow", "200"))
        self.LName6.setText(_translate("Bottlewindow", "TextLabel"))
        self.LName9.setText(_translate("Bottlewindow", "TextLabel"))
        self.LName7.setText(_translate("Bottlewindow", "TextLabel"))
        self.LName8.setText(_translate("Bottlewindow", "TextLabel"))
        self.LName3.setText(_translate("Bottlewindow", "TextLabel"))
        self.PBMminus2.setText(_translate("Bottlewindow", "-"))
        self.PBMplus1.setText(_translate("Bottlewindow", "+"))
        self.LName2.setText(_translate("Bottlewindow", "TextLabel"))
        self.LName5.setText(_translate("Bottlewindow", "TextLabel"))
        self.LName4.setText(_translate("Bottlewindow", "TextLabel"))
        self.LName10.setText(_translate("Bottlewindow", "TextLabel"))
        self.LName1.setText(_translate("Bottlewindow", "TextLabel"))
        self.PBMminus1.setText(_translate("Bottlewindow", "-"))
        self.PBMminus4.setText(_translate("Bottlewindow", "-"))
        self.PBMminus3.setText(_translate("Bottlewindow", "-"))
        self.LAmount9.setText(_translate("Bottlewindow", "200"))
        self.PBMminus5.setText(_translate("Bottlewindow", "-"))
        self.LAmount4.setText(_translate("Bottlewindow", "200"))
        self.PBMminus10.setText(_translate("Bottlewindow", "-"))
        self.LAmount2.setText(_translate("Bottlewindow", "200"))
        self.PBMminus9.setText(_translate("Bottlewindow", "-"))
        self.LAmount3.setText(_translate("Bottlewindow", "200"))
        self.LAmount10.setText(_translate("Bottlewindow", "200"))
        self.LAmount6.setText(_translate("Bottlewindow", "200"))
        self.LAmount5.setText(_translate("Bottlewindow", "200"))
        self.LAmount8.setText(_translate("Bottlewindow", "200"))
        self.PBMminus8.setText(_translate("Bottlewindow", "-"))
        self.PBMminus7.setText(_translate("Bottlewindow", "-"))
        self.PBMplus7.setText(_translate("Bottlewindow", "+"))
        self.PBMplus2.setText(_translate("Bottlewindow", "+"))
        self.PBMminus6.setText(_translate("Bottlewindow", "-"))
        self.PBMplus3.setText(_translate("Bottlewindow", "+"))
        self.PBMplus6.setText(_translate("Bottlewindow", "+"))
        self.PBMplus5.setText(_translate("Bottlewindow", "+"))
        self.PBMplus4.setText(_translate("Bottlewindow", "+"))
        self.PBMplus9.setText(_translate("Bottlewindow", "+"))
        self.PBMplus8.setText(_translate("Bottlewindow", "+"))
        self.LAmount7.setText(_translate("Bottlewindow", "200"))
        self.PBMplus10.setText(_translate("Bottlewindow", "+"))
        self.LHeader.setText(_translate("Bottlewindow", "Füllstand der Flaschen auswählen/ändern"))
        self.PBEintragen.setText(_translate("Bottlewindow", "Eintragen"))
        self.PBAbbrechen.setText(_translate("Bottlewindow", "Abbrechen"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Bottlewindow = QtWidgets.QMainWindow()
    ui = Ui_Bottlewindow()
    ui.setupUi(Bottlewindow)
    Bottlewindow.show()
    sys.exit(app.exec_())
