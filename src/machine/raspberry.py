from typing import List, Optional
from src.machine.interface import PinController
from src.logger_handler import LoggerHandler


logger = LoggerHandler("RpiController")

try:
    # pylint: disable=import-error
    from RPi import GPIO  # type: ignore
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    DEV = False
except ModuleNotFoundError:
    DEV = True


class RpiController(PinController):
    """Controller class to control Raspberry Pi pins"""

    def __init__(self, inverted: bool) -> None:
        super().__init__(inverted)
        self.devenvironment = DEV
        self.low = GPIO.LOW if not DEV else 0
        self.high = GPIO.HIGH if not DEV else 1
        if inverted:
            self.low, self.high = self.high, self.low

    def initialize_pin_list(self, pin_list: List[int]):
        """Set up the given pin list"""
        print(f"Devenvironment on the RPi module is {'on' if self.devenvironment else 'off'}")
        if not self.devenvironment:
            GPIO.setup(pin_list, GPIO.OUT, initial=self.low)
        else:
            logger.log_event("WARNING", "Could not import RPi.GPIO. Will not be able to control pins")

    def activate_pin_list(self, pin_list: List[int]):
        """Activates the given pin list"""
        if not self.devenvironment:
            GPIO.output(pin_list, self.high)

    def close_pin_list(self, pin_list: List[int]):
        """Closes the given pin_list"""
        if not self.devenvironment:
            GPIO.output(pin_list, self.low)

    def cleanup_pin_list(self, pin_list: Optional[List[int]] = None):
        if self.devenvironment:
            return
        if pin_list is None:
            GPIO.cleanup()
        else:
            GPIO.cleanup(pin_list)
