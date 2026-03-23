import ezdxf

# temporary import
from src.models.dxf_model import DXFDoc


class DxfParser:
    """
    Parse dxf document
    current version parses objects:
    LWPOLYLINE
    current version reads attributes of entities:
    "layer",
    'elevation',
    'color',
    'is_closed'
    'coords'
    """

    def __init__(self):
        self.entities_to_parse = ["LWPOLYLINE"]
        self.common_attributes_to_parse = {
            "LWPOLYLINE": [
                "layer",
                'elevation',
                'color',
                'linetype'
            ]
        }

        self.special_attributes_to_parse = {
            "LWPOLYLINE": [
                "is_closed",
            ]
        }

        self.api_methods_to_parse = {
            "LWPOLYLINE": [
                "get_points",
                "dxftype"
            ]
        }

    """read dxf file and convert dxf_enities into ezdxf objects
    stores dxf layers info into doc layers attr"""

    @staticmethod
    def read_dxf(doc: DXFDoc, file_path: str) -> None:
        """
        read DXF file. Define DXFDoc Drawing object
        :param doc: DXFDoc object from model
        :param file_path: file path from user
        :return: None
        """
        try:
            doc.data = ezdxf.readfile(file_path)

        except IOError:
            print(f"Not a DXF file or a generic I/O error.")
            raise FileNotFoundError
        except ezdxf.DXFStructureError:
            print(f"Invalid or corrupted DXF file.")
            raise ValueError
        except UnicodeDecodeError:
            print("decoding error occured")

    def parse_dxf_entities(self, doc: DXFDoc) -> None:
        """
        Parse DXFDoc object Drawing object. Defines DXFDoc entities
        See DxfParser init to config type of entities and attributes to parse through
        """

        model_space = doc.data.modelspace()
        for entity in model_space:
            entity_type = entity.dxftype()
            entity_attribs = {}
            if entity_type in self.entities_to_parse:
                for attr in self.common_attributes_to_parse[entity_type]:
                    parsed_common_attrib = getattr(entity.dxf, attr)
                    entity_attribs[attr] = parsed_common_attrib

                for spec_attr in self.special_attributes_to_parse[entity_type]:
                    parsed_scper_attr = getattr(entity, spec_attr)
                    entity_attribs[spec_attr] = parsed_scper_attr

                for method in self.api_methods_to_parse[entity_type]:
                    parsed_entity_attrib = getattr(entity, method)()
                    entity_attribs[method] = parsed_entity_attrib
                doc.entities.append(entity_attribs.copy())
                entity_attribs.clear()

    @staticmethod
    def parse_dxf_layers(doc: DXFDoc) -> None:
        """
        Parse DXFDoc object Drawing object. Defines DXFDoc layers
        :param doc: DXFDoc object from model
        :return: None
        """
        layers = doc.data.layers
        for layer in layers:
            doc.layers.append(layer.dxfattribs().copy())

    @staticmethod
    def parse_dxf_line_types(doc: DXFDoc) -> None:
        """
        Parse DXFDoc object Drawing object. Defines DXFDoc parse_dxf line_types
        :param doc: DXFDoc object from model
        :return: None
        """
        linetypes = doc.data.linetypes

        for linetype in linetypes:
            line_type_info = linetype.dxfattribs().copy()
            line_type_info["tags"] = linetype.pattern_tags.tags
            doc.linetypes.append(line_type_info)

