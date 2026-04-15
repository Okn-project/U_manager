from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import Qt


class PanelHeader(QLabel):
    STYLES = {
        "normal":
            """
                font-weight: bold;
                font-size: 14px;
                color: #2c3e50;
                padding: 8px 0px;
                background-color: #ecf0f1;
                border-bottom: 2px solid #3498db;
                margin-bottom: 5px;
            """
    }

    def __init__(self, text="", parent=None):
        super().__init__(text, parent)
        self.setAlignment(Qt.AlignCenter)
        self.setStyleSheet(self.STYLES["normal"])
