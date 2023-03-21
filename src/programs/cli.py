# pylint: disable=unused-argument
import os
from typing import Optional
from pathlib import Path
import typer

from src.config_manager import CONFIG as cfg, version_callback, show_start_message
from src.migration.update_data import add_new_recipes_from_default_db
from src.utils import generate_custom_style_file
from src.programs.cocktailberry import run_cocktailberry
from src.programs.calibration import run_calibration
from src.programs.data_import import importer
from src.programs.clearing import clear_local_database


cli = typer.Typer(add_completion=False)


@cli.callback(invoke_without_command=True)
def main(
    ctx: typer.Context,
    calibration: bool = typer.Option(False, "--calibration", "-c", help="Run the calibration program."),
    debug: bool = typer.Option(False, "--debug", "-d", help="Using debug instead of normal Endpoints."),
    version: Optional[bool] = typer.Option(
        None, "--version", "-V", callback=version_callback, help="Show current version.")
):
    """
    Starts the cocktail program. Optional, can start the calibration program.
    If you want to debug your microservice, you can use the --debug flag.

    For more information visit https://cocktailberry.readthedocs.io/ or https://github.com/AndreWohnsland/CocktailBerry.
    """
    if ctx.invoked_subcommand is not None:
        return
    show_start_message()
    cfg.sync_config_to_file()
    if debug:
        os.environ.setdefault('DEBUG_MS', 'True')
        print("Using debug mode")
    generate_custom_style_file()
    if calibration:
        run_calibration()
    run_cocktailberry()


@cli.command()
def data_import(
    path: Path,
    conversion: float = typer.Option(1.0, "--conversion", "-c", help="Conversion factor to ml"),
    no_unit: bool = typer.Option(False, "--no-unit", "-nu", help="Ingredient data got no unit text"),
):
    """
    Imports the recipe data from a file.
    If the units are not in ml, please provide the conversion factor into ml.

    The file should contain the cocktail name, followed by ingredient data (amount, name).
    For further information regarding the file structure,
    please see https://cocktailberry.readthedocs.io/commands/#importing-recipes-from-file.
    """
    importer(path, conversion, no_unit)


@cli.command()
def update_database():
    """
    Using the default provided database to check for newly added recipes due to new updates.
    Adds the new recipes including missing ingredients to the local database.
    Ignore recipes that collide with names of your self-added recipes.
    Creates a backup before doing the update,
    see also https://cocktailberry.readthedocs.io/troubleshooting/#restoring-database

    Please take note that the ingredients are in german, so if you renamed your ingredients,
    this will most likely add all ingredients from the new recipes in german to your local database.
    If you are not satisfied the result, consult the documentation how to use the backup.
    You can also create a own backup with the build in CocktailBerry backup function over the program interface.
    More information also at https://cocktailberry.readthedocs.io/commands/#updating-local-database
    """
    add_new_recipes_from_default_db()


@cli.command()
def clear_database():
    """
    Clears the local database from the entered or default data.
    After this action, there will be no recipes or ingredients in your local CocktailBerry data.
    A backup of your local database is created before deleting.
    Use this if you want to build your own custom database and not use any of the supplied data.
    See also: https://cocktailberry.readthedocs.io/commands/#clearing-local-database
    """
    clear_local_database()
