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
from ingredients import *
from recipes import *
from bottles import *

from Cocktailmanager_2 import Ui_MainWindow
from passwordbuttons import Ui_PasswordWindow
from passwordbuttons2 import Ui_PasswordWindow2
from progressbarwindow import Ui_Progressbarwindow
from bottlewindow import Ui_Bottlewindow
from savehelper import save_quant


class MainScreen(QMainWindow, Ui_MainWindow):
    """ Creates the Mainscreen. """

    def __init__(self, devenvironment, parent=None):
        """ Init. Many of the button and List connects are in pass_setup. """
        super(MainScreen, self).__init__(parent)
        self.setupUi(self)
        self.LEpw.selectionChanged.connect(lambda: self.passwordwindow(1))
        self.LEpw2.selectionChanged.connect(lambda: self.passwordwindow(2))
        self.LECleanMachine.selectionChanged.connect(lambda: self.passwordwindow(3))
        if not devenvironment:
            self.setCursor(Qt.BlankCursor)
        self.devenvironment = devenvironment

    def passwordwindow(self, register):
        """ Opens up the PasswordScreen. """
        # Since there are three different passwortlabels, it exists a window for each
        if register == 1:
            self.register = 1
            if not hasattr(self, "pw1"):
                self.pw1 = PasswordScreen(self)
            self.pw1.showMaximized()
        elif register == 2:
            self.register = 2
            if not hasattr(self, "pw2"):
                self.pw2 = PasswordScreen(self)
            self.pw2.showMaximized()
        elif register == 3:
            self.register = 3
            if not hasattr(self, "pw3"):
                self.pw3 = PasswordScreen(self)
            self.pw3.showMaximized()

    def progressionqwindow(self):
        """ Opens up the progressionwindow to show the Cocktail status. """
        self.prow = Progressscreen(self)
        self.prow.show()

    def prow_change(self, pbvalue):
        """ Changes the value of the Progressionbar of the ProBarWindow. """
        self.prow.progressBar.setValue(pbvalue)

    def prow_close(self):
        """ Closes the Progressionwindow at the end of the cyclus. """
        self.prow.close()

    def bottleswindow(self, bot_names=[], vol_values=[]):
        self.botw = Bottlewindow(self)
        self.botw.show()


class Progressscreen(QMainWindow, Ui_Progressbarwindow):
    """ Class for the Progressscreen during Cocktail making. """

    def __init__(self, parent=None):
        super(Progressscreen, self).__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.PBabbrechen.clicked.connect(lambda: abbrechen_R())
        self.setWindowIcon(QIcon("Cocktail-icon.png"))
        self.ms = parent


class PasswordScreen(QDialog, Ui_PasswordWindow2):
    """ Creates the Passwordscreen. """

    def __init__(self, parent=None):
        super(PasswordScreen, self).__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(
            Qt.Window |
            Qt.CustomizeWindowHint |
            Qt.WindowTitleHint |
            Qt.WindowCloseButtonHint |
            Qt.WindowStaysOnTopHint
            )
        self.setWindowIcon(QIcon("Cocktail-icon.png"))
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
        # decides in which window the numbers are entered
        if self.ms.register == 1:
            self.pwlineedit = self.ms.LEpw
        elif self.ms.register == 2:
            self.pwlineedit = self.ms.LEpw2
        elif self.ms.register == 3:
            self.pwlineedit = self.ms.LECleanMachine

    def number_clicked(self, number):
        self.pwlineedit.setText(self.pwlineedit.text() + "{}".format(number))

    def enter_clicked(self):
        self.close()

    def del_clicked(self):
        if len(self.pwlineedit.text()) > 0:
            strstor = str(self.pwlineedit.text())
            self.pwlineedit.setText(strstor[:-1])


class Bottlewindow(QMainWindow, Ui_Bottlewindow):
    """ Creates the Window to change to levels of the bottles. """

    def __init__(self, parent=None):
        super(Bottlewindow, self).__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)

        self.PBAbbrechen.clicked.connect(self.abbrechen_clicked)
        self.PBEintragen.clicked.connect(self.eintragen_clicked)

        myplus =  [
            self.PBMplus1, self.PBMplus2, self.PBMplus3, self.PBMplus4, self.PBMplus5,
            self.PBMplus6, self.PBMplus7, self.PBMplus8, self.PBMplus9, self.PBMplus10
        ]
        myminus =  [
            self.PBMminus1, self.PBMminus2, self.PBMminus3, self.PBMminus4, self.PBMminus5,
            self.PBMminus6, self.PBMminus7, self.PBMminus8, self.PBMminus9, self.PBMminus10
        ]
        mylabel = [
            self.LAmount1, self.LAmount2, self.LAmount3, self.LAmount4, self.LAmount5,
            self.LAmount6, self.LAmount7, self.LAmount8, self.LAmount9, self.LAmount10
        ]

        for plus, minus, field in zip(myplus, myminus, mylabel):
            plus.clicked.connect(lambda _, l=field: self.plusminus(label=l, operator='+'))
            minus.clicked.connect(lambda _, l=field: self.plusminus(label=l, operator='-'))

        self.ms = parent
        for i in range(1,11):
            CBBname = getattr(self.ms, "CBB" + str(i))
            labelobj = getattr(self, 'LName' + str(i))
            labelobj.setText('    ' + CBBname.currentText())
        
        
    def abbrechen_clicked(self):
        self.close()

    def eintragen_clicked(self):
        self.close()
    
    def plusminus(self, label, operator):
        minimal = 100
        maximal = 1500
        dm = 25
        amount = int(label.text())
        if operator == "+" and amount < maximal:
            amount += dm
        if operator == "-" and amount > minimal:
            amount -= dm
        label.setText(str(amount))


def pass_setup(w, DB, c, partymode, devenvironment):
    """ Connect all the functions with the Buttons. """
    # First, connect all the Pushbuttons with the Functions
    w.PBZutathinzu.clicked.connect(lambda: Zutat_eintragen(w, DB, c))
    w.PBRezepthinzu.clicked.connect(lambda: Rezept_eintragen(w, DB, c, True))
    # w.PBBelegung.clicked.connect(lambda: Belegung_eintragen(w, DB, c, True))
    w.PBBelegung.clicked.connect(lambda: customlevels(w, DB, c))
    w.PBclear.clicked.connect(lambda: Rezepte_clear(w, DB, c, True))
    w.PBRezeptaktualisieren.clicked.connect(lambda: Rezept_eintragen(w, DB, c, False))
    w.PBdelete.clicked.connect(lambda: Rezepte_delete(w, DB, c))
    w.PBZdelete.clicked.connect(lambda: Zutaten_delete(w, DB, c))
    w.PBZclear.clicked.connect(lambda: Zutaten_clear(w, DB, c))
    w.PBZaktualisieren.clicked.connect(lambda: Zutat_eintragen(w, DB, c, False))
    w.PBZubereiten_custom.clicked.connect(lambda: Maker_Zubereiten(w, DB, c, False, devenvironment))
    w.PBCleanMachine.clicked.connect(lambda: CleanMachine(w, DB, c, devenvironment))
    w.PBFlanwenden.clicked.connect(lambda: Belegung_Flanwenden(w, DB, c))
    w.PBZplus.clicked.connect(lambda: Zutaten_Flvolumen_pm(w, DB, c, "+"))
    w.PBZminus.clicked.connect(lambda: Zutaten_Flvolumen_pm(w, DB, c, "-"))
    w.PBMplus.clicked.connect(lambda: Maker_pm(w, DB, c, "+"))
    w.PBMminus.clicked.connect(lambda: Maker_pm(w, DB, c, "-"))
    w.PBSetnull.clicked.connect(lambda: Maker_nullProB(w, DB, c))
    w.PBZnull.clicked.connect(lambda: save_quant(w, DB, c, "LEpw2", 'Zutaten_export.csv', "Zutaten", "Verbrauch", "Verbrauchsmenge"))
    w.PBRnull.clicked.connect(lambda: save_quant(w, DB, c, "LEpw", 'Rezepte_export.csv', "Rezepte", "Anzahl", "Anzahl_Lifetime", True))
    w.PBenable.clicked.connect(lambda: enableall(w, DB, c))

    # Connect the Lists with the Functions
    w.LWZutaten.itemClicked.connect(lambda: Zutaten_Zutaten_click(w, DB, c))
    w.LWMaker.itemClicked.connect(lambda: Maker_Rezepte_click(w, DB, c))
    w.LWRezepte.itemClicked.connect(lambda: Rezepte_Rezepte_click(w, DB, c))
    w.LWZutaten.currentTextChanged.connect(lambda: Zutaten_Zutaten_click(w, DB, c))
    w.LWMaker.currentTextChanged.connect(lambda: Maker_Rezepte_click(w, DB, c))
    w.LWRezepte.currentTextChanged.connect(lambda: Rezepte_Rezepte_click(w, DB, c))

    # Connects the slider
    w.HSIntensity.valueChanged.connect(lambda: Maker_ProB_change(w, DB, c))

    # Disable some of the Tabs (for the Partymode, no one can access the recipes)
    if partymode:
        w.tabWidget.setTabEnabled(2, False)

    # gets the bottle ingredients into the global list
    get_bottle_ingredients(w, DB, c)
    # Clear Help Marker
    Maker_List_null(w, DB, c)
    # Load ingredients
    Zutaten_a(w, DB, c)
    # Load Bottles into the Labels
    Belegung_a(w, DB, c)
    # Load Combobuttons Recipes
    ZutatenCB_Rezepte(w, DB, c)
    # Load Combobuttons Bottles
    newCB_Bottles(w, DB,c)
    # Load current Bottles into the Combobuttons
    Belegung_einlesen(w, DB, c)
    # Load Existing Recipes from DB into Recipe List
    Rezepte_a_R(w, DB, c)
    # Load Possible Recipes Into Maker List
    Rezepte_a_M(w, DB, c)
    # Load the Progressbar
    Belegung_progressbar(w, DB, c)

    # Connects additional Functionality to the Comboboxes
    w.CBB1.currentIndexChanged.connect(lambda: refresh_bottle_cb(w, DB, c))
    w.CBB2.currentIndexChanged.connect(lambda: refresh_bottle_cb(w, DB, c))
    w.CBB3.currentIndexChanged.connect(lambda: refresh_bottle_cb(w, DB, c))
    w.CBB4.currentIndexChanged.connect(lambda: refresh_bottle_cb(w, DB, c))
    w.CBB5.currentIndexChanged.connect(lambda: refresh_bottle_cb(w, DB, c))
    w.CBB6.currentIndexChanged.connect(lambda: refresh_bottle_cb(w, DB, c))
    w.CBB7.currentIndexChanged.connect(lambda: refresh_bottle_cb(w, DB, c))
    w.CBB8.currentIndexChanged.connect(lambda: refresh_bottle_cb(w, DB, c))
    w.CBB9.currentIndexChanged.connect(lambda: refresh_bottle_cb(w, DB, c))
    w.CBB10.currentIndexChanged.connect(lambda: refresh_bottle_cb(w, DB, c))
