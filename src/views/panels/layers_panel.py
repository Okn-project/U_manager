from PyQt5.QtWidgets import QWidget, QVBoxLayout, QScrollArea
from src.views.labels import PanelHeader
from src.utils.utils import clear_layout, remove_stretch


class LayerPanel(QWidget):
    def __init__(self, parent, name, header: str):
        super().__init__(parent)
        self.__main_layout = QVBoxLayout(self)

        self.__header_layout = QVBoxLayout()
        self.__header_layout.setSpacing(0)
        self.__header_layout.setContentsMargins(0, 0, 0, 0)
        self.__header = PanelHeader(header)
        self.__header_layout.addWidget(self.__header)

        self.__panel = QWidget(self)
        self.__panel.setObjectName(name)
        self.__panel_layout = QVBoxLayout(self.__panel)
        self.__panel_layout.setSpacing(0)
        self.__panel_layout.setContentsMargins(0, 0, 0, 0)

        self.__scroller = QScrollArea()
        self.__scroller.setWidgetResizable(True)
        self.__scroller.setWidget(self.__panel)
        self.__scroller_layout = QVBoxLayout()
        self.__scroller_layout.addWidget(self.__scroller)

        self.__main_layout.addLayout(self.__header_layout)
        self.__main_layout.addLayout(self.__scroller_layout)

    def addWidget(self, widget: QWidget):
        self.__panel_layout.addWidget(widget)

    def addStretch(self, num):
        self.__panel_layout.addStretch(num)

    def remove_stretch(self):
        remove_stretch(self.__panel_layout)

    def find_child(self, qtype, name):
        return self.__panel.findChild(qtype, name)

    def clear_panel(self):
        clear_layout(self.__panel_layout)

    def get_children(self):
        return self.__panel.children()

    def get_frames(self):
        return [child for child in self.__panel.children() if hasattr(child, "layer_text")]

    def has_frames(self):
        return len(self.get_frames())

    def remove_frame(self, frame: QWidget):
        frame.setParent(None)
