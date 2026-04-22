from src.core.parsers import DxfParser
from src.formatters import DXFShapelyFormat
from src.models.app_model import AppDoc
from src.models.dxf_model import DXFDoc


class ImportController:
    """
    модуль для чтения фалов разных типов
    сейчас реализуется импорт dxf
    """

    def __init__(self,
                 dxf_parser: DxfParser,
                 dxf_shapely_format: DXFShapelyFormat,
                 doc: AppDoc | None = None,
                 dxf_doc: DXFDoc | None = None,
                 ):
        self.dxf_parser = dxf_parser
        self.dxf_shapely_format = dxf_shapely_format
        self.doc = doc
        self.dxf_doc = dxf_doc
