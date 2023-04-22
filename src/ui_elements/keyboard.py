# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\keyboard.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Keyboard(object):
    def setupUi(self, Keyboard):
        Keyboard.setObjectName("Keyboard")
        Keyboard.resize(800, 480)
        Keyboard.setMinimumSize(QtCore.QSize(0, 480))
        Keyboard.setMaximumSize(QtCore.QSize(800, 480))
        Keyboard.setStyleSheet("")
        self.verticalLayout = QtWidgets.QVBoxLayout(Keyboard)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.LName = QtWidgets.QLineEdit(Keyboard)
        self.LName.setMinimumSize(QtCore.QSize(0, 70))
        self.LName.setMaximumSize(QtCore.QSize(16777215, 70))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.LName.setFont(font)
        self.LName.setObjectName("LName")
        self.horizontalLayout.addWidget(self.LName)
        self.clear = QtWidgets.QPushButton(Keyboard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clear.sizePolicy().hasHeightForWidth())
        self.clear.setSizePolicy(sizePolicy)
        self.clear.setMinimumSize(QtCore.QSize(155, 70))
        self.clear.setMaximumSize(QtCore.QSize(16777215, 70))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.clear.setFont(font)
        self.clear.setObjectName("clear")
        self.horizontalLayout.addWidget(self.clear)
        self.backButton = QtWidgets.QPushButton(Keyboard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.backButton.sizePolicy().hasHeightForWidth())
        self.backButton.setSizePolicy(sizePolicy)
        self.backButton.setMinimumSize(QtCore.QSize(155, 70))
        self.backButton.setMaximumSize(QtCore.QSize(16777215, 70))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.backButton.setFont(font)
        self.backButton.setObjectName("backButton")
        self.horizontalLayout.addWidget(self.backButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSpacing(2)
        self.gridLayout.setObjectName("gridLayout")
        self.Buttonq = QtWidgets.QPushButton(Keyboard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Buttonq.sizePolicy().hasHeightForWidth())
        self.Buttonq.setSizePolicy(sizePolicy)
        self.Buttonq.setMinimumSize(QtCore.QSize(20, 0))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.Buttonq.setFont(font)
        self.Buttonq.setObjectName("Buttonq")
        self.gridLayout.addWidget(self.Buttonq, 1, 0, 1, 1)
        self.Buttonw = QtWidgets.QPushButton(Keyboard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Buttonw.sizePolicy().hasHeightForWidth())
        self.Buttonw.setSizePolicy(sizePolicy)
        self.Buttonw.setMinimumSize(QtCore.QSize(20, 0))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.Buttonw.setFont(font)
        self.Buttonw.setObjectName("Buttonw")
        self.gridLayout.addWidget(self.Buttonw, 1, 1, 1, 1)
        self.Buttone = QtWidgets.QPushButton(Keyboard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Buttone.sizePolicy().hasHeightForWidth())
        self.Buttone.setSizePolicy(sizePolicy)
        self.Buttone.setMinimumSize(QtCore.QSize(20, 0))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.Buttone.setFont(font)
        self.Buttone.setObjectName("Buttone")
        self.gridLayout.addWidget(self.Buttone, 1, 2, 1, 1)
        self.Buttonr = QtWidgets.QPushButton(Keyboard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Buttonr.sizePolicy().hasHeightForWidth())
        self.Buttonr.setSizePolicy(sizePolicy)
        self.Buttonr.setMinimumSize(QtCore.QSize(20, 0))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.Buttonr.setFont(font)
        self.Buttonr.setObjectName("Buttonr")
        self.gridLayout.addWidget(self.Buttonr, 1, 3, 1, 1)
        self.Buttont = QtWidgets.QPushButton(Keyboard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Buttont.sizePolicy().hasHeightForWidth())
        self.Buttont.setSizePolicy(sizePolicy)
        self.Buttont.setMinimumSize(QtCore.QSize(20, 0))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.Buttont.setFont(font)
        self.Buttont.setObjectName("Buttont")
        self.gridLayout.addWidget(self.Buttont, 1, 4, 1, 1)
        self.Buttony = QtWidgets.QPushButton(Keyboard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Buttony.sizePolicy().hasHeightForWidth())
        self.Buttony.setSizePolicy(sizePolicy)
        self.Buttony.setMinimumSize(QtCore.QSize(20, 0))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.Buttony.setFont(font)
        self.Buttony.setObjectName("Buttony")
        self.gridLayout.addWidget(self.Buttony, 1, 5, 1, 1)
        self.Buttonu = QtWidgets.QPushButton(Keyboard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Buttonu.sizePolicy().hasHeightForWidth())
        self.Buttonu.setSizePolicy(sizePolicy)
        self.Buttonu.setMinimumSize(QtCore.QSize(20, 0))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.Buttonu.setFont(font)
        self.Buttonu.setObjectName("Buttonu")
        self.gridLayout.addWidget(self.Buttonu, 1, 6, 1, 1)
        self.Buttoni = QtWidgets.QPushButton(Keyboard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Buttoni.sizePolicy().hasHeightForWidth())
        self.Buttoni.setSizePolicy(sizePolicy)
        self.Buttoni.setMinimumSize(QtCore.QSize(20, 0))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.Buttoni.setFont(font)
        self.Buttoni.setObjectName("Buttoni")
        self.gridLayout.addWidget(self.Buttoni, 1, 7, 1, 1)
        self.Buttono = QtWidgets.QPushButton(Keyboard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Buttono.sizePolicy().hasHeightForWidth())
        self.Buttono.setSizePolicy(sizePolicy)
        self.Buttono.setMinimumSize(QtCore.QSize(20, 0))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.Buttono.setFont(font)
        self.Buttono.setObjectName("Buttono")
        self.gridLayout.addWidget(self.Buttono, 1, 8, 1, 1)
        self.Buttons = QtWidgets.QPushButton(Keyboard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Buttons.sizePolicy().hasHeightForWidth())
        self.Buttons.setSizePolicy(sizePolicy)
        self.Buttons.setMinimumSize(QtCore.QSize(20, 0))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.Buttons.setFont(font)
        self.Buttons.setObjectName("Buttons")
        self.gridLayout.addWidget(self.Buttons, 3, 1, 1, 1)
        self.Buttond = QtWidgets.QPushButton(Keyboard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Buttond.sizePolicy().hasHeightForWidth())
        self.Buttond.setSizePolicy(sizePolicy)
        self.Buttond.setMinimumSize(QtCore.QSize(20, 0))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.Buttond.setFont(font)
        self.Buttond.setObjectName("Buttond")
        self.gridLayout.addWidget(self.Buttond, 3, 2, 1, 1)
        self.Buttonf = QtWidgets.QPushButton(Keyboard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Buttonf.sizePolicy().hasHeightForWidth())
        self.Buttonf.setSizePolicy(sizePolicy)
        self.Buttonf.setMinimumSize(QtCore.QSize(20, 0))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.Buttonf.setFont(font)
        self.Buttonf.setObjectName("Buttonf")
        self.gridLayout.addWidget(self.Buttonf, 3, 3, 1, 1)
        self.Buttong = QtWidgets.QPushButton(Keyboard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Buttong.sizePolicy().hasHeightForWidth())
        self.Buttong.setSizePolicy(sizePolicy)
        self.Buttong.setMinimumSize(QtCore.QSize(20, 0))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.Buttong.setFont(font)
        self.Buttong.setObjectName("Buttong")
        self.gridLayout.addWidget(self.Buttong, 3, 4, 1, 1)
        self.Buttonh = QtWidgets.QPushButton(Keyboard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Buttonh.sizePolicy().hasHeightForWidth())
        self.Buttonh.setSizePolicy(sizePolicy)
        self.Buttonh.setMinimumSize(QtCore.QSize(20, 0))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.Buttonh.setFont(font)
        self.Buttonh.setObjectName("Buttonh")
        self.gridLayout.addWidget(self.Buttonh, 3, 5, 1, 1)
        self.Buttonj = QtWidgets.QPushButton(Keyboard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Buttonj.sizePolicy().hasHeightForWidth())
        self.Buttonj.setSizePolicy(sizePolicy)
        self.Buttonj.setMinimumSize(QtCore.QSize(20, 0))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.Buttonj.setFont(font)
        self.Buttonj.setObjectName("Buttonj")
        self.gridLayout.addWidget(self.Buttonj, 3, 6, 1, 1)
        self.Buttonl = QtWidgets.QPushButton(Keyboard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Buttonl.sizePolicy().hasHeightForWidth())
        self.Buttonl.setSizePolicy(sizePolicy)
        self.Buttonl.setMinimumSize(QtCore.QSize(20, 0))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.Buttonl.setFont(font)
        self.Buttonl.setObjectName("Buttonl")
        self.gridLayout.addWidget(self.Buttonl, 3, 8, 1, 1)
        self.Buttonz = QtWidgets.QPushButton(Keyboard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Buttonz.sizePolicy().hasHeightForWidth())
        self.Buttonz.setSizePolicy(sizePolicy)
        self.Buttonz.setMinimumSize(QtCore.QSize(20, 0))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.Buttonz.setFont(font)
        self.Buttonz.setObjectName("Buttonz")
        self.gridLayout.addWidget(self.Buttonz, 4, 1, 1, 1)
        self.Buttonx = QtWidgets.QPushButton(Keyboard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Buttonx.sizePolicy().hasHeightForWidth())
        self.Buttonx.setSizePolicy(sizePolicy)
        self.Buttonx.setMinimumSize(QtCore.QSize(20, 0))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.Buttonx.setFont(font)
        self.Buttonx.setObjectName("Buttonx")
        self.gridLayout.addWidget(self.Buttonx, 4, 2, 1, 1)
        self.Buttonv = QtWidgets.QPushButton(Keyboard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Buttonv.sizePolicy().hasHeightForWidth())
        self.Buttonv.setSizePolicy(sizePolicy)
        self.Buttonv.setMinimumSize(QtCore.QSize(20, 0))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.Buttonv.setFont(font)
        self.Buttonv.setObjectName("Buttonv")
        self.gridLayout.addWidget(self.Buttonv, 4, 4, 1, 1)
        self.Buttonb = QtWidgets.QPushButton(Keyboard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Buttonb.sizePolicy().hasHeightForWidth())
        self.Buttonb.setSizePolicy(sizePolicy)
        self.Buttonb.setMinimumSize(QtCore.QSize(20, 0))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.Buttonb.setFont(font)
        self.Buttonb.setObjectName("Buttonb")
        self.gridLayout.addWidget(self.Buttonb, 4, 5, 1, 1)
        self.Buttonn = QtWidgets.QPushButton(Keyboard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Buttonn.sizePolicy().hasHeightForWidth())
        self.Buttonn.setSizePolicy(sizePolicy)
        self.Buttonn.setMinimumSize(QtCore.QSize(20, 0))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.Buttonn.setFont(font)
        self.Buttonn.setObjectName("Buttonn")
        self.gridLayout.addWidget(self.Buttonn, 4, 6, 1, 1)
        self.Buttonm = QtWidgets.QPushButton(Keyboard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Buttonm.sizePolicy().hasHeightForWidth())
        self.Buttonm.setSizePolicy(sizePolicy)
        self.Buttonm.setMinimumSize(QtCore.QSize(20, 0))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.Buttonm.setFont(font)
        self.Buttonm.setObjectName("Buttonm")
        self.gridLayout.addWidget(self.Buttonm, 4, 7, 1, 1)
        self.delButton = QtWidgets.QPushButton(Keyboard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.delButton.sizePolicy().hasHeightForWidth())
        self.delButton.setSizePolicy(sizePolicy)
        self.delButton.setMinimumSize(QtCore.QSize(20, 0))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.delButton.setFont(font)
        self.delButton.setCheckable(False)
        self.delButton.setChecked(False)
        self.delButton.setObjectName("delButton")
        self.gridLayout.addWidget(self.delButton, 4, 8, 2, 1)
        self.space = QtWidgets.QPushButton(Keyboard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.space.sizePolicy().hasHeightForWidth())
        self.space.setSizePolicy(sizePolicy)
        self.space.setMinimumSize(QtCore.QSize(20, 0))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.space.setFont(font)
        self.space.setObjectName("space")
        self.gridLayout.addWidget(self.space, 5, 1, 1, 7)
        self.Button0 = QtWidgets.QPushButton(Keyboard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button0.sizePolicy().hasHeightForWidth())
        self.Button0.setSizePolicy(sizePolicy)
        self.Button0.setMinimumSize(QtCore.QSize(20, 0))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.Button0.setFont(font)
        self.Button0.setObjectName("Button0")
        self.gridLayout.addWidget(self.Button0, 0, 0, 1, 1)
        self.Button1 = QtWidgets.QPushButton(Keyboard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button1.sizePolicy().hasHeightForWidth())
        self.Button1.setSizePolicy(sizePolicy)
        self.Button1.setMinimumSize(QtCore.QSize(20, 0))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.Button1.setFont(font)
        self.Button1.setObjectName("Button1")
        self.gridLayout.addWidget(self.Button1, 0, 1, 1, 1)
        self.Button2 = QtWidgets.QPushButton(Keyboard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button2.sizePolicy().hasHeightForWidth())
        self.Button2.setSizePolicy(sizePolicy)
        self.Button2.setMinimumSize(QtCore.QSize(20, 0))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.Button2.setFont(font)
        self.Button2.setObjectName("Button2")
        self.gridLayout.addWidget(self.Button2, 0, 2, 1, 1)
        self.Button3 = QtWidgets.QPushButton(Keyboard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button3.sizePolicy().hasHeightForWidth())
        self.Button3.setSizePolicy(sizePolicy)
        self.Button3.setMinimumSize(QtCore.QSize(20, 0))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.Button3.setFont(font)
        self.Button3.setObjectName("Button3")
        self.gridLayout.addWidget(self.Button3, 0, 3, 1, 1)
        self.Button4 = QtWidgets.QPushButton(Keyboard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button4.sizePolicy().hasHeightForWidth())
        self.Button4.setSizePolicy(sizePolicy)
        self.Button4.setMinimumSize(QtCore.QSize(20, 0))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.Button4.setFont(font)
        self.Button4.setObjectName("Button4")
        self.gridLayout.addWidget(self.Button4, 0, 4, 1, 1)
        self.Button5 = QtWidgets.QPushButton(Keyboard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button5.sizePolicy().hasHeightForWidth())
        self.Button5.setSizePolicy(sizePolicy)
        self.Button5.setMinimumSize(QtCore.QSize(20, 0))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.Button5.setFont(font)
        self.Button5.setObjectName("Button5")
        self.gridLayout.addWidget(self.Button5, 0, 5, 1, 1)
        self.Button6 = QtWidgets.QPushButton(Keyboard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button6.sizePolicy().hasHeightForWidth())
        self.Button6.setSizePolicy(sizePolicy)
        self.Button6.setMinimumSize(QtCore.QSize(20, 0))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.Button6.setFont(font)
        self.Button6.setObjectName("Button6")
        self.gridLayout.addWidget(self.Button6, 0, 6, 1, 1)
        self.Button7 = QtWidgets.QPushButton(Keyboard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button7.sizePolicy().hasHeightForWidth())
        self.Button7.setSizePolicy(sizePolicy)
        self.Button7.setMinimumSize(QtCore.QSize(20, 0))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.Button7.setFont(font)
        self.Button7.setObjectName("Button7")
        self.gridLayout.addWidget(self.Button7, 0, 7, 1, 1)
        self.Button8 = QtWidgets.QPushButton(Keyboard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button8.sizePolicy().hasHeightForWidth())
        self.Button8.setSizePolicy(sizePolicy)
        self.Button8.setMinimumSize(QtCore.QSize(20, 0))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.Button8.setFont(font)
        self.Button8.setObjectName("Button8")
        self.gridLayout.addWidget(self.Button8, 0, 8, 1, 1)
        self.Button9 = QtWidgets.QPushButton(Keyboard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button9.sizePolicy().hasHeightForWidth())
        self.Button9.setSizePolicy(sizePolicy)
        self.Button9.setMinimumSize(QtCore.QSize(20, 0))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.Button9.setFont(font)
        self.Button9.setObjectName("Button9")
        self.gridLayout.addWidget(self.Button9, 0, 9, 1, 1)
        self.Buttonp = QtWidgets.QPushButton(Keyboard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Buttonp.sizePolicy().hasHeightForWidth())
        self.Buttonp.setSizePolicy(sizePolicy)
        self.Buttonp.setMinimumSize(QtCore.QSize(20, 0))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.Buttonp.setFont(font)
        self.Buttonp.setObjectName("Buttonp")
        self.gridLayout.addWidget(self.Buttonp, 1, 9, 1, 1)
        self.enterButton = QtWidgets.QPushButton(Keyboard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.enterButton.sizePolicy().hasHeightForWidth())
        self.enterButton.setSizePolicy(sizePolicy)
        self.enterButton.setMinimumSize(QtCore.QSize(20, 0))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.enterButton.setFont(font)
        self.enterButton.setObjectName("enterButton")
        self.gridLayout.addWidget(self.enterButton, 3, 9, 3, 1)
        self.Buttona = QtWidgets.QPushButton(Keyboard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Buttona.sizePolicy().hasHeightForWidth())
        self.Buttona.setSizePolicy(sizePolicy)
        self.Buttona.setMinimumSize(QtCore.QSize(20, 0))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.Buttona.setFont(font)
        self.Buttona.setObjectName("Buttona")
        self.gridLayout.addWidget(self.Buttona, 3, 0, 1, 1)
        self.Buttonc = QtWidgets.QPushButton(Keyboard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Buttonc.sizePolicy().hasHeightForWidth())
        self.Buttonc.setSizePolicy(sizePolicy)
        self.Buttonc.setMinimumSize(QtCore.QSize(20, 0))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.Buttonc.setFont(font)
        self.Buttonc.setObjectName("Buttonc")
        self.gridLayout.addWidget(self.Buttonc, 4, 3, 1, 1)
        self.Buttonk = QtWidgets.QPushButton(Keyboard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Buttonk.sizePolicy().hasHeightForWidth())
        self.Buttonk.setSizePolicy(sizePolicy)
        self.Buttonk.setMinimumSize(QtCore.QSize(20, 0))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.Buttonk.setFont(font)
        self.Buttonk.setObjectName("Buttonk")
        self.gridLayout.addWidget(self.Buttonk, 3, 7, 1, 1)
        self.shift = QtWidgets.QPushButton(Keyboard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.shift.sizePolicy().hasHeightForWidth())
        self.shift.setSizePolicy(sizePolicy)
        self.shift.setMinimumSize(QtCore.QSize(20, 0))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.shift.setFont(font)
        self.shift.setStyleSheet("")
        self.shift.setCheckable(True)
        self.shift.setObjectName("shift")
        self.gridLayout.addWidget(self.shift, 4, 0, 1, 1)
        self.button_control = QtWidgets.QPushButton(Keyboard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_control.sizePolicy().hasHeightForWidth())
        self.button_control.setSizePolicy(sizePolicy)
        self.button_control.setMinimumSize(QtCore.QSize(20, 0))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.button_control.setFont(font)
        self.button_control.setStyleSheet("")
        self.button_control.setCheckable(True)
        self.button_control.setObjectName("button_control")
        self.gridLayout.addWidget(self.button_control, 5, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)

        self.retranslateUi(Keyboard)
        QtCore.QMetaObject.connectSlotsByName(Keyboard)

    def retranslateUi(self, Keyboard):
        _translate = QtCore.QCoreApplication.translate
        Keyboard.setWindowTitle(_translate("Keyboard", "Zutatenname eingeben"))
        self.LName.setProperty("cssClass", _translate("Keyboard", "secondary"))
        self.clear.setText(_translate("Keyboard", "Clear"))
        self.backButton.setText(_translate("Keyboard", "Back"))
        self.Buttonq.setText(_translate("Keyboard", "q"))
        self.Buttonw.setText(_translate("Keyboard", "w"))
        self.Buttone.setText(_translate("Keyboard", "e"))
        self.Buttonr.setText(_translate("Keyboard", "r"))
        self.Buttont.setText(_translate("Keyboard", "t"))
        self.Buttony.setText(_translate("Keyboard", "y"))
        self.Buttonu.setText(_translate("Keyboard", "u"))
        self.Buttoni.setText(_translate("Keyboard", "i"))
        self.Buttono.setText(_translate("Keyboard", "o"))
        self.Buttons.setText(_translate("Keyboard", "s"))
        self.Buttond.setText(_translate("Keyboard", "d"))
        self.Buttonf.setText(_translate("Keyboard", "f"))
        self.Buttong.setText(_translate("Keyboard", "g"))
        self.Buttonh.setText(_translate("Keyboard", "h"))
        self.Buttonj.setText(_translate("Keyboard", "j"))
        self.Buttonl.setText(_translate("Keyboard", "l"))
        self.Buttonz.setText(_translate("Keyboard", "z"))
        self.Buttonx.setText(_translate("Keyboard", "x"))
        self.Buttonv.setText(_translate("Keyboard", "v"))
        self.Buttonb.setText(_translate("Keyboard", "b"))
        self.Buttonn.setText(_translate("Keyboard", "n"))
        self.Buttonm.setText(_translate("Keyboard", "m"))
        self.delButton.setText(_translate("Keyboard", "del"))
        self.space.setText(_translate("Keyboard", "Space"))
        self.Button0.setText(_translate("Keyboard", "0"))
        self.Button1.setText(_translate("Keyboard", "1"))
        self.Button2.setText(_translate("Keyboard", "2"))
        self.Button3.setText(_translate("Keyboard", "3"))
        self.Button4.setText(_translate("Keyboard", "4"))
        self.Button5.setText(_translate("Keyboard", "5"))
        self.Button6.setText(_translate("Keyboard", "6"))
        self.Button7.setText(_translate("Keyboard", "7"))
        self.Button8.setText(_translate("Keyboard", "8"))
        self.Button9.setText(_translate("Keyboard", "9"))
        self.Buttonp.setText(_translate("Keyboard", "p"))
        self.enterButton.setText(_translate("Keyboard", "Enter"))
        self.enterButton.setProperty("cssClass", _translate("Keyboard", "btn-inverted"))
        self.Buttona.setText(_translate("Keyboard", "a"))
        self.Buttonc.setText(_translate("Keyboard", "c"))
        self.Buttonk.setText(_translate("Keyboard", "k"))
        self.shift.setText(_translate("Keyboard", "Shift"))
        self.button_control.setText(_translate("Keyboard", "ctrl"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Keyboard = QtWidgets.QDialog()
    ui = Ui_Keyboard()
    ui.setupUi(Keyboard)
    Keyboard.show()
    sys.exit(app.exec_())
