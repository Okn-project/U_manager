from shapely import Polygon, LineString, Point
import ezdxf
from ezdxf.document import Drawing



class DXFShapelyFormat:
    """convert ezdxf doc objects into shapely objects, collect shapely objects to storage
    current version converts objects: LWp
    """

    def __init__(self, doc: Drawing):
        self.doc = doc
        self.storage = []

    def convert(self):
        for entity in self.doc.modelspace():
            pass


class ShapelyDXFFormat:
    def __init__(self, doc):
        self.doc = doc


