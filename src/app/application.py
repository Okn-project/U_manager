from src.core.parsers.dxf_parser import DxfParser
from src.core.processor.dxf_processor import DXFProcessor
from src.formatters.ezdxf_geopandas_convert import DXFShapelyFormat, ShapelyDXFFormat
from src.models.dxf_model import DXFDoc
from src.models.app_model import AppDoc
from src.controllers.dxf_controller import DXFController  # TODO убрать позже
from src.controllers import MainController, ImportController, ExportController, ModelController
from PyQt5.QtWidgets import QApplication
from src.views.windows import MainWindow, ClipPolygonsWindow
from src.config import Config
import sys



class Application:
    def __init__(self):
        """
        central application class
        """
        self.app = QApplication(sys.argv)
        self.main_window = MainWindow()
        self.clip_polygons_window = ClipPolygonsWindow()

        self.doc = AppDoc()
        self.dxf_doc = DXFDoc()
        self.dxf_parser = DxfParser()
        self.dxf_shapely_format = DXFShapelyFormat()
        self.shapely_dxf_format = ShapelyDXFFormat()
        self.dxf_processor = DXFProcessor()
        self.config = Config()
        self.export_controller = ExportController()
        self.import_controller = ImportController(
            dxf_parser=self.dxf_parser,
            dxf_shapely_format=self.dxf_shapely_format,
            doc=self.doc,
            dxf_doc=self.dxf_doc
        )
        self.model_controller = ModelController()

        self.main_controller = MainController(
            export_controller=self.export_controller,
            import_controller=self.import_controller,
            model_controller=self.model_controller,
            main_window=self.main_window,
            clip_polygons_window=self.clip_polygons_window
        )

        self.dxf_controller = DXFController(
            dxf_parser=self.dxf_parser,
            dxf_processor=self.dxf_processor,
            dxf_shapely_format=self.dxf_shapely_format,
            shapely_dxf_format=self.shapely_dxf_format,
            config=self.config,
            doc=self.doc,
            dxf_doc=self.dxf_doc,
            main_window=self.main_window,
            clip_polygons_window=self.clip_polygons_window

        )
