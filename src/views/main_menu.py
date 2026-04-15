from PyQt5.QtWidgets import QMenuBar, QAction, QMainWindow, QMenu
from PyQt5.QtCore import pyqtSignal


class MainMenu(QMenuBar):
    """
    Main menu in main window
    """
    import_file_request = pyqtSignal()
    export_file_request = pyqtSignal()
    clip_polygons_request = pyqtSignal()
    close_polygons_request = pyqtSignal()

    CONFIG = {
        '&Файл': [
            {'group_name': "file"},
            {'text': 'Загрузить файл',
             'name': 'load_file',
             'shortcut': 'Ctrl+O',
             'status_tip': 'Открыть DXF‑файл',
             'signal': 'import_file_request'
             },

            {'text': 'Сохранить как',
             'name': 'save_file_as',
             'shortcut': 'Ctrl+S',
             'signal': 'export_file_request'
             },

            '---',  # separator
            {'text': 'Выход',
             'shortcut': 'Ctrl+Q'
             }
        ],
        '&CAD': [
            {'group_name': "CAD"},
            {'text': 'Обработка горизонталей',
             'name': 'clip_polygons',
             # "setEnabled": False,
             "signal": "clip_polygons_request"},

            {'text': 'Замыкание полигонов',
             'name': 'close_polygons',
             # "setEnabled": False,
             "signal": "close_polygons_request"
             }

        ],
        '&Справка': [
            {'text': 'О программе'}
        ]
    }

    def __init__(self, parent):
        super().__init__(parent)
        self.config_menu(parent)

    def enable_cad_menu(self, state) -> None:
        """
        enables autocad menu commands when file is loaded
        :return:
        """

        cad_menu = self.findChild(QMenu, "CAD")
        for menu_item in cad_menu.actions():

            if not menu_item.isSeparator():
                menu_item.setEnabled(state)

    def config_menu(self, parent: QMainWindow) -> None:
        """

        :param parent: main window param
        :return:
        """
        for menu_group, group_item in self.CONFIG.items():
            this_menu_group = self.addMenu(menu_group)

            for item in group_item:
                if item == '---':
                    this_menu_group.addSeparator()
                elif "group_name" in item:
                    this_menu_group.setObjectName(item["group_name"])
                else:
                    action = QAction(item['text'], parent)
                    if "name" in item:
                        action.setObjectName(item['name'])
                    if 'shortcut' in item:
                        action.setShortcut(item['shortcut'])
                    if 'status_tip' in item:
                        action.setStatusTip(item['status_tip'])
                    if 'setEnabled' in item:
                        action.setEnabled(item['setEnabled'])
                    if 'signal' in item:
                        signal = getattr(self, item['signal'])
                        action.triggered.connect(signal.emit)
                    this_menu_group.addAction(action)
