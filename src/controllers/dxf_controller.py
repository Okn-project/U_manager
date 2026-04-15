from PyQt5.QtWidgets import QFileDialog

# temporary import
from src.core.parsers.dxf_parser import DxfParser
from src.core.processor.dxf_processor import DXFProcessor
from src.formatters.ezdxf_geopandas_convert import DXFShapelyFormat, ShapelyDXFFormat
from src.models.dxf_model import DXFDoc
from src.models.app_model import AppDoc
from src.views.main_window import MainWindow
from src.views.clip_polygons_window import ClipPolygonsWindow
from src.config import Config


class DXFController:
    """
    controls dxf procession and UI representation functions
    """

    def __init__(self,
                 dxf_parser: DxfParser,
                 dxf_processor: DXFProcessor,
                 dxf_shapely_format: DXFShapelyFormat,
                 shapely_dxf_format: ShapelyDXFFormat,
                 config: Config | None,
                 settings: dict | None = None,
                 file_path: str | None = None,
                 doc: AppDoc | None = None,
                 dxf_doc: DXFDoc | None = None,
                 main_window: MainWindow = None,
                 clip_polygons_window: ClipPolygonsWindow = None
                 ):
        self.doc = doc
        self.dxf_parser = dxf_parser
        self.dxf_processor = dxf_processor
        self.dxf_shapely_format = dxf_shapely_format
        self.shapely_dxf_format = shapely_dxf_format
        self.config = config
        self.settings = settings
        self.file_path = file_path
        self.dxf_doc = dxf_doc
        self.main_window = main_window
        self.clip_polygons_window = clip_polygons_window
        self.connect_main_menu_signals()
        self.connect_clip_menu_signals()

    def connect_main_menu_signals(self):
        """
        connect  main_menu_ file actions with functions
        :return:
        """
        self.main_window.menu_bar.import_file_request.connect(self.pipe_load_dxf_file)
        self.main_window.menu_bar.clip_polygons_request.connect(self.show_clip_polygons_window)

    def connect_clip_menu_signals(self):
        self.clip_polygons_window.set_clip_line.connect(self.add_clip_line)
        self.clip_polygons_window.del_clip_line.connect(self.del_clip_line)
        self.clip_polygons_window.set_clip_poly.connect(self.add_clip_poly)
        self.clip_polygons_window.del_clip_poly.connect(self.del_clip_poly)
        self.clip_polygons_window.clear_clip.connect(self.clear_clip)
        self.clip_polygons_window.clip.connect(self.clip_poygons)

    def add_clip_line(self, line):
        self.config.add_clip_line(line)

    def del_clip_line(self, line):
        self.config.del_clip_line(line)

    def add_clip_poly(self, poly):
        self.config.add_clip_poly(poly)

    def del_clip_poly(self, poly):
        self.config.del_clip_poly(poly)

    def clear_clip(self):
        self.config.clear_clip()

    def show_clip_polygons_window(self):
        layers = self.doc.layers["name"].values if "name" in self.doc.layers.columns.values else []
        self.clip_polygons_window.show_file_layers(layers)
        self.clip_polygons_window.exec_()

    def pipe_load_dxf_file(self):
        """
        read and load DXF file into app model
        :return:
        """
        self.doc.clear()
        self.config.clear_clip()
        self.dxf_doc = DXFDoc()  # TODO Temporary desision to clear dxf source file. Must be changed soon.
        self.file_path, _ = QFileDialog.getOpenFileName(
            parent=self.main_window,
            caption="Выберите файл",
            directory="",
            filter="CAD (*.dxf);; Все файлы (*)"
        )

        if not self.file_path:
            title = "сбой загрузки"
            message = "файл не был загружен"
            self.main_window.show_warning_failed_import(title, message)
            return
        try:
            self.dxf_parser.read_dxf(self.dxf_doc, self.file_path)
            self.dxf_parser.parse_dxf_entities(self.dxf_doc)
            self.dxf_parser.parse_dxf_layers(self.dxf_doc)
            self.dxf_parser.parse_dxf_line_types(self.dxf_doc)
            self.dxf_shapely_format.convert_dxf_data_to_gpd(self.dxf_doc, self.doc)



        except FileNotFoundError:
            title = f"Неверный файл"
            message = f"Загруженный файл не является DXF файлом и не может быть прочтен"
            self.main_window.show_warning_failed_import(title, message)
            self.file_path = None
            return
        except ValueError:
            title = f"Поврежденный файл"
            message = f"Загруженный DXF файл поврежден и не может быть прочтен"
            self.main_window.show_warning_failed_import(title, message)
            self.file_path = None
            return
        except UnicodeDecodeError:
            title = f"Повреждение кодировки"
            message = f"В Загруженном файле обнаружена ошибка кодировки, файл не может быть прочтен"
            self.file_path = None
            return
        except Exception:
            title = f"Критическая ошибка"
            message = f"При загрузке файла произошел критический сбой. Файл не может быть прочтен"
            self.file_path = None
            return

    def convert_gpd_dxf(self):
        self.shapely_dxf_format.convert_gpd_data_to_dxf(self.dxf_doc, self.doc)

    def clip_poygons(self):
        self.dxf_processor.clip_polygon_areas(doc=self.doc, config=self.config)
        self.dxf_processor.explode_multilines(doc=self.doc, config=self.config)
        self.shapely_dxf_format.convert_gpd_data_to_dxf(self.dxf_doc, self.doc, f"{self.file_path}_res.dxf")
