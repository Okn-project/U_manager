# temporary import
import pandas as pd
import ezdxf
from ezdxf.addons import Importer

from src.models.dxf_model import DXFDoc

from src.models.app_model import AppDoc
from ezdxf.document import Drawing
from shapely import LineString, Polygon
import numpy as np
import geopandas as gpd


class DXFShapelyFormat:
    """convert DXFDoc object into AppDoc object

    convertion_mapping for objects:
    LWPOLYLINE:
    common attrs [layer, elevation, color, is_closed]
    api_convertion: dxftype & get_points  -> shapely LineString
    """

    def __init__(self):
        self.convertion_map = \
            {"LWPOLYLINE": self.convert_lwpolyline_to_linestring
             }

    def convert_dxf_data_to_gpd(self, dxf_doc: DXFDoc, app_doc: AppDoc) -> None:
        """
        converts list of dictionaries with dxf entites  into gpd.dataframe
        :param dxf_doc:
        :param app_doc:
        :return:
        """
        entities = dxf_doc.entities
        layers = dxf_doc.layers
        line_types = dxf_doc.linetypes
        geometries = []

        for entity in entities:
            convert_func = self.convertion_map.get(entity["dxftype"])
            geometry = convert_func(entity)
            geometries.append(geometry)
        app_doc.geometries = gpd.GeoDataFrame(data=geometries)
        app_doc.layers = pd.DataFrame(data=layers)[["name", "linetype", "color", "lineweight"]]
        app_doc.line_styles = pd.DataFrame(data=line_types)[["name", "description", 'tags']]

    @staticmethod
    def convert_lwpolyline_to_linestring(lwpolyline: dict) -> dict:
        """
        process lwpolyline coords
        :param lwpolyline:
        :return:
        """
        coordinates = np.array(lwpolyline.pop("get_points"))[:, :2]
        geometry = LineString(coordinates=coordinates)
        lwpolyline["geometry"] = geometry
        return lwpolyline


class ShapelyDXFFormat:
    # TODO add version options interface
    """
    temporary
    create dxf_doc version: 2010
    convert gpd dataframe objects into ezdxf objects
    add ezdxf objects to dxf_doc

     convertion_mapping for objects:
    LineString:
    common attrs
    [layer,
    elevation,
    color,
    coords
    ] -> dict
    api attrs
    [is_closed -> closed]


    polygon: common attrs
    layer,
    elevation,
    color,
    coords
    ] -> dict
    api attrs
    [is_closed -> closed
    polygon.exterior.coords -> coords
    ]
    """

    def __init__(self):
        self.convertion_map = \
            {"LineString": self.convert_linestring_to_lwpolyline,
             "Polygon": self.convert_polygon_to_lwpolyline
             }
        self.coords_convert = \
            {"LineString": lambda linestring: linestring.coords,
             "Polygon": lambda polygon: polygon.exterior.coords
             }

    def convert_gpd_data_to_dxf(self, dxf_doc: DXFDoc, app_doc: AppDoc, save_path) -> None:
        """
               TODO
               :param dxf_doc:
               :param app_doc:
               :return:
               """
        # temporary usage
        doc = ezdxf.new(setup=False)
        importer = Importer(source=dxf_doc.data, target=doc)
        modelspace = doc.modelspace()
        importer.import_table("linetypes")
        importer.import_table("layers")

        for ndx, geometry in app_doc.geometries.iterrows():
            add_func = f"add_{geometry["dxftype"].lower()}"
            add_func = getattr(modelspace, add_func)
            coords, dxfattribs = self.convertion_map.get(geometry.geometry.geom_type)(geometry)
            add_func(coords, dxfattribs=dxfattribs.to_dict())

        # temporary usage
        doc.saveas(save_path, encoding='utf-8')

    @staticmethod
    def convert_linestring_to_lwpolyline(linestring: gpd.pd.Series) -> tuple:
        """
        get coordinates and dxf attribs of linestring
        :param linestring: gpd series linestring object
        :return: coordinates: list   dxf attribs: series
        """
        coords = list(linestring.geometry.coords)
        linestring.rename(inplace=True, index={"is_closed": "closed"})
        dxf_attribs = linestring.drop(["geometry", "dxftype"])
        return coords, dxf_attribs

    @staticmethod
    def convert_polygon_to_lwpolyline(polygon: gpd.pd.Series) -> tuple:
        """
        get coordinates and dxf attribs of polygon
        :param polygon: gpd series polygon object
        :return: coordinates: list   dxf attribs: series
        """
        coords = list(polygon.geometry.exterior.coords)
        polygon.rename(inplace=True, index={"is_closed": "closed"})
        dxf_attribs = polygon.drop(["geometry", "dxftype"])
        return coords, dxf_attribs
