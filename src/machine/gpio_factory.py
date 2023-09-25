"""Module to create the according GPIO controller for the appropriate Board"""
from src.machine.interface import GPIOController
from src.machine.raspberry import RaspberryGPIO
from src.machine.generic_board import GenericGPIO
from src.config_manager import CONFIG as cfg


class GPIOFactory:
    def __init__(self, inverted: bool) -> None:
        # global general inverted status
        self.inverted = inverted

    def generate_gpio(self, inverted: bool, pin: int) -> GPIOController:
        """Return the appropriate GPIO
        Option to specific invert one GPIO relative to general setting
        """
        board = cfg.MAKER_BOARD
        # using xor here to created the right inverted status
        is_inverted = self.inverted ^ inverted
        if board == "RPI":
            return RaspberryGPIO(is_inverted, pin)
        return GenericGPIO(is_inverted, pin)
