import sys

from PyQt6 import QtWidgets

from app import Application
from config import WINDOW_WIDTH, WINDOW_HEIGHT


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = Application()
    widget.setWindowTitle("Password Generator")
    widget.resize(WINDOW_WIDTH, WINDOW_HEIGHT)
    widget.show()

    sys.exit(app.exec())