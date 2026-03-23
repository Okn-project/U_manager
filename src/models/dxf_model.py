import pandas as pd
import geopandas as gpd
from typing import List, Dict, Optional

# temporary import
import ezdxf
from ezdxf.document import Drawing


class DXFDoc:
    def __init__(
            self,
            data: Optional[Drawing] = None,
            layers: Optional[List[Dict]] = None,
            entities: Optional[List[Dict]] = None,
            linetypes: Optional[List[Dict]] = None
    ):
        self.__data = data
        self.__layers = layers or []
        self.__entities = entities or []
        self.__linetypes = linetypes or []

    @property
    def data(self) -> Optional[Drawing]:
        return self.__data

    @data.setter
    def data(self, value: Drawing) -> None:
        if not isinstance(value, Drawing):
            raise TypeError("data must be a Drawing object")
        self.__data = value

    @property
    def layers(self) -> List[Dict]:
        return self.__layers

    @layers.setter
    def layers(self, value: List[Dict]) -> None:
        if not isinstance(value, list):
            raise TypeError("layers must be a list of dictionaries")
        self.__layers = value

    @property
    def entities(self) -> List[Dict]:
        return self.__entities

    @entities.setter
    def entities(self, value: List[Dict]) -> None:
        if not isinstance(value, list):
            raise TypeError("entities must be a list of dictionaries")
        self.__entities = value

    @property
    def linetypes(self) -> List[Dict]:
        return self.__linetypes

    @linetypes.setter
    def linetypes(self, value: List[Dict]) -> None:
        if not isinstance(value, list):
            raise TypeError("linetypes must be a list of dictionaries")
        self.__linetypes = value

