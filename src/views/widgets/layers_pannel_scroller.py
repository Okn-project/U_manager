from PyQt5.QtWidgets import QWidget, QScrollArea
from PyQt5.QtCore import Qt


class PanelScroller(QScrollArea):
    def __init__(self, parent):
        super().__init__(parent)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.setWidgetResizable(True)
