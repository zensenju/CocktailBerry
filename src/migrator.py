# pylint: disable=too-few-public-methods
import configparser
import sys
import subprocess
from pathlib import Path
from sqlite3 import OperationalError
from typing import Union

from src.logger_handler import LoggerHandler
from src.database_commander import DatabaseHandler
from src import __version__

DIRPATH = Path(__file__).parent.absolute()
CONFIG_PATH = DIRPATH.parent / ".version.ini"
logger = LoggerHandler("migrator_module", "production_logs")


class Migrator:
    """Class to do all neccecary migration locally for new versions"""

    def __init__(self) -> None:
        self.program_version = _Version(__version__)
        self.config = configparser.ConfigParser()
        self.config.read(CONFIG_PATH)
        self.local_version = _Version(self.__get_local_version())

    def __get_local_version(self):
        try:
            local_version = self.config['DEFAULT']['LOCALVERSION']
        except KeyError:
            local_version = None
        return local_version

    def older_than_version(self, version: Union[str, None]) -> bool:
        """Checks if the current version is below the given version"""
        return _Version(version) > self.local_version

    def __write_local_version(self):
        """Writes the latest version to the local version"""
        logger.log_event("INFO", f"Local data migrated from {self.local_version} to {self.program_version}")
        self.config['DEFAULT']['LOCALVERSION'] = self.program_version.version
        with open(CONFIG_PATH, 'w', encoding="utf-8") as configfile:
            self.config.write(configfile)

    def make_migrations(self):
        """Make migration dependant on current local and program version"""
        # Database changes with version 1.5.0
        logger.log_event("INFO", f"Local version is: {self.local_version}, checking for necessary migrations")
        if self.older_than_version("1.5.0"):
            logger.log_event("INFO", "Making migrations for v1.5.0")
            self.__rename_database_to_english()
            self.__add_team_buffer_to_database()
            self.__install_pip_package("GitPython", "1.5.0")
        if self.older_than_version("1.5.3"):
            logger.log_event("INFO", "Making migrations for v1.5.3")
            self.__install_pip_package("typer", "1.5.3")
        if self.older_than_version("1.6.0"):
            logger.log_event("INFO", "Making migrations for v1.6.0")
            self.__change_git_repo()
            self.__install_pip_package("pyfiglet", "1.6.0")
        if self.older_than_version("1.6.1"):
            logger.log_event("INFO", "Making migrations for v1.6.1")
            self.__add_more_bottles_to_db()
        self.__check_local_version_data()

    def __check_local_version_data(self):
        """Checks to update the local version data"""
        if self.older_than_version(self.program_version.version):
            self.__write_local_version()
        else:
            logger.log_event("INFO", "Nothing to migrate")

    def __rename_database_to_english(self):
        """Renames all German columns to English ones"""
        logger.log_event("INFO", "Renaming German column names to English ones")
        db_handler = DatabaseHandler()
        commands = [
            # Rename all bottle things
            "ALTER TABLE Belegung RENAME TO Bottles",
            "ALTER TABLE Bottles RENAME COLUMN Flasche TO Bottle",
            "ALTER TABLE Bottles DROP COLUMN Mengenlevel",
            # Rename all recipe things
            "ALTER TABLE Rezepte RENAME TO Recipes",
            "ALTER TABLE Recipes RENAME COLUMN Alkoholgehalt TO Alcohol",
            "ALTER TABLE Recipes RENAME COLUMN Menge TO Amount",
            "ALTER TABLE Recipes RENAME COLUMN Kommentar TO Comment",
            "ALTER TABLE Recipes RENAME COLUMN Anzahl TO Counter",
            "ALTER TABLE Recipes RENAME COLUMN Anzahl_Lifetime TO Counter_lifetime",
            # Rename all available things
            "ALTER TABLE Vorhanden RENAME TO Available",
            # Rename all recipe data things
            "ALTER TABLE Zusammen RENAME TO RecipeData",
            "ALTER TABLE RecipeData RENAME COLUMN Rezept_ID TO Recipe_ID",
            "ALTER TABLE RecipeData RENAME COLUMN Zutaten_ID TO Ingredient_ID",
            "ALTER TABLE RecipeData RENAME COLUMN Menge TO Amount",
            "ALTER TABLE RecipeData RENAME COLUMN Alkoholisch TO Is_alcoholic",
            # Rename all ingredient things
            "ALTER TABLE Zutaten RENAME TO Ingredients",
            "ALTER TABLE Ingredients RENAME COLUMN Alkoholgehalt TO Alcohol",
            "ALTER TABLE Ingredients RENAME COLUMN Flaschenvolumen TO Volume",
            "ALTER TABLE Ingredients RENAME COLUMN Verbrauchsmenge TO Consumption_lifetime",
            "ALTER TABLE Ingredients RENAME COLUMN Verbrauch TO Consumption",
            "ALTER TABLE Ingredients RENAME COLUMN Mengenlevel TO Fill_level",
        ]
        for command in commands:
            try:
                db_handler.query_database(command)
            # this may occour if renaming already took place
            except OperationalError:
                pass

    def __add_more_bottles_to_db(self):
        """Updates the bottles to support up to 16 bottles"""
        logger.log_event("INFO", "Adding bottle numbers 11 to 16 to DB")
        db_handler = DatabaseHandler()
        # Adding constraint if still missing
        db_handler.query_database("CREATE UNIQUE INDEX IF NOT EXISTS idx_bottle ON Bottles(Bottle)")
        for bottle_count in range(11, 17):
            db_handler.query_database("INSERT OR IGNORE INTO Bottles(Bottle) VALUES (?)", (bottle_count,))

    def __add_team_buffer_to_database(self):
        """Adds an additional table for buffering not send team data"""
        logger.log_event("INFO", "Adding team buffer table to database")
        db_handler = DatabaseHandler()
        db_handler.query_database(
            """CREATE TABLE IF NOT EXISTS Teamdata(
                ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                Payload TEXT NOT NULL);"""
        )

    def __change_git_repo(self):
        """Sets the git source to the new named repo"""
        logger.log_event("INFO", "Changing git origin to new repo name")
        try:
            subprocess.check_call(["git", "remote", "set-url", "origin",
                                   "https://github.com/AndreWohnsland/CocktailBerry.git"])
        except subprocess.CalledProcessError as err:
            logger.log_event(
                "ERROR", "Could not change origin. Check if you made any local file changes / use 'git restore .'!")
            logger.log_exception(err)
            raise CouldNotMigrateException("1.6.0") from err

    def __install_pip_package(self, packagename: str, version_to_migrate: str):
        """Try to install a python package over pip"""
        logger.log_event("INFO", f"Trying to install {packagename}, it is needed since this version")
        try:
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', packagename])
            logger.log_event("INFO", f"Successfully installed {packagename}")
        except subprocess.CalledProcessError as err:
            logger.log_event("ERROR", f"Could not install {packagename} using pip. Please install it manually!")
            logger.log_exception(err)
            raise CouldNotMigrateException(version_to_migrate) from err


class _Version:
    """Class to compare semantic version numbers"""

    def __init__(self, version_number: Union[str, None]) -> None:
        self.version = version_number
        # no verison was found, just asume the worst, so using first version
        if version_number is None:
            major = 1
            minor = 0
            patch = 0
        # otherwise split version for later comparison
        else:
            major, minor, *patch = version_number.split(".")
        self.major = int(major)
        self.minor = int(minor)
        # Some version like 1.0 or 1.1 dont got a patch property
        # List unpacking will return an empty list or a list of one
        # Future version should contain patch (e.g. 1.1.0) as well
        if patch:
            self.patch = int(patch[0])
        else:
            self.patch = 0

    def __gt__(self, __o: object) -> bool:
        return (self.major, self.minor, self.patch) > (__o.major, __o.minor, __o.patch)

    def __eq__(self, __o: object) -> bool:
        return self.version == __o.version

    def __str__(self) -> str:
        if self.version is None:
            return "No defined Version"
        return f"v{self.version}"

    def __repr__(self) -> str:
        if self.version is None:
            return "Version(not defined)"
        return f"Version({self.version})"


class CouldNotMigrateException(Exception):
    """Raised when there was an error with the migration"""

    def __init__(self, version):
        self.message = f"Error while migration to version: {version}"
        super().__init__(self.message)
