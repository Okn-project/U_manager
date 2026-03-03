import ezdxf.entities.dxfns
import shapely
from shapely import LineString
from ezdxf.document import Drawing
import numpy as np
import geopandas as gpd

# Temporary import
from src.core.parsers.dxf_parser import DxfParser


# Temporary usage
# FILE_PATH = r'../../tests/data/small_test.dxf'
# parser = DxfParser(file_path=FILE_PATH)
# parser.read_dxf()


class DXFShapelyFormat:
    """convert ezdxf doc objects into list of atributes, collect list of atributes  to storage
    current version converts objects: LWPOLYLINE
    current version gets attributes:
    layer
    line_type
    weight
    elevation
    color
    is_closed: 1 if closed 0 if not closed
    geometry: shapely object
    """

    def __init__(self, doc: Drawing):
        self.doc = doc
        self.storage = []

    def get_data_from_ezdxf(self) -> None:
        """
        converts ezdxf LWPOLYLINE objects  into list of atributes, collect list of atributes  to storage
        see list of attributes in DXFShapelyFormat.doc
        """
        for entity in self.doc.modelspace():
            if entity.dxftype() == 'LWPOLYLINE':
                try:
                    coords = entity.lwpoints.values[:, 0:2]
                    # TODO redo getting LWPOLYLINE points
                    layer = entity.dxf.layer
                    line_type = entity.dxf.linetype
                    weight = entity.dxf.const_width
                    z = entity.dxf.elevation
                    color = entity.dxf.color
                    is_closed = entity.dxfattribs()["flags"]
                    width = entity.dxf.const_width
                    geometry = shapely.LineString(coords)
                    self.storage.append(
                        [layer,
                         line_type,
                         weight,
                         z,
                         color,
                         is_closed,
                         width,
                         geometry])
                except ezdxf.lldxf.const.DXFAttributeError:
                    print("one of attributes does no exist, process ruined")

        print("")

    def convert_data_to_gpd(self):
        """converts storage data list into gpd.dataframe
        clears storage after done"""
        self.doc = gpd.GeoDataFrame(data=self.storage, columns=[
            'layer',
            'line_type',
            'weight',
            'z',
            'color',
            'is_closed',
            'width',
            'geometry'])
        self.storage.clear()


class ShapelyDXFFormat:
    def __init__(self, doc):
        self.doc = doc


# Temporary usage
# dxf_shapely_format = DXFShapelyFormat(doc=parser.doc)
# dxf_shapely_format.get_data_from_ezdxf()
# .convert_data_to_gpd()

