from .export_controller import ExportController
from .import_controller import ImportController
from .model_controller import ModelController
from src.views.windows import MainWindow
from src.views.windows import ClipPolygonsWindow


class MainController:
    def __init__(self,
                 export_controller: ExportController,
                 import_controller: ImportController,
                 model_controller: ModelController,
                 main_window: MainWindow,
                 clip_polygons_window: ClipPolygonsWindow
                 ):
        self.__model_controller = model_controller
        self.__export_controller = export_controller
        self.__import_controller = import_controller
        self.__main_window = main_window
        self.__clip_polygons_window = clip_polygons_window
