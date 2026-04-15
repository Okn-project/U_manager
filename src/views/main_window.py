from PyQt5.QtWidgets import (QMainWindow, QPushButton, QLabel,
                             QVBoxLayout, QWidget, QLineEdit, QHBoxLayout, QMenu, QMessageBox)
from src.views.main_menu import MainMenu


class MainWindow(QMainWindow):
    """
    main window widget
    """

    def __init__(self):
        super().__init__()
        self.setWindowTitle("DXF Processor")
        self.setGeometry(100, 100, 500, 300)

        self._init_ui()

    def _init_ui(self):
        self.menu_bar = MainMenu(self)
        self.setMenuBar(self.menu_bar)

    def show_warning_no_file_import(self, title: str, message: str):
        QMessageBox.warning(self, title, message)

    def show_warning_failed_import(self, title: str, message: str):
        """
        wrong file type loaded error
        :param title:
        :param message:
        :return:
        """
        QMessageBox.warning(self, title, message)

