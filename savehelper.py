import sys
import sqlite3
import time
import datetime
import csv
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import *

import globals
from msgboxgenerate import standartbox

def save_quant(w, DB, c, wobject_name, filename, dbstring, searchstring1, searchstring2):
    """ Saves all the amounts of the incredients/recipes to a csv. 
    after that sets the variable incredient/recipes counter to zero.
    Needs the password for that procedure.
    """
    wobject = getattr(w, wobject_name)
    if wobject.text() == globals.masterpassword:
        with open(filename, mode='a', newline='') as writer_file:
            csv_writer = csv.writer(writer_file, delimiter=',')
            csv_writer.writerow(
                ["----- Neuer Export von %s -----" % datetime.date.today()])
            row1 = []
            row2 = []
            # selects the actual use and the names and writes them
            sqlstring = "SELECT Name, {0} FROM {1} ORDER BY {0} DESC, Name ASC".format(
                searchstring1, dbstring)
            Zspeicher = c.execute(sqlstring)
            for row in Zspeicher:
                row1.append(row[0])
                row2.append(row[1])
            csv_writer.writerow(row1)
            csv_writer.writerow(row2)
            csv_writer.writerow(["----- Gesamte Mengen über Lebenszeit -----"])
            row1 = []
            row2 = []
            # selects the life time use and saves them
            sqlstring = "SELECT Name, {0} FROM {1} ORDER BY {0} DESC, Name ASC".format(
                searchstring2, dbstring)
            Zspeicher = c.execute(sqlstring)
            for row in Zspeicher:
                row1.append(row[0])
                row2.append(row[1])
            csv_writer.writerow(row1)
            csv_writer.writerow(row2)
            csv_writer.writerow([" "])
        sqlstring = "UPDATE OR IGNORE {} SET {} = 0".format(dbstring, searchstring1)
        c.execute(sqlstring)
        DB.commit()
        standartbox(
            "Alle Daten wurden exportiert und die zurücksetzbaren Mengen zurückgesetzt!")
    else:
        standartbox("Falsches Passwort!")
    wobject.setText("")