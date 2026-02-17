import ezdxf
from ezdxf.document import Drawing


class DxfParser:
    """read dxf file and convert it into ezdxf objects"""

    def __init__(self, file_path: str):
        self.file_path = file_path
        self.doc = None

    def read_dxf(self):
        """red DXF file."""
        try:
            self.doc = ezdxf.readfile(self.file_path)
        except IOError:
            print(f"Not a DXF file or a generic I/O error.")
        except ezdxf.DXFStructureError:
            print(f"Invalid or corrupted DXF file.")
        return True


path = r'../../../tests/data/big_test.dxf'
dxf_doc = DxfParser(path)
dxf_doc.read_dxf()

for entity in dxf_doc.doc.modelspace():
    print(f"тип примитива: {entity.dxftype()}")
    print(f"cлой примитива: {entity.dxf.layer}")
    print()

    if entity.dxftype() == "LWPOLYLINE":
        print(f"в полилинии вершин: {len(entity)}")


from ezdxf.entities import lwpolyline
