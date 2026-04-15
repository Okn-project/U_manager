from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import pyqtSignal


class CLipButton(QPushButton):
    clip_hors_command = pyqtSignal(str)

    STYLES = \
        {
            "normal":
                """
                QPushButton {
                background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                  stop: 0 #FF9800, stop: 1 #F57C00);
                color: white;
                border: 1px solid #E65100;
                padding: 12px 24px;
                border-radius: 8px;
                font-weight: bold;
                font-size: 14px;
                box-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2);
    }
                QPushButton:hover {
                background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                stop: 0 #FFA726, stop: 1 #FB8C00);
                box-shadow: 3px 3px 5px rgba(0, 0, 0, 0.3);
    }
                QPushButton:pressed {
                background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                stop: 0 #E65100, stop: 1 #BF360C);
                box-shadow: inset 1px 1px 3px rgba(0, 0, 0, 0.4);
    }
                """
        }

    def __init__(self, parent):
        super().__init__(parent)
        self.setMaximumWidth(150)
        self.setText("обработка")
        self.name = "CLipButton"
        self.clicked.connect(self.on_clicked)

    def on_clicked(self):
        self.clip_hors_command.emit(self.name)
