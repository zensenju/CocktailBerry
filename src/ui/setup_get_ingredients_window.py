from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QDialog

from src.ui_elements.bonusingredient import Ui_addingredient
from src.config_manager import shared

from src.logger_handler import LoggerHandler
from src.display_controller import DP_CONTROLLER
from src.database_commander import DB_COMMANDER
from src.rpi_controller import MACHINE
from src.bottles import set_fill_level_bars
from src.dialog_handler import UI_LANGUAGE

LOG_HANDLER = LoggerHandler("additional_ingredient", "production_logs")


class GetIngredientWindow(QDialog, Ui_addingredient):
    """ Creates a Dialog to chose an additional ingredient and the amount
    to spend this ingredient.
    """

    def __init__(self, parent=None):
        """ Init. Connects all the buttons and get values for the Combobox. """
        super().__init__()
        self.setupUi(self)
        self.setWindowFlags(Qt.Window | Qt.CustomizeWindowHint | Qt.WindowStaysOnTopHint)
        # Set window properties
        self.setWindowIcon(QIcon(parent.icon_path))
        self.mainscreen = parent
        # Connect all the buttons
        self.PBplus.clicked.connect(lambda: DP_CONTROLLER.plusminus(self.LAmount, "+", 20, 100, 10))
        self.PBminus.clicked.connect(lambda: DP_CONTROLLER.plusminus(self.LAmount, "-", 20, 100, 10))
        self.PBAusgeben.clicked.connect(self.ausgeben_clicked)
        self.PBAbbrechen.clicked.connect(self.abbrechen_clicked)
        all_bottles = DB_COMMANDER.get_ingredients_at_bottles()
        bottles = [x for x in all_bottles if x != ""]
        DP_CONTROLLER.fill_single_combobox(self.CBingredient, bottles, first_empty=False)
        UI_LANGUAGE.adjust_bonusingredient_screen(self)
        self.showFullScreen()
        DP_CONTROLLER.set_display_settings(self)

    def abbrechen_clicked(self):
        """ Closes the Window without a change. """
        self.close()

    def ausgeben_clicked(self):
        """ Calls the Progressbarwindow and spends the given amount of the ingredient. """
        ingredient_name, volume = DP_CONTROLLER.get_ingredient_window_data(self)
        bottle, level = DB_COMMANDER.get_ingredient_bottle_and_level_by_name(ingredient_name)

        self.close()
        if volume > level:
            DP_CONTROLLER.say_not_enough_ingredient_volume(ingredient_name, level, volume)
            self.mainscreen.tabWidget.setCurrentIndex(3)
            return

        print(f"Spending {volume} ml {self.CBingredient.currentText()}")
        made_volume, _, _ = MACHINE.make_cocktail(self.mainscreen, [bottle], [volume], ingredient_name, False)
        DB_COMMANDER.increment_ingredient_consumption(ingredient_name, made_volume[0])
        set_fill_level_bars(self.mainscreen)
        volume_string = f"{volume} ml"
        LOG_HANDLER.log_event("INFO", f"{volume_string:6} | {ingredient_name}")
        self.mainscreen.prow_close()
        shared.cocktail_started = False
