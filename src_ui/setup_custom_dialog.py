from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QDialog

from ui_elements.customdialog import Ui_CustomDialog
from config.config_manager import ConfigManager
from src.display_controller import DP_CONTROLLER


class CustomDialog(QDialog, Ui_CustomDialog, ConfigManager):
    """ Class for the Team selection Screen. """

    def __init__(self, message: str, title: str = "Information", icon_path: str = None):
        super().__init__()
        ConfigManager.__init__(self)
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.informationLabel.setText(message)
        self.setWindowTitle(title)
        self.closeButton.clicked.connect(self.close_clicked)
        self.setWindowIcon(QIcon(icon_path))
        self.move(0, 0)
        DP_CONTROLLER.set_dev_settings(self)

    def close_clicked(self):
        self.close()
