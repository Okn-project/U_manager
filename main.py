import sys
import traceback
import os
# sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))
from src.app.application import Application

if __name__ == "__main__":
    app = Application()
    app.main_window.show()
    sys.exit(app.app.exec_())
