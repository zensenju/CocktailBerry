# -*- coding: utf-8 -*-
""" Module with all necessary functions for the recipes Tab.
This includes all functions for the Lists, DB and Buttons/Dropdowns.
"""

from collections import Counter
from typing import List, Tuple

from src.tabs import maker

from src.display_controller import DP_CONTROLLER
from src.database_commander import DB_COMMANDER
from src.error_handler import logerror
from src.models import Cocktail, Ingredient
from src.config_manager import shared


def fill_recipe_box_with_ingredients(w):
    """ Assigns all ingredients to the Comboboxes in the recipe tab """
    comboboxes_recipe = DP_CONTROLLER.get_comboboxes_recipes(w)
    ingredient_list = [x.name for x in DB_COMMANDER.get_all_ingredients(get_hand=False)]
    DP_CONTROLLER.fill_multiple_combobox(comboboxes_recipe, ingredient_list, clear_first=True)


@logerror
def handle_enter_recipe(w):
    """ Enters or updates the recipe into the db"""
    recipe_input = DP_CONTROLLER.get_recipe_field_data(w)
    recipe_name, selected_name, ingredient_names, ingredient_volumes, enabled, virgin, comment = recipe_input
    new_recipe = not bool(selected_name)
    print(f"{new_recipe=}")

    if not recipe_name:
        DP_CONTROLLER.say_enter_cocktail_name()
        return
    names, volumes, valid = _validate_extract_ingredients(ingredient_names, ingredient_volumes)
    if not valid:
        return

    recipe_id, error_message = _check_enter_constraints(recipe_name, new_recipe)
    if error_message:
        return

    recipe_volume, ingredient_data, recipe_alcohol_level = _build_recipe_data(names, volumes)

    cocktail = _enter_or_update_recipe(
        recipe_id, recipe_name, recipe_volume, recipe_alcohol_level, enabled, virgin, ingredient_data, comment
    )

    # remove the old name only if update
    if not new_recipe:
        DP_CONTROLLER.remove_recipe_from_list_widgets(w, selected_name)
    DP_CONTROLLER.fill_list_widget_recipes(w, [cocktail.name])
    DP_CONTROLLER.clear_recipe_data_maker(w, select_other_item=False)
    if enabled:
        maker.evaluate_recipe_maker_view(w, [cocktail])
    DP_CONTROLLER.clear_recipe_data_recipes(w, False)

    if new_recipe:
        DP_CONTROLLER.say_recipe_added(cocktail.name)
    else:
        DP_CONTROLLER.say_recipe_updated(selected_name, cocktail.name)


def _validate_extract_ingredients(ingredient_names: List[str], ingredient_volumes: List[str]) -> Tuple[List[str], List[int], bool]:
    """Gives a list for names and volume of ingredients.
    If some according value is missing, informs the user.
    Returns [names], [volumes], is_valid"""
    names: list[str] = []
    volumes: list[str] = []
    for name, volume in zip(ingredient_names, ingredient_volumes):
        if (name == "" and volume != "") or (name != "" and volume == ""):
            DP_CONTROLLER.say_some_value_missing()
            return [], [], False
        if name != "":
            names.append(name)
            volumes.append(volume)
    if len(names) == 0:
        DP_CONTROLLER.say_recipe_at_least_one_ingredient()
        return [], [], False
    counter_names = Counter(names)
    double_names = [x[0] for x in counter_names.items() if x[1] > 1]
    if len(double_names) != 0:
        DP_CONTROLLER.say_ingredient_double_usage(double_names[0])
        return [], [], False
    try:
        int_volumes = [int(x) for x in volumes]
    except ValueError:
        DP_CONTROLLER.say_needs_to_be_int()
        return [], [], False
    return names, int_volumes, True


def _check_enter_constraints(recipe_name: str, new_recipe: bool) -> Tuple[int, bool]:
    """Checks if either the recipe already exists (new recipe) or if one is selected (update)
    Returns cocktail, got_error"""
    cocktail = DB_COMMANDER.get_cocktail(recipe_name)
    if cocktail is not None and new_recipe:
        DP_CONTROLLER.say_name_already_exists()
        return cocktail.id, True
    if cocktail is None:
        return 0, False
    return cocktail.id, False


def _build_recipe_data(names: list[str], volumes: list[int]):
    """Gets volume, ingredient objects and concentration of cocktails"""
    recipe_volume = sum(volumes)
    ingredient_data: list[Ingredient] = []
    recipe_volume_concentration = 0

    # first build the ingredient objects for machine add
    for ingredient_name, ingredient_volume in zip(names, volumes):
        ingredient: Ingredient = DB_COMMANDER.get_ingredient(ingredient_name)  # type: ignore
        ingredient.amount = ingredient_volume
        ingredient.recipe_hand = False
        recipe_volume_concentration += ingredient.alcohol * ingredient_volume
        ingredient_data.append(ingredient)

    # build also the handadd data into an ingredient
    for ing in shared.handaddlist:
        ingredient: Ingredient = DB_COMMANDER.get_ingredient(ing.id)  # type: ignore
        ingredient.amount = ing.amount
        ingredient.recipe_hand = True
        recipe_volume += ing.amount
        recipe_volume_concentration += ingredient.alcohol * ing.amount
        ingredient_data.append(ingredient)

    recipe_alcohol_level = int(recipe_volume_concentration / recipe_volume)

    return recipe_volume, ingredient_data, recipe_alcohol_level


def _enter_or_update_recipe(
    recipe_id,
    recipe_name,
    recipe_volume,
    recipe_alcohol_level,
    enabled,
    virgin,
    ingredient_data: List[Ingredient],
    comment
):
    """Logic to insert/update data into DB"""
    if recipe_id:
        DB_COMMANDER.delete_recipe_ingredient_data(recipe_id)
        DB_COMMANDER.set_recipe(recipe_id, recipe_name, recipe_alcohol_level, recipe_volume, comment, enabled, virgin)
    else:
        DB_COMMANDER.insert_new_recipe(recipe_name, recipe_alcohol_level, recipe_volume, comment, enabled, virgin)
    cocktail = DB_COMMANDER.get_cocktail(recipe_name)  # type: ignore -> will always return cocktail
    for ingredient in ingredient_data:
        DB_COMMANDER.insert_recipe_data(cocktail.id, ingredient.id, ingredient.amount, bool(ingredient.recipe_hand))
    # important to get the cocktail again, since the first time getting it, we only got it for its id
    # at this time the cocktail got no recipe data. Getting it again will fix this
    cocktail: Cocktail = DB_COMMANDER.get_cocktail(recipe_name)  # type: ignore -> will always return cocktail
    return cocktail


def load_recipe_view_names(w):
    """ Updates the ListWidget in the recipe Tab. """
    cocktails = DB_COMMANDER.get_all_cocktails()
    recipe_list = [x.name for x in cocktails]
    DP_CONTROLLER.clear_list_widget_recipes(w)
    DP_CONTROLLER.fill_list_widget_recipes(w, recipe_list)


@logerror
def load_selected_recipe_data(w):
    """ Loads all Data from the recipe DB into the according Fields in the recipe tab. """
    _, recipe_name, *_ = DP_CONTROLLER.get_recipe_field_data(w)
    DP_CONTROLLER.set_recipe_add_label(w, bool(recipe_name))
    if not recipe_name:
        return

    DP_CONTROLLER.clear_recipe_data_recipes(w, True)
    cocktail = DB_COMMANDER.get_cocktail(recipe_name)
    if cocktail is None:
        return
    DP_CONTROLLER.set_recipe_data(w, cocktail)


@logerror
def delete_recipe(w):
    """ Deletes the selected recipe, requires the Password """
    _, recipe_name, *_ = DP_CONTROLLER.get_recipe_field_data(w)
    if not recipe_name:
        DP_CONTROLLER.say_no_recipe_selected()
        return
    if not DP_CONTROLLER.password_prompt():
        return

    DB_COMMANDER.delete_recipe(recipe_name)
    DP_CONTROLLER.remove_recipe_from_list_widgets(w, recipe_name)
    DP_CONTROLLER.clear_recipe_data_recipes(w, False)
    DP_CONTROLLER.clear_recipe_data_maker(w)
    DP_CONTROLLER.say_recipe_deleted(recipe_name)


@logerror
def enable_all_recipes(w):
    """Set all recipes to enabled """
    if not DP_CONTROLLER.ask_enable_all_recipes():
        return
    disabled_cocktails = DB_COMMANDER.get_all_cocktails(get_enabled=False)
    DB_COMMANDER.set_all_recipes_enabled()
    maker.evaluate_recipe_maker_view(w, disabled_cocktails)
    DP_CONTROLLER.clear_recipe_data_recipes(w, True)
    DP_CONTROLLER.say_all_recipes_enabled()
