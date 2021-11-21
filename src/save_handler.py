import os
import datetime
import csv

from src.database_commander import DB_COMMANDER
from src.display_controller import DP_CONTROLLER
from src.service_handler import SERVICE_HANDLER

DIRPATH = os.path.dirname(os.path.abspath(__file__))


class SaveHandler:
    def export_ingredients(self, w):
        if not DP_CONTROLLER.check_ingredient_password(w):
            DP_CONTROLLER.say_wrong_password()
            return
        consumption_list = DB_COMMANDER.get_consumption_data_lists_ingredients()
        self.save_quant("Zutaten_export.csv", consumption_list)
        DB_COMMANDER.delete_consumption_ingredients()

    def export_recipes(self, w):
        if not DP_CONTROLLER.check_recipe_password(w):
            DP_CONTROLLER.say_wrong_password()
            return
        consumption_list = DB_COMMANDER.get_consumption_data_lists_recipes()
        self.save_quant("Rezepte_export.csv", consumption_list)
        DB_COMMANDER.delete_consumption_recipes()

    def save_quant(self, filename, data):
        """ Saves all the amounts of the ingredients/recipes to a csv and reset the counter to zero"""
        self.write_rows_to_csv(filename, [*data, [" "]])
        DP_CONTROLLER.say_all_data_exported()

    def write_rows_to_csv(self, filename, data_rows):
        dtime = str(datetime.date.today())
        dtime = dtime.replace("-", "")
        subfoldername = "saves"
        full_file_name = f"{dtime}_{filename}"
        savepath = os.path.join(DIRPATH, "..", subfoldername, full_file_name)
        with open(savepath, mode="a", newline="", encoding="utf-8") as writer_file:
            csv_writer = csv.writer(writer_file, delimiter=",")
            for row in data_rows:
                csv_writer.writerow(row)
        with open(savepath, "rb") as read_file:
            SERVICE_HANDLER.send_mail(full_file_name, read_file)


SAVE_HANDLER = SaveHandler()
