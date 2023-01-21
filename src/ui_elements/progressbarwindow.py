# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\progressbarwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Progressbarwindow(object):
    def setupUi(self, Progressbarwindow):
        Progressbarwindow.setObjectName("Progressbarwindow")
        Progressbarwindow.resize(800, 480)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Progressbarwindow.sizePolicy().hasHeightForWidth())
        Progressbarwindow.setSizePolicy(sizePolicy)
        Progressbarwindow.setMinimumSize(QtCore.QSize(800, 480))
        Progressbarwindow.setMaximumSize(QtCore.QSize(800, 480))
        Progressbarwindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        Progressbarwindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(Progressbarwindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.LHeader = QtWidgets.QLabel(self.centralwidget)
        self.LHeader.setMinimumSize(QtCore.QSize(0, 100))
        self.LHeader.setMaximumSize(QtCore.QSize(16777215, 200))
        font = QtGui.QFont()
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.LHeader.setFont(font)
        self.LHeader.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.LHeader.setWordWrap(True)
        self.LHeader.setObjectName("LHeader")
        self.verticalLayout.addWidget(self.LHeader)
        self.LProgress = QtWidgets.QLabel(self.centralwidget)
        self.LProgress.setMinimumSize(QtCore.QSize(0, 50))
        self.LProgress.setMaximumSize(QtCore.QSize(16777215, 60))
        font = QtGui.QFont()
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)
        self.LProgress.setFont(font)
        self.LProgress.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.LProgress.setObjectName("LProgress")
        self.verticalLayout.addWidget(self.LProgress)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setMaximumSize(QtCore.QSize(16777215, 300))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setTextVisible(False)
        self.progressBar.setOrientation(QtCore.Qt.Horizontal)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)
        self.Labbruch = QtWidgets.QLabel(self.centralwidget)
        self.Labbruch.setMaximumSize(QtCore.QSize(16777215, 200))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.Labbruch.setFont(font)
        self.Labbruch.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.Labbruch.setObjectName("Labbruch")
        self.verticalLayout.addWidget(self.Labbruch)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(140, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.PBabbrechen = QtWidgets.QPushButton(self.centralwidget)
        self.PBabbrechen.setMinimumSize(QtCore.QSize(450, 100))
        self.PBabbrechen.setMaximumSize(QtCore.QSize(2000, 200))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.PBabbrechen.setFont(font)
        self.PBabbrechen.setObjectName("PBabbrechen")
        self.horizontalLayout.addWidget(self.PBabbrechen)
        spacerItem1 = QtWidgets.QSpacerItem(140, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        Progressbarwindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(Progressbarwindow)
        QtCore.QMetaObject.connectSlotsByName(Progressbarwindow)

    def retranslateUi(self, Progressbarwindow):
        _translate = QtCore.QCoreApplication.translate
        Progressbarwindow.setWindowTitle(_translate("Progressbarwindow", "~~ Cocktail wird zubereitet ~~"))
        self.LHeader.setText(_translate("Progressbarwindow", "Cocktailname very long"))
        self.LHeader.setProperty("cssClass", _translate("Progressbarwindow", "bold"))
        self.LProgress.setText(_translate("Progressbarwindow", "Progress"))
        self.LProgress.setProperty("cssClass", _translate("Progressbarwindow", "secondary bold"))
        self.progressBar.setFormat(_translate("Progressbarwindow", "%p%"))
        self.progressBar.setProperty("cssClass", _translate("Progressbarwindow", "bold"))
        self.Labbruch.setText(_translate("Progressbarwindow", "Der Vorgang kann auch abgebrochen werden"))
        self.Labbruch.setProperty("cssClass", _translate("Progressbarwindow", "secondary bold"))
        self.PBabbrechen.setText(_translate("Progressbarwindow", "Abbrechen"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Progressbarwindow = QtWidgets.QMainWindow()
    ui = Ui_Progressbarwindow()
    ui.setupUi(Progressbarwindow)
    Progressbarwindow.show()
    sys.exit(app.exec_())
