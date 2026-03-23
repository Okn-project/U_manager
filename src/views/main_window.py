from PyQt5.QtWidgets import (QMainWindow, QMenuBar,QPushButton, QLabel,
                             QVBoxLayout, QWidget, QLineEdit, QHBoxLayout)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("DXF Processor")
        self.setGeometry(100, 100, 500, 300)

