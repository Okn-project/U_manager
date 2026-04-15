from PyQt5.QtWidgets import QWidget, QHBoxLayout
from PyQt5.QtCore import Qt, pyqtSignal


class LayersNamesLabelFrame(QWidget):
    layer_selected = pyqtSignal(object)
    STYLES = \
        {
            "normal":
                """
                    QWidget {
                        background-color: #f0f0f0;
                        border: 1px solid #ccc;
                        border-radius: 4px;
                        padding: 5px;
                        margin: 5px;
                        box-shadow: 1px 1px 2px rgba(0, 0, 0, 0.1);
                    }
                """,
            "selected":
                """
                    QWidget {
                       background-color: #ffff99;
                       border: 2px solid #ffcc00;
                       border-radius: 4px;
                       padding: 5px;
                       margin: 5px;
                       box-shadow: 2px 2px 3px rgba(0, 0, 0, 0.2);
               }
                """

        }

    def __init__(self, text="", parent=None):
        super().__init__(parent)
        self.setMaximumHeight(50)
        self.setMaximumWidth(250)
        self.setStyleSheet(self.STYLES["normal"])
        self.layer_text = text
        self.setObjectName(text)
        self.is_selected = False
        self.textbox = QHBoxLayout(self)
        self.textbox.setContentsMargins(0, 0, 0, 0)
        self.textbox.setSpacing(5)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.layer_selected.emit({"layer_text": self.layer_text,
                                      "parent": self.parent().objectName(),
                                      "object_name": self.objectName()})
            event.accept()
        else:
            super().mousePressEvent(event)

    def set_selected(self):
        self.setStyleSheet(self.STYLES["selected"])
        self.is_selected = True

    def set_normal(self):
        self.setStyleSheet(self.STYLES["normal"])
        self.is_selected = False
