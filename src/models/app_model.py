import geopandas as gpd
import pandas as pd


class AppDoc:
    def __init__(self,
                 layers: pd.DataFrame | None = None,
                 geometries: gpd.GeoDataFrame | None = None,
                 line_styles: pd.DataFrame | None = None
                 ):
        self.__layers = layers
        self.__geometries = geometries
        self.__line_styles = line_styles

    @property
    def geometries(self) -> gpd.GeoDataFrame:
        return self.__geometries

    @geometries.setter
    def geometries(self, value: gpd.GeoDataFrame | None) -> None:
        if not isinstance(value, gpd.GeoDataFrame):
            raise TypeError("geometries must be a GeoDataFrame object")
        self.__geometries = value

    @property
    def layers(self) -> pd.DataFrame:
        return self.__layers

    @layers.setter
    def layers(self, value: pd.DataFrame | None) -> None:
        if not isinstance(value, pd.DataFrame):
            raise TypeError("layers must be a DataFrame object")
        self.__layers = value

    @property
    def line_styles(self) -> pd.DataFrame:
        return self.__line_styles

    @line_styles.setter
    def line_styles(self, value: pd.DataFrame | None) -> None:
        if not isinstance(value, pd.DataFrame):
            raise TypeError("line_styles must be a DataFrame object")
        self.__line_styles = value
