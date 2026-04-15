from PyQt5.QtWidgets import QWidget


class FileLayersPannel(QWidget):
    def __init__(self, parent, name: str = "FileLayersPannel"):
        super().__init__(parent)
        self.name = name
