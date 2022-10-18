from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QDialog, QLineEdit

from src.display_controller import DP_CONTROLLER
from src.ui_elements.passwordbuttons import Ui_PasswordWindow


class PasswordScreen(QDialog, Ui_PasswordWindow):
    """ Creates the Passwordscreen. """

    def __init__(self, parent, le_to_write: QLineEdit, x_pos: int = 0, y_pos: int = 0, headertext: str = "Password", use_float=False):
        """ Init. Connect all the buttons and set window policy. """
        super().__init__()
        self.setupUi(self)
        self.setWindowFlags(Qt.Window | Qt.CustomizeWindowHint | Qt.WindowStaysOnTopHint)  # type: ignore
        self.setAttribute(Qt.WA_DeleteOnClose)  # type: ignore
        DP_CONTROLLER.inject_stylesheet(self)
        self.setWindowIcon(QIcon(parent.icon_path))
        # Connect all the buttons, generates a list of the numbers an objectnames to do that
        self.PBenter.clicked.connect(self.enter_clicked)
        self.PBdel.clicked.connect(self.del_clicked)
        self.number_list = list(range(10))
        self.attribute_numbers = [getattr(self, "PB" + str(x)) for x in self.number_list]
        for obj, number in zip(self.attribute_numbers, self.number_list):
            obj.clicked.connect(lambda _, n=number: self.number_clicked(number=n))
        self.mainscreen = parent
        self.setWindowTitle(headertext)
        self.LHeader.setText(headertext)
        self.pwlineedit = le_to_write
        self._add_float(use_float)
        self.move(x_pos, y_pos)
        self.show()
        DP_CONTROLLER.set_display_settings(self, resize=False)

    def number_clicked(self, number: int):
        """  Adds the clicked number to the lineedit. """
        self.pwlineedit.setText(f"{self.pwlineedit.text()}{number}")

    def enter_clicked(self):
        """ Enters/Closes the Dialog. """
        self.close()

    def del_clicked(self):
        """ Deletes the last digit in the lineedit. """
        strstor = self.pwlineedit.text()
        self.pwlineedit.setText(strstor[:-1])

    def _add_float(self, use_float: bool):
        if not use_float:
            self.PBdot.deleteLater()
            return
        self.PBdot.clicked.connect(self._dot_clicked)

    def _dot_clicked(self):
        """Adds a dot if its not the first letter or a dot already exists"""
        strstor = self.pwlineedit.text()
        if "." in strstor or len(strstor) == 0:
            return
        self.pwlineedit.setText(f"{self.pwlineedit.text()}.")
