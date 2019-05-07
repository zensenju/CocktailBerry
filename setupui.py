""" Connects all the functions to the Buttons as well the Lists 
of the passed window. Also defines the Mode for controls. 
"""
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import *

import globals
from maker import *
from incredients import *
from recipes import *
from bottles import *

from Cocktailmanager_2 import Ui_MainWindow
from passwordbuttons import Ui_PasswordWindow


class MainScreen(QMainWindow, Ui_MainWindow):
    """ Creates the Mainscreen. """

    def __init__(self, parent=None):
        super(MainScreen, self).__init__(parent)
        self.setupUi(self)
        self.LEpw.selectionChanged.connect(lambda: self.passwordwindow(1))
        self.LEpw2.selectionChanged.connect(lambda: self.passwordwindow(2))

    def passwordwindow(self, register):
        """ Opens up the PasswordScreen. """
        # pw = PasswordScreen(self)
        if register == 1:
            if not hasattr(self, "pw1"):
                self.pw1 = PasswordScreen(self)
            self.pw1.show()
        elif register == 2:
            if not hasattr(self, "pw2"):
                self.pw2 = PasswordScreen2(self)
            self.pw2.show()


class PasswordScreen(QMainWindow, Ui_PasswordWindow):
    """ Creates the Passwordscreen (Rezepte). """

    def __init__(self, parent=None):
        super(PasswordScreen, self).__init__(parent)
        # self.setAttribute(Qt.WA_DeleteOnClose)
        self.setupUi(self)
        self.setWindowFlag(Qt.WindowMinimizeButtonHint, False)
        # self.setWindowFlags(Qt.FramelessWindowHint)
        self.PB0.clicked.connect(lambda: self.number_clicked(0))
        self.PB1.clicked.connect(lambda: self.number_clicked(1))
        self.PB2.clicked.connect(lambda: self.number_clicked(2))
        self.PB3.clicked.connect(lambda: self.number_clicked(3))
        self.PB4.clicked.connect(lambda: self.number_clicked(4))
        self.PB5.clicked.connect(lambda: self.number_clicked(5))
        self.PB6.clicked.connect(lambda: self.number_clicked(6))
        self.PB7.clicked.connect(lambda: self.number_clicked(7))
        self.PB8.clicked.connect(lambda: self.number_clicked(8))
        self.PB9.clicked.connect(lambda: self.number_clicked(9))
        self.PBenter.clicked.connect(self.enter_clicked)
        self.PBdel.clicked.connect(self.del_clicked)
        self.ms = parent

    def number_clicked(self, number):
        # print(number)
        self.ms.LEpw.setText(self.ms.LEpw.text() + "{}".format(number))

    def enter_clicked(self):
        # print("enter")
        self.close()

    def del_clicked(self):
        if len(self.ms.LEpw.text()) > 0:
            # print("del")
            strstor = str(self.ms.LEpw.text())
            self.ms.LEpw.setText(strstor[:-1])


class PasswordScreen2(QMainWindow, Ui_PasswordWindow):
    """ Creates the Passwordscreen2 (Zutaten). """

    def __init__(self, parent=None):
        super(PasswordScreen2, self).__init__(parent)
        # self.setAttribute(Qt.WA_DeleteOnClose)
        self.setupUi(self)
        # self.setWindowFlag(Qt.WindowCloseButtonHint, False)
        self.setWindowFlag(Qt.WindowMinimizeButtonHint, False)
        # self.setWindowFlags(Qt.FramelessWindowHint)
        self.PB0.clicked.connect(lambda: self.number_clicked(0))
        self.PB1.clicked.connect(lambda: self.number_clicked(1))
        self.PB2.clicked.connect(lambda: self.number_clicked(2))
        self.PB3.clicked.connect(lambda: self.number_clicked(3))
        self.PB4.clicked.connect(lambda: self.number_clicked(4))
        self.PB5.clicked.connect(lambda: self.number_clicked(5))
        self.PB6.clicked.connect(lambda: self.number_clicked(6))
        self.PB7.clicked.connect(lambda: self.number_clicked(7))
        self.PB8.clicked.connect(lambda: self.number_clicked(8))
        self.PB9.clicked.connect(lambda: self.number_clicked(9))
        self.PBenter.clicked.connect(self.enter_clicked)
        self.PBdel.clicked.connect(self.del_clicked)
        self.ms = parent

    def number_clicked(self, number):
        # print(number)
        self.ms.LEpw2.setText(self.ms.LEpw2.text() + "{}".format(number))

    def enter_clicked(self):
        # print("enter")
        self.close()

    def del_clicked(self):
        if len(self.ms.LEpw2.text()) > 0:
            # print("del")
            strstor = str(self.ms.LEpw2.text())
            self.ms.LEpw2.setText(strstor[:-1])


def pass_setup(w, DB, c, partymode, devenvironment):
    """ Connect all the functions with the Buttons. """
    w.PBZutathinzu.clicked.connect(lambda: Zutat_eintragen(w, DB, c))
    w.PBRezepthinzu.clicked.connect(lambda: Rezept_eintragen(w, DB, c))
    w.PBBelegung.clicked.connect(lambda: Belegung_eintragen(w, DB, c))
    w.PBclear.clicked.connect(lambda: Rezepte_clear(w, DB, c, True))
    w.PBRezeptaktualisieren.clicked.connect(lambda: Rezept_aktualisieren(w, DB, c))
    w.PBdelete.clicked.connect(lambda: Rezepte_delete(w, DB, c))
    w.PBZdelete.clicked.connect(lambda: Zutaten_delete(w, DB, c))
    w.PBZclear.clicked.connect(lambda: Zutaten_clear(w, DB, c))
    w.PBZaktualisieren.clicked.connect(Zutaten_aktualiesieren)
    w.PBZubereiten.clicked.connect(lambda: Maker_Zubereiten(w, DB, c, True, devenvironment))
    w.PBZubereiten_custom.clicked.connect(lambda: Maker_Zubereiten(w, DB, c, False, devenvironment))
    w.PBabbrechen.clicked.connect(lambda: abbrechen_R(w, DB, c))
    w.PBCleanMachine.clicked.connect(lambda: CleanMachine(w, DB, c, devenvironment))
    w.PBFlanwenden.clicked.connect(lambda: Belegung_Flanwenden(w, DB, c))
    w.PBZplus.clicked.connect(lambda: Zutaten_Flvolumen_pm(w, DB, c, "+"))
    w.PBZminus.clicked.connect(lambda: Zutaten_Flvolumen_pm(w, DB, c, "-"))
    w.PBMplus.clicked.connect(lambda: Maker_pm(w, DB, c, "+"))
    w.PBMminus.clicked.connect(lambda: Maker_pm(w, DB, c, "-"))
    w.PBSetnull.clicked.connect(lambda: Maker_nullProB(w, DB, c))
    w.PBZnull.clicked.connect(lambda: save_Zutaten(w, DB, c))
    w.PBRnull.clicked.connect(lambda: save_Rezepte(w, DB, c))

    # w.LEpw2.selectionChanged.connect(lambda: passwordwindow(w,))

    # Connect the Functions with the Lists
    w.LWZutaten.itemClicked.connect(lambda: Zutaten_Zutaten_click(w, DB, c))
    w.LWMaker.itemClicked.connect(lambda: Maker_Rezepte_click(w, DB, c))
    w.LWRezepte.itemClicked.connect(lambda: Rezepte_Rezepte_click(w, DB, c))

    # Disable some of the Tabs (for the Partymode)
    if partymode:
        w.tabWidget.setTabEnabled(2, False)

    # Clear Help Marker
    Maker_List_null(w, DB, c)
    # Load Incredients
    Zutaten_a(w, DB, c)
    # Load Bottles into the Labels
    Belegung_a(w, DB, c)
    # Load Combobuttons Recipes
    ZutatenCB_Rezepte(w, DB, c)
    # Load Combobuttons Bottles
    ZutatenCB_Belegung(w, DB, c)
    # Load current Bottles into the Combobuttons
    Belegung_einlesen(w, DB, c)
    # Load Existing Recipes from DB into Recipe List
    Rezepte_a_R(w, DB, c)
    # Load Possible Recipes Into Maker List
    Rezepte_a_M(w, DB, c)
    # Load the Progressbar
    Belegung_progressbar(w, DB, c)
