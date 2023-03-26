# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\addonmanager.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AddonManager(object):
    def setupUi(self, AddonManager):
        AddonManager.setObjectName("AddonManager")
        AddonManager.resize(800, 480)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(AddonManager.sizePolicy().hasHeightForWidth())
        AddonManager.setSizePolicy(sizePolicy)
        AddonManager.setMinimumSize(QtCore.QSize(800, 480))
        AddonManager.setMaximumSize(QtCore.QSize(800, 480))
        AddonManager.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        AddonManager.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(AddonManager)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setFrameShadow(QtWidgets.QFrame.Plain)
        self.scrollArea.setLineWidth(1)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 782, 384))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.addon_container = QtWidgets.QVBoxLayout()
        self.addon_container.setObjectName("addon_container")
        self.table_addons = QtWidgets.QTableWidget(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.table_addons.setFont(font)
        self.table_addons.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.table_addons.setDragDropOverwriteMode(True)
        self.table_addons.setObjectName("table_addons")
        self.table_addons.setColumnCount(0)
        self.table_addons.setRowCount(0)
        self.addon_container.addWidget(self.table_addons)
        self.gridLayout_2.addLayout(self.addon_container, 0, 0, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_2)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 4, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.button_back = QtWidgets.QPushButton(self.centralwidget)
        self.button_back.setMinimumSize(QtCore.QSize(0, 70))
        self.button_back.setMaximumSize(QtCore.QSize(5000, 100))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.button_back.setFont(font)
        self.button_back.setProperty("cssClass", "")
        self.button_back.setObjectName("button_back")
        self.horizontalLayout.addWidget(self.button_back)
        self.button_apply = QtWidgets.QPushButton(self.centralwidget)
        self.button_apply.setMinimumSize(QtCore.QSize(0, 70))
        self.button_apply.setMaximumSize(QtCore.QSize(5000, 100))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.button_apply.setFont(font)
        self.button_apply.setObjectName("button_apply")
        self.horizontalLayout.addWidget(self.button_apply)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        AddonManager.setCentralWidget(self.centralwidget)

        self.retranslateUi(AddonManager)
        QtCore.QMetaObject.connectSlotsByName(AddonManager)

    def retranslateUi(self, AddonManager):
        _translate = QtCore.QCoreApplication.translate
        AddonManager.setWindowTitle(_translate("AddonManager", "Addons Options"))
        self.table_addons.setSortingEnabled(True)
        self.button_back.setText(_translate("AddonManager", "< Back"))
        self.button_apply.setText(_translate("AddonManager", "Apply"))
        self.button_apply.setProperty("cssClass", _translate("AddonManager", "btn-inverted"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AddonManager = QtWidgets.QMainWindow()
    ui = Ui_AddonManager()
    ui.setupUi(AddonManager)
    AddonManager.show()
    sys.exit(app.exec_())
