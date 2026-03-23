import sys

from src.app.application import Application

if __name__ == "__main__":
    app = Application()
    app.main_window.show()
    sys.exit(app.app.exec_())
