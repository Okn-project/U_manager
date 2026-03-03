import geopandas as gpd
from shapely import Polygon

# Temporary import
from src.core.parsers.dxf_parser import DxfParser
from src.formatters.ezdxf_geopandas_convert import DXFShapelyFormat

# Temporary usage
FILE_PATH = r'C:\Users\Mission\Desktop\main\proj\U_manager\tests\data\small_test.dxf'
parser = DxfParser(file_path=FILE_PATH)
parser.read_dxf()
dxf_shapely_format = DXFShapelyFormat(doc=parser.doc)
dxf_shapely_format.get_data_from_ezdxf()
dxf_shapely_format.convert_data_to_gpd()


class CADProcessor:
    """Processor manipulates autocad objects
    it current version it realises these functions:
    - clip horisontals inside polygons
    """

    def __init__(self, doc: gpd.GeoDataFrame, settings: dict):
        # settings - temporary dict  to be transfered into class Settings object
        self.doc = doc
        self.settings = settings

    def show_polylines(self):
        # temporary function
        pass

    def clip_polygon_areas(self):
        """

        select every closed line from user SETTINGS with selector
        convert closed lines into polygons
        select every line from user SETTINGS
        :return: None
        """
        polygon_selector = (
                (self.doc.geometry.geom_type == "LineString") &
                (self.doc["is_closed"] &
                 (self.doc.layer == self.settings["polygons"]))
        )

        line_selecor = (
                (self.doc.geometry.geom_type == "LineString") &
                (self.doc.layer == self.settings["lines"])
        )
        self.doc.loc[polygon_selector, "geometry"] = self.doc.loc[polygon_selector, "geometry"].apply(
            lambda geometry: Polygon(geometry.coords))
        polygons = self.doc[polygon_selector]
        lines = self.doc[line_selecor]

        # TODO use sjoin + intersection for better perfomanse in future versions
        new_lines = gpd.overlay(lines, polygons, how='difference')
        print(self.doc.to_string())
        self.doc.drop(list(lines.index.values), axis='rows', inplace=True)
        self.doc = gpd.pd.concat(objs=[self.doc, new_lines])
        print(self.doc.to_string())


# Temporary usage
SETTINGS = {"lines": "ГОРИЗОНТАЛИ", "polygons": "ЗАНИЯ"}
dxf_processor = CADProcessor(doc=dxf_shapely_format.doc, settings=SETTINGS)
dxf_processor.show_polylines()
dxf_processor.clip_polygon_areas()
print("debug")
