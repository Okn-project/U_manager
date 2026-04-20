from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import Qt


class LayersNamesLabel(QLabel):
    STYLES = \
        {
            "normal":
                """
                padding: 5px;
                margin: 5px;
                font-weight: bold;
                color: #333;
                """
        }

    def __init__(self, text="", parent=None):
        super().__init__(text, parent)
        self.setup_layers_style()

    def setup_layers_style(self):
        self.setLineWidth(2)
        self.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.setWordWrap(False)
        self.setStyleSheet(self.STYLES["normal"])
