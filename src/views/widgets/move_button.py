from PyQt5.QtWidgets import QPushButton, QSizePolicy
from PyQt5.QtCore import pyqtSignal, QMargins


class MoveButton(QPushButton):
    STYLES = \
        {
            "normal":
                """ 
                    QPushButton {
                    background-color: #f0f0f0;
                    border: 1px solid #ccc;
                    padding: 8px 16px;
                    border-radius: 4px;
                    font-weight: bold;
                    color: #333;
                    font-size: 14px;
                }
                    QPushButton:hover {
                    background-color: #e0e0e0;
                    border-color: #aaa;
                }
                    QPushButton:pressed {
                    background-color: #d0d0d0;
                    border-color: #999;
                }
                """
        }

    def __init__(self, parent):
        super().__init__(parent)
        self.setStyleSheet(self.STYLES["normal"])
        self.setMaximumWidth(150)
        self.setContentsMargins(0, 0, 0, 0)
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)


class MoveRightButton(MoveButton):
    move_right_command = pyqtSignal(str)

    def __init__(self, parent, name: str = "MoveRightButton"):
        super().__init__(parent)
        self.setText(">>>")
        self.name = name
        self.clicked.connect(self.on_clicked)

    def on_clicked(self):
        """
        emits move_right_command signal when clicked
        :return:
        """
        self.move_right_command.emit(self.name)


class MoveLeftButton(MoveButton):
    move_left_command = pyqtSignal(str)

    def __init__(self, parent, name: str = "MoveRightButton"):
        super().__init__(parent)
        self.setText("<<<")
        self.name = name
        self.clicked.connect(self.on_clicked)

    def on_clicked(self):
        """
        emits move_left_command signal when clicked
        :return:
        """
        self.move_left_command.emit(self.name)
