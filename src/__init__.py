from typing import Literal

__version__ = "1.19.0"
PROJECT_NAME = "CocktailBerry"
MAX_SUPPORTED_BOTTLES = 16
SupportedLanguagesType = Literal["en", "de"]
SupportedBoardType = Literal["RPI", "Generic"]
SupportedThemesType = Literal["default", "bavaria", "alien", "berry", "custom"]
SupportedRfidType = Literal["No", "MFRC522"]  # "PiicoDev"
NEEDED_PYTHON_VERSION = (3, 9)
FUTURE_PYTHON_VERSION = (3, 9)
