from src.app.application import Application

if __name__ == "__main__":
    app = Application()
    app.dxf_controller.read_dxf()
    app.dxf_controller.convert_dxf_gpd()
    app.dxf_controller.clip_poygons()
    app.dxf_controller.convert_gpd_dxf()

