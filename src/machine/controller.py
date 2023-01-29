import time
from typing import List, Union
from PyQt5.QtWidgets import qApp

from src.config_manager import shared, CONFIG as cfg
from src.machine.generic_board import GenericController
from src.machine.interface import PinController
from src.machine.raspberry import RpiController


class MachineController():
    """Controller Class for all Machine related Pin routines """

    def __init__(self):
        super().__init__()
        self._pin_controller = self.__chose_controller()

    def __chose_controller(self) -> PinController:
        """Selects the controller class for the Pin"""
        if cfg.MAKER_BOARD == "RPI":
            return RpiController()
        # In case none is found, fall back to generic using python-periphery
        return GenericController()

    def clean_pumps(self, w):
        """Clean the pumps for the defined time in the config.
        Activates all pumps for the given time
        """
        active_pins = cfg.PUMP_PINS[: cfg.MAKER_NUMBER_BOTTLES]
        t_cleaned = 0.0
        self._header_print("Start Cleaning")
        self._start_pumps(active_pins)
        w.open_progression_window("Cleaning")
        # also using same button cancel from prepare cocktail
        shared.make_cocktail = True
        while t_cleaned < cfg.MAKER_CLEAN_TIME and shared.make_cocktail:
            self._clean_print(t_cleaned)
            t_cleaned += cfg.MAKER_SLEEP_TIME
            t_cleaned = round(t_cleaned, 2)
            time.sleep(cfg.MAKER_SLEEP_TIME)
            w.change_progression_window(t_cleaned / cfg.MAKER_CLEAN_TIME * 100)
            qApp.processEvents()
        self._clean_print(cfg.MAKER_CLEAN_TIME)
        print("")
        self._stop_pumps(active_pins)
        self._header_print("Done Cleaning")
        w.close_progression_window()

    def make_cocktail(
        self,
        w,
        bottle_list: List[int],
        volume_list: list[Union[float, int]],
        recipe="",
        is_cocktail=True
    ):
        """RPI Logic to prepare the cocktail.
        Calculates needed time for each slot according to data and config.
        Updates Progressbar status. Returns data for DB updates.

        Args:
            w (QtMainWindow): MainWindow Object
            bottle_list (List[int]): Number of bottles to be used
            volume_list (List[float]): Corresponding Volume needed of bottles
            recipe (str, optional): Option to change the display text of Progress Screen. Defaults to "".

        Returns:
            tuple(List[int], float, float): Consumption of each bottle, taken time, max needed time
        """
        # Only show team dialog if it is enabled
        if cfg.TEAMS_ACTIVE and is_cocktail:
            w.open_team_window()
        shared.cocktail_started = True
        shared.make_cocktail = True
        if w is not None:
            w.open_progression_window(recipe)
        indexes = [x - 1 for x in bottle_list]
        pins = [cfg.PUMP_PINS[i] for i in indexes]
        volume_flows = [cfg.PUMP_VOLUMEFLOW[i] for i in indexes]
        pin_times = [round(volume / flow, 1) for volume, flow in zip(volume_list, volume_flows)]
        max_time = max(pin_times)
        # Starting Making cocktail
        self._header_print(f"Starting {recipe}")
        self._start_pumps(pins)
        already_closed_pins = set()
        current_time = 0.0
        consumption = [0.0] * len(indexes)
        while current_time < max_time and shared.make_cocktail:
            # Iterate over each Pin and keep needed state
            for element, (pin, pin_time, volume_flow) in enumerate(zip(pins, pin_times, volume_flows)):
                if pin_time > current_time:
                    consumption[element] += volume_flow * cfg.MAKER_SLEEP_TIME
                elif pin not in already_closed_pins:
                    self._print_time(current_time, max_time)
                    self._stop_pumps([pin])
                    already_closed_pins.add(pin)
            # Adjust needed data
            self._consumption_print(consumption, current_time, max_time)
            current_time += cfg.MAKER_SLEEP_TIME
            current_time = round(current_time, 2)
            time.sleep(cfg.MAKER_SLEEP_TIME)
            if w is not None:
                w.change_progression_window(current_time / max_time * 100)
            qApp.processEvents()

        self._stop_pumps(pins)
        consumption = [round(x) for x in consumption]
        print("Total calculated consumption:", consumption)
        self._header_print(f"Finished {recipe}")
        if w is not None:
            w.close_progression_window()
        return consumption, current_time, max_time

    def _print_time(self, current_time: float, total_time: float):
        """Prints the current passed time in relation to total time"""
        print(f"{current_time:.1f}/{total_time:.1f} s:\t", end="")

    def set_up_pumps(self):
        """Gets all used pins, prints pins and uses controller class to set up"""
        active_pins = cfg.PUMP_PINS[: cfg.MAKER_NUMBER_BOTTLES]
        print(f"Initializing Pins: {active_pins}")
        self._pin_controller.initialize_pin_list(active_pins)

    def _start_pumps(self, pin_list: List[int]):
        """Informs and opens all given pins"""
        print(f"Opening Pins: {pin_list}")
        self._pin_controller.activate_pin_list(pin_list)

    def close_all_pumps(self):
        """Close all pins connected to the pumps"""
        active_pins = cfg.PUMP_PINS[: cfg.MAKER_NUMBER_BOTTLES]
        self._stop_pumps(active_pins)

    def cleanup(self):
        """Cleanup for shutdown the machine"""
        self.close_all_pumps()
        self._pin_controller.cleanup_pin_list()

    def _stop_pumps(self, pin_list: List[int]):
        """Informs and closes all given pins"""
        print(f"Closing Pins: {pin_list}")
        self._pin_controller.close_pin_list(pin_list)

    def _consumption_print(self, consumption: List[float], current_time: float, max_time: float, interval=1):
        """Displays each interval seconds information for cocktail preparation"""
        if current_time % interval == 0:
            pretty_consumption = [round(x) for x in consumption]
            print(f"{current_time:.1f}/{max_time:.1f} s:\tpreparing, consumption: {pretty_consumption}")

    def _clean_print(self, t_cleaned: float, interval=0.5):
        """Progress print for cleaning"""
        if t_cleaned % interval == 0:
            print(
                f"Cleaning, {t_cleaned:.1f}/{cfg.MAKER_CLEAN_TIME:.1f} s {'.' * int(t_cleaned*2)}", end="\r"
            )  # type: ignore

    def _header_print(self, msg: str):
        """Formats the message with dashes around"""
        print(f"{' ' + msg + ' ':-^80}")


MACHINE = MachineController()
