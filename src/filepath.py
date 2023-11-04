"""Holds all the path location of the project"""

from pathlib import Path

# Root Path
ROOT_PATH = Path(__file__).parents[1].absolute()
CUSTOM_CONFIG_FILE = ROOT_PATH / "custom_config.yaml"
VERSION_FILE = ROOT_PATH / ".version.ini"
LOG_FOLDER = ROOT_PATH / "logs"
SAVE_FOLDER = ROOT_PATH / "saves"
ADDON_FOLDER = ROOT_PATH / "addons"
SCRIPTS_FOLDER = ROOT_PATH / "scripts"
USER_IMAGE_FOLDER = ROOT_PATH / "display_images_user"

# src path
SRC_PATH = ROOT_PATH / "src"
STYLE_FOLDER = SRC_PATH / "ui" / "styles"
CUSTOM_STYLE_FILE = STYLE_FOLDER / "custom.css"
CUSTOM_STYLE_SCSS = STYLE_FOLDER / "custom.scss"
LANGUAGE_FILE = SRC_PATH / "language.yaml"
APP_ICON_FILE = SRC_PATH / "ui_elements" / "Cocktail-icon.png"
ADDON_SKELTON = SRC_PATH / "programs" / "addon_skeleton.py"
DEFAULT_IMAGE_FOLDER = SRC_PATH / "ui_elements" / "default_images"

# other
LOCAL_MICROSERVICE_FILE = Path.home().absolute() / "ms-docker-compose.yaml"
DEFAULT_MICROSERVICE_FILE = SCRIPTS_FOLDER / "ms-docker-compose.yaml"
