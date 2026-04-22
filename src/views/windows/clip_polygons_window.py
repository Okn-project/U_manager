from PyQt5.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout, QScrollArea, QWidget, QLabel, QSpacerItem
from PyQt5.QtCore import Qt, QMargins, pyqtSignal
from src.views.labels import LayersNamesLabel
from src.views.frames import LayersNamesLabelFrame
from src.views.panels.layers_panel import LayerPanel
from src.views.panels.buttons_panel import ButtonsPanel


class ClipPolygonsWindow(QDialog):
    set_clip_line = pyqtSignal(str)
    del_clip_line = pyqtSignal(str)
    set_clip_poly = pyqtSignal(str)
    del_clip_poly = pyqtSignal(str)
    clear_clip = pyqtSignal()
    clip = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle("Обрезка горизонталей")
        self.setModal(True)
        self.resize(700, 500)

        self.main_layout = QHBoxLayout(self)

        self.layers_panel = LayerPanel(self, "layers_panel", "Слои файла")
        self.buttons_panel = ButtonsPanel(self, "buttons_panel")

        self.lines_panel = LayerPanel(self, "lines_panel", "Слои горизонталей")
        self.poly_panel = LayerPanel(self, "poly_panel", "Слои полигонов")
        self.settings_panel = QVBoxLayout()
        self.settings_panel.setSpacing(0)
        self.settings_panel.setContentsMargins(0, 0, 0, 0)
        self.settings_panel.addWidget(self.lines_panel)
        self.settings_panel.addWidget(self.poly_panel)

        self.main_layout.addWidget(self.layers_panel, 2)
        self.main_layout.addWidget(self.buttons_panel, 1)
        self.main_layout.addLayout(self.settings_panel, 2)
        self.connect_signals()

    def connect_signals(self):
        self.buttons_panel.add_line_request.connect(self.add_lines_to_settings)
        self.buttons_panel.remove_line_request.connect(self.remove_line_from_settings)
        self.buttons_panel.add_poly_request.connect(self.add_poly_to_settings)
        self.buttons_panel.remove_poly_request.connect(self.remove_poly_from_settings)
        self.buttons_panel.clip_request.connect(self.clip)

    def show_file_layers(self, layers: list) -> None:
        """show list of layers in left layers pannel"""
        self.layers_panel.clear_panel()

        for layer_name in layers:
            layer_text = LayersNamesLabel(layer_name, self)
            layer_textbox = LayersNamesLabelFrame(layer_name)
            layer_textbox.textbox.addWidget(layer_text)
            layer_textbox.layer_selected.connect(self.layer_selected)
            self.layers_panel.addWidget(layer_textbox)
        self.layers_panel.addStretch(1)

    def layer_selected(self, signal):
        panel = getattr(self, signal["parent"])
        for frame in self.layers_panel.get_frames():
            frame.set_normal()
        for frame in self.lines_panel.get_frames():
            frame.set_normal()
        for frame in self.poly_panel.get_frames():
            frame.set_normal()
        frame = panel.find_child(QWidget, signal["layer_text"])
        frame.set_selected()

    def check_panels(self):
        clip_active = self.lines_panel.has_frames() and self.poly_panel.has_frames()
        self.buttons_panel.clip_active(clip_active)

    def add_lines_to_settings(self, signal):
        for frame in self.layers_panel.get_frames():
            if frame.is_selected:
                frame.set_normal()
                frame.setParent(None)
                self.lines_panel.remove_stretch()
                self.lines_panel.addWidget(frame)
                self.lines_panel.addStretch(1)
                self.set_line_command(frame.objectName())
                self.check_panels()
                break

    def remove_line_from_settings(self, signal):
        for frame in self.lines_panel.get_frames():
            if frame.is_selected:
                frame.set_normal()
                frame.setParent(None)
                self.layers_panel.remove_stretch()
                self.layers_panel.addWidget(frame)
                self.layers_panel.addStretch(1)
                self.del_line_command(frame.objectName())
                self.check_panels()
                break

    def add_poly_to_settings(self, signal):
        for frame in self.layers_panel.get_frames():
            if frame.is_selected:
                frame.set_normal()
                frame.setParent(None)
                self.poly_panel.remove_stretch()
                self.poly_panel.addWidget(frame)
                self.poly_panel.addStretch(1)
                self.set_poly_command(frame.objectName())
                self.check_panels()
                break

    def remove_poly_from_settings(self, signal):
        for frame in self.poly_panel.get_frames():
            if frame.is_selected:
                frame.set_normal()
                frame.setParent(None)
                self.layers_panel.remove_stretch()
                self.layers_panel.addWidget(frame)
                self.layers_panel.addStretch(1)
                self.del_poly_command(frame.objectName())
                self.check_panels()
                break

    def set_line_command(self, line):
        self.set_clip_line.emit(line)

    def del_line_command(self, line):
        self.del_clip_line.emit(line)

    def set_poly_command(self, poly):
        self.set_clip_poly.emit(poly)

    def del_poly_command(self, poly):
        self.del_clip_poly.emit(poly)

    def clear_commands(self):
        self.clear_clip.emit()

    def clip_command(self):
        self.clip.emit()

    def closeEvent(self, event):
        self.layers_panel.clear_panel()
        self.lines_panel.clear_panel()
        self.poly_panel.clear_panel()
        self.clear_commands()
        event.accept()
