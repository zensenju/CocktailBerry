from typing import Optional, get_args
import re
from dataclasses import fields
from PyQt5.QtWidgets import QMainWindow, QLabel, QColorDialog, QLineEdit
from PyQt5.QtGui import QColor
from PyQt5.QtCore import QSize
import qtsass

from src import SupportedThemesType
from src.filepath import STYLE_FOLDER
from src.ui.icons import parse_colors
from src.dialog_handler import UI_LANGUAGE
from src.display_controller import DP_CONTROLLER
from src.ui_elements import Ui_ColorWindow
from src.ui_elements.clickablelineedit import ClickableLineEdit
from src.ui.creation_utils import SMALL_FONT, MEDIUM_FONT, LARGE_FONT, adjust_font, create_spacer

THEMES = list(get_args(SupportedThemesType))


class ColorWindow(QMainWindow, Ui_ColorWindow):
    """ Creates the log window Widget. """

    def __init__(self, parent):
        """ Init. Connect all the buttons and set window policy. """
        super().__init__()
        self.setupUi(self)
        DP_CONTROLLER.initialize_window_object(self)
        self.mainscreen = parent
        self.color_picker: Optional[QColorDialog] = None
        self.inputs_colors: dict[str, ClickableLineEdit] = {}
        self.custom_colors = parse_colors("custom")
        # Connect all the buttons, generates a list of the numbers an object names to do that
        self.button_back.clicked.connect(self.close)
        self.button_use_template.clicked.connect(self._set_selected_template)
        self.button_apply.clicked.connect(self._apply_settings)

        # Get log file names, fill widget, select default, if it exists
        DP_CONTROLLER.fill_single_combobox(self.selection_template, THEMES, first_empty=False)
        self._generate_color_fields()

        UI_LANGUAGE.adjust_color_window(self)
        self.showFullScreen()
        DP_CONTROLLER.set_display_settings(self)

    def _set_selected_template(self):
        """Uses the selected template and fills the color into the fields"""
        template: SupportedThemesType = self.selection_template.currentText()  # type: ignore -> only these are set
        colors = parse_colors(template)
        for color in fields(colors):
            line_edit = self.inputs_colors[color.name]
            color_value = colors[color.name]
            line_edit.setText(color_value)
            line_edit.setStyleSheet(self._generate_style(color_value))

    def _generate_color_fields(self):
        """Generates all the needed fields to change colors"""
        # adds a spacer on top
        self.color_container.addItem(create_spacer(20))
        for color in fields(self.custom_colors):
            self._generate_color_section(color.name)
            self.color_container.addItem(create_spacer(12))

    def _generate_color_section(self, color_name: str):
        """Generates a section for the color including color pad, and user input"""
        header = QLabel(f"{color_name}:")
        adjust_font(header, LARGE_FONT, True)
        self.color_container.addWidget(header)
        description_text = UI_LANGUAGE.get_config_description(color_name, "color_window")
        if description_text:
            description = QLabel(description_text)
            adjust_font(description, SMALL_FONT)
            self.color_container.addWidget(description)
        # Reads out the current config value
        current_value = self.custom_colors[color_name]
        color_input = ClickableLineEdit(str(current_value))
        color_input.setMinimumSize(QSize(0, 50))
        color_input.clicked.connect(lambda: self._connect_color_picker(color_input))
        color_input.setStyleSheet(self._generate_style(current_value))
        adjust_font(color_input, MEDIUM_FONT)
        color_input.setProperty("cssClass", "secondary")
        self.color_container.addWidget(color_input)
        self.inputs_colors[color_name] = color_input

    def _connect_color_picker(self, line_edit_to_write: QLineEdit):
        """Opens a color picker for the user to select the color
        Uses the current color as default.
        Inserts the selected color into the line edit
        """
        self.color_picker = QColorDialog(self)
        current_color = line_edit_to_write.text()
        self.color_picker.setCurrentColor(QColor(current_color))

        if self.color_picker.exec_():
            selected_color = self.color_picker.currentColor().name()
            line_edit_to_write.setText(selected_color)
            line_edit_to_write.setStyleSheet(self._generate_style(selected_color))

    def _generate_style(self, color: str):
        """Generates a style with same bg and font color"""
        return f"background-color: {color}; color: {color};"

    def _apply_settings(self):
        """Applies the settings to the custom.scss file
        Builds the css file afterwards with the qtsass package
        """
        # read in the custom style file
        custom_style_file = STYLE_FOLDER / "custom.scss"
        style = custom_style_file.read_text()
        # replace lines with new color
        for color_name, color_line_edit in self.inputs_colors.items():
            color_value: str = color_line_edit.text()
            replace_regex = r"\$" + f"{color_name}:" + r"\s*(#[0-9a-f]{3,6});"
            replacement = f"${color_name}: {color_value};"
            style = re.sub(replace_regex, replacement, style)
        custom_style_file.write_text(style)
        # compile the file with qtsass
        compiled_style_file = STYLE_FOLDER / "custom.css"
        qtsass.compile_filename(custom_style_file, compiled_style_file)
        self.close()
