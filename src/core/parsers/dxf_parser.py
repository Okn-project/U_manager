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
            raise FileNotFoundError
        except ezdxf.DXFStructureError:
            print(f"Invalid or corrupted DXF file.")
            raise ValueError

        except UnicodeDecodeError:
            print("decoding error occured")
