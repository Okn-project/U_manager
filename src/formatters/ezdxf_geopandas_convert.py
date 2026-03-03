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
    linetype
    lineweight
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
                    linetype = entity.dxf.linetype
                    lineweight = entity.dxf.const_width
                    elevation = entity.dxf.elevation
                    color = entity.dxf.color
                    is_closed = entity.dxfattribs()["flags"]
                    geometry = shapely.LineString(coords)
                    self.storage.append(
                        [layer,
                         linetype,
                         lineweight,
                         elevation,
                         color,
                         is_closed,
                         geometry])
                except ezdxf.lldxf.const.DXFAttributeError:
                    print("one of attributes does no exist, process ruined")

        print("")

    def convert_data_to_gpd(self):
        """converts storage data list into gpd.dataframe
        clears storage after done"""
        self.doc = gpd.GeoDataFrame(data=self.storage, columns=[
            'layer',
            'linetype',
            'lineweight',
            'elevation',
            'color',

            'is_closed',
            'geometry'])
        self.storage.clear()


class ShapelyDXFFormat:
    """
    creates dxf_doc version: 2010
    TODO add version options interface
    convert gpd dataframe objects into ezdxf object
    current version converts objects:  polygon, LWPOLYLINE
    current version gets attributes:
        layer
        linetype
        lineweight
        elevation
        color

        geometry: shapely object
        """

    def __init__(self, doc: gpd.GeoDataFrame):
        self.doc = doc
        self.dxf_doc = ezdxf.new("R2010", setup=True)
        self.model_space = self.dxf_doc.modelspace()

    def convert_data_to_dxf(self):
        """
        converts gpdDataframe objects  into ezdxf objects, add objects to dxf_doc model_space
        see list of attributes in ShapelyDXFFormat.doc
        :return: None
        """


        for ndx, geometry in self.doc.iterrows():
            # all atrs without geometry
            entity_attribs = geometry[["layer",  "lineweight", "elevation", "color"]].to_dict()
            print(entity_attribs)
            geom_type = geometry.geometry.geom_type
            if geom_type == "Polygon":
                coords = np.array(geometry.geometry.exterior.coords)
            elif geom_type == "LineString":
                coords = np.array(geometry.geometry.coords)
            self.model_space.add_lwpolyline(coords, dxfattribs=entity_attribs)

        # Temporary usage
# dxf_shapely_format = DXFShapelyFormat(doc=parser.doc)
# dxf_shapely_format.get_data_from_ezdxf()
# .convert_data_to_gpd()
