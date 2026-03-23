import geopandas as gpd
from shapely import Polygon
from src.models.app_model import AppDoc


class DXFProcessor:
    """Processor manipulates autocad objects
    it current version it realises these functions:
    - clip horisontals inside polygons
    """

    @staticmethod
    def clip_polygon_areas(doc: AppDoc, settings: dict) -> None:
        """
        select every closed line from user SETTINGS with selector
        convert closed lines into polygons
        select every line from user SETTINGS
        clip every line inside polygone
        replace old lines in doc
        :return: None
        """

        polygon_selector = (
                (doc.geometries.geometry.geom_type == "LineString") &
                (doc.geometries["is_closed"] &
                 (doc.geometries.layer == settings["polygons"]))
        )

        line_selecor = (
                (doc.geometries.geometry.geom_type == "LineString") &
                (doc.geometries.layer == settings["lines"])
        )
        doc.geometries.loc[polygon_selector, "geometry"] = doc.geometries.loc[polygon_selector, "geometry"].apply(
            lambda geometry: Polygon(geometry.coords))
        polygons = doc.geometries[polygon_selector]
        lines = doc.geometries[line_selecor]

        # TODO use sjoin + intersection for better perfomanse in future versions
        new_lines = gpd.overlay(lines, polygons, how='difference')
        doc.geometries.drop(list(lines.index.values), axis='rows', inplace=True)
        doc.geometries = gpd.pd.concat(objs=[doc.geometries, new_lines], ignore_index=True)

        # new_lines.to

    @staticmethod
    def explode_multilines(doc: AppDoc, settings: dict):
        """
        explode multilines
        replace doc old multilines to new lines
        :param doc: application document
        :param settings: chosen layer in wich to explode multilines
        :return:
        """
        layer = settings.get("lines")

        multilines_selector = (
                (doc.geometries.geometry.geom_type == "MultiLineString") &
                (doc.geometries.layer == layer)
        )
        multilines = doc.geometries[multilines_selector]
        new_lines = doc.geometries[multilines_selector].explode(ignore_index=True)
        doc.geometries.drop(list(multilines.index.values), axis="rows", inplace=True)
        doc.geometries = gpd.pd.concat(objs=[doc.geometries, new_lines], ignore_index=True)
