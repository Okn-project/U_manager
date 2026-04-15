from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout
from PyQt5.QtCore import pyqtSignal
from src.views.buttons.move_button import MoveRightButton, MoveLeftButton
from src.views.buttons.clip_button import CLipButton


class ButtonsPanel(QWidget):
    add_line_request = pyqtSignal(str)
    remove_line_request = pyqtSignal(str)
    add_poly_request = pyqtSignal(str)
    remove_poly_request = pyqtSignal(str)
    clip_request = pyqtSignal(str)

    def __init__(self, parent, name):
        super().__init__(parent)
        self.name = name
        self.init_ui()
        self.connect_signals()

    def init_ui(self):
        self.main_layout = QVBoxLayout(self)

        self.add_line = MoveRightButton(self, "add_line")
        self.remove_line = MoveLeftButton(self, "remove_line")
        self.add_poly = MoveRightButton(self, "add_poly")
        self.remove_poly = MoveLeftButton(self, "remove_poly")
        self.clip = CLipButton(self)

        self.top_buttons = QVBoxLayout()
        self.top_buttons.setSpacing(0)
        self.top_buttons.setContentsMargins(0, 50, 0, 0)
        self.top_buttons.addWidget(self.add_line)
        self.top_buttons.addWidget(self.remove_line)
        self.top_buttons.addSpacing(170)

        self.bot_buttons = QVBoxLayout()
        self.bot_buttons.setSpacing(0)
        self.bot_buttons.setContentsMargins(0, 0, 0, 0)
        self.bot_buttons.addWidget(self.add_poly)
        self.bot_buttons.addWidget(self.remove_poly)
        self.bot_buttons.addStretch(1)
        self.bot_buttons.addWidget(self.clip)

        self.main_layout.addLayout(self.top_buttons)
        self.main_layout.addLayout(self.bot_buttons)

    def connect_signals(self):
        self.add_line.move_right_command.connect(self.add_line_slot)
        self.remove_line.move_left_command.connect(self.remove_line_slot)
        self.add_poly.move_right_command.connect(self.add_poly_slot)
        self.remove_poly.move_left_command.connect(self.remove_poly_slot)
        self.clip.clip_hors_command.connect(self.clip_slot)

    def add_line_slot(self):
        self.add_line_request.emit("add_line_request")

    def remove_line_slot(self):
        self.remove_line_request.emit("remove_line_request")

    def add_poly_slot(self):
        self.add_poly_request.emit("add_poly_request")

    def remove_poly_slot(self):
        self.remove_poly_request.emit("remove_poly_request")

    def clip_slot(self):
        self.clip_request.emit("clip_request")

    def clip_active(self, state: bool):
        self.clip.set_active(state)
