from src.core.parsers.dxf_parser import DxfParser
from src.core.processor.dxf_processor import DXFProcessor
from src.formatters.ezdxf_geopandas_convert import DXFShapelyFormat, ShapelyDXFFormat
from src.models.dxf_model import DXFDoc
from src.models.app_model import AppDoc
from src.controllers.dxf_controller import DXFController
from src.views.temporary_user_input import TemporaryUserInput


class Application:
    def __init__(self):
        """
        central application class
        """
        self.doc = AppDoc()
        self.dxf_doc = DXFDoc()
        self.dxf_parser = DxfParser()
        self.dxf_shapely_format = DXFShapelyFormat()
        self.shapely_dxf_format = ShapelyDXFFormat()
        self.dxf_processor = DXFProcessor()
        self.temporary_user_input = TemporaryUserInput()
        self.dxf_controller = DXFController(
            dxf_parser=self.dxf_parser,
            dxf_processor=self.dxf_processor,
            dxf_shapely_format=self.dxf_shapely_format,
            shapely_dxf_format=self.shapely_dxf_format,
            settings=self.temporary_user_input.settings,
            file_path=self.temporary_user_input.file_path,
            doc=self.doc,
            dxf_doc=self.dxf_doc
        )


app = Application()
app.dxf_controller.read_dxf()
app.dxf_controller.convert_dxf_gpd()
app.dxf_controller.clip_poygons()
app.dxf_controller.convert_gpd_dxf()
