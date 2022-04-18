
from typing import Any, Callable, List, Union
from pathlib import Path
from PyQt5.QtWidgets import QScrollArea, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QCheckBox, QPushButton, QBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

from src.config_manager import ConfigManager
from src.ui_elements.clickablelineedit import ClickableLineEdit
from src.ui.setup_keyboard_widget import KeyboardWidget
from src.ui.setup_password_screen import PasswordScreen


STYLE_FILE = Path(__file__).parents[0].absolute() / "styles.qss"
SMALL_FONT = 12
MEDIUM_FONT = 14
LARGE_FONT = 16


class ConfigWindow(QMainWindow, ConfigManager):
    def __init__(self):
        super().__init__()
        ConfigManager.__init__(self)
        self.icon_path = None
        self.config_objects = {}
        self._init_ui()

    def _init_ui(self):
        self.setWindowTitle("Change Configuration")
        self.scroll_area = QScrollArea()
        self.widget = QWidget()
        self.vbox = QVBoxLayout()

        for key, value in self.config_type.items():
            needed_type, _ = value
            self._choose_dispay_style(key, needed_type)

        self.button_back = QPushButton("Back")
        self.button_back.clicked.connect(self.close)
        self._adjust_font(self.button_back, LARGE_FONT, True)
        self.button_save = QPushButton("Save")
        self.button_save.clicked.connect(self._save_config)
        self.button_save.setProperty("cssClass", "btn-inverted")
        self._adjust_font(self.button_save, LARGE_FONT, True)
        self.hbox = QHBoxLayout()
        self.hbox.addWidget(self.button_back)
        self.hbox.addWidget(self.button_save)
        self.vbox.addLayout(self.hbox)

        self.widget.setLayout(self.vbox)

        self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setWidget(self.widget)
        self.setCentralWidget(self.scroll_area)

        # TODO: Refactor this into display controller and call it
        with open(STYLE_FILE, "r", encoding="utf-8") as filehandler:
            self.setStyleSheet(filehandler.read())
        self.show()

    def _save_config(self):
        print("TODO: Validation and Saving")
        print(self._retrieve_values())
        # self.close()

    def _choose_dispay_style(self, configname: str, configtype: type):
        """Creates the input face for the according config types"""
        # Add the elements header to the view
        header = QLabel(f"{configname}:")
        self._adjust_font(header, LARGE_FONT, True)
        self.vbox.addWidget(header)
        # Reads out the current config value
        current_value = getattr(self, configname)
        getter_fn = self._build_input_field(configname, configtype, current_value)
        # asigning the getter function for the config into the dict
        self.config_objects[configname] = getter_fn

    def _build_input_field(self, configname: str, configtype: type, current_value: Any, layout: Union[QBoxLayout, None] = None):
        """Builds the input field and returns its getter function"""
        if layout is None:
            layout = self.vbox
        if configtype == int:
            return self._build_int_field(layout, configname, current_value)
        if configtype == bool:
            return self._buid_bool_field(layout, current_value)
        if configtype == list:
            return self._build_list_field(configname, current_value)
        return self._build_fallback_field(layout, current_value)

    def _build_int_field(self, layout: QBoxLayout, configname: str, current_value: int) -> Callable[[], int]:
        """Builds a field for integer input with numpad"""
        config_input = ClickableLineEdit(str(current_value))
        self._adjust_font(config_input, MEDIUM_FONT)
        config_input.clicked.connect(lambda: PasswordScreen(self, le_to_write=config_input, headertext=configname))
        layout.addWidget(config_input)
        return lambda: int(config_input.text())

    def _buid_bool_field(self, layout: QBoxLayout, current_value: bool, displayed_text="on") -> Callable[[], bool]:
        """Builds a field for bool input with a checkbox"""
        config_input = QCheckBox(displayed_text)
        self._adjust_font(config_input, MEDIUM_FONT)
        config_input.setChecked(current_value)
        layout.addWidget(config_input)
        return config_input.isChecked

    def _build_list_field(self, configname: str, current_value: List) -> Callable[[], List[Any]]:
        """Builds a list of fields for a list input"""
        config_input = QVBoxLayout()
        getter_fn_list = []
        # iterate over each list value and build the according field
        for initial_value in current_value:
            self._add_ui_element_to_list(initial_value, getter_fn_list, configname, config_input)
        # adds a button for adding new list entries
        add_button = QPushButton("+ add")
        self._adjust_font(add_button, MEDIUM_FONT, True)
        add_button.clicked.connect(lambda: self._add_ui_element_to_list("", getter_fn_list, configname, config_input))
        # build container that new added elements are above add button seperately
        v_container = QVBoxLayout()
        v_container.addLayout(config_input)
        v_container.addWidget(add_button)
        self.vbox.addLayout(v_container)
        return lambda: [x() for x in getter_fn_list]

    def _add_ui_element_to_list(self, initial_value, getter_fn_list: List, configname: str, container: QBoxLayout):
        """Adds an additional input element for list buildup"""
        # Gets the type of the list elements
        list_type, _ = self.config_type_list.get(configname)
        h_container = QHBoxLayout()
        getter_fn = self._build_input_field(configname, list_type, initial_value, h_container)
        remove_button = QPushButton("x")
        self._adjust_font(remove_button, MEDIUM_FONT, True)
        # the first argument in lambda is needed since the object reference within the loop
        remove_button.clicked.connect(
            lambda _, x=h_container: self._remove_ui_element_from_list(x, getter_fn, getter_fn_list))
        h_container.addWidget(remove_button)
        container.addLayout(h_container)
        getter_fn_list.append(getter_fn)

    def _remove_ui_element_from_list(self, element, getter_fn, getter_fn_list: List[Callable]):
        """Removed the referenced element from the ui"""
        for i in reversed(range(element.count())):
            found_widget = element.itemAt(i).widget()
            found_widget.setParent(None)
        getter_fn_list.remove(getter_fn)
        element.deleteLater()

    def _build_fallback_field(self, layout: QBoxLayout, current_value) -> Callable[[], str]:
        """builds the default input field for string input"""
        config_input = ClickableLineEdit(str(current_value))
        self._adjust_font(config_input, MEDIUM_FONT, True)
        config_input.clicked.connect(lambda: KeyboardWidget(self, config_input, 200))
        layout.addWidget(config_input)
        return config_input.text

    def _retrieve_values(self):
        return {key: getter() for key, getter in self.config_objects.items()}

    def _adjust_font(self, element: QWidget, fontsize: int, bold: bool = False):
        font = QFont()
        font.setPointSize(fontsize)
        font.setBold(bold)
        weight = 75 if bold else 50
        font.setWeight(weight)
        element.setFont(font)
