import pandas as pd
import geopandas as gpd

# temporary import
from src.core.parsers.dxf_parser import DxfParser
from src.core.processor.dxf_processor import DXFProcessor
from src.formatters.ezdxf_geopandas_convert import DXFShapelyFormat, ShapelyDXFFormat
from src.models.dxf_model import DXFDoc
from src.models.app_model import AppDoc


class DXFController:
    """
    controls dxf procession and UI representation functions
    """

    def __init__(self,
                 dxf_parser: DxfParser,
                 dxf_processor: DXFProcessor,
                 dxf_shapely_format: DXFShapelyFormat,
                 shapely_dxf_format: ShapelyDXFFormat,
                 settings: dict | None = None,
                 file_path: str | None = None,
                 doc: AppDoc | None = None,
                 dxf_doc: DXFDoc | None = None
                 ):
        self.doc = doc
        self.dxf_parser = dxf_parser
        self.dxf_processor = dxf_processor
        self.dxf_shapely_format = dxf_shapely_format
        self.shapely_dxf_format = shapely_dxf_format
        self.settings = settings
        self.file_path = file_path
        self.dxf_doc = dxf_doc

    def get_file_path(self):
        pass

    def read_dxf(self):
        self.dxf_parser.read_dxf(self.dxf_doc, self.file_path)
        self.dxf_parser.parse_dxf_entities(self.dxf_doc)
        self.dxf_parser.parse_dxf_layers(self.dxf_doc)
        self.dxf_parser.parse_dxf_line_types(self.dxf_doc)

    def convert_dxf_gpd(self):
        self.dxf_shapely_format.convert_dxf_data_to_gpd(self.dxf_doc, self.doc)

    def convert_gpd_dxf(self):
        self.shapely_dxf_format.convert_gpd_data_to_dxf(self.dxf_doc, self.doc)

    def clip_poygons(self):
        self.dxf_processor.clip_polygon_areas(doc=self.doc, settings=self.settings)
        self.dxf_processor.explode_multilines(doc=self.doc, settings=self.settings)
