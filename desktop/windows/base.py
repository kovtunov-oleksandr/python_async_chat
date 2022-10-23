from PyQt5.QtWidgets import QMainWindow, QLabel
from PyQt5.QtCore import QRect, Qt


class BaseWindow:
    def __init__(self, client):
        self.client = client
        self.window = QMainWindow()

    def setup_window(self, window_title: str):
        self.window.resize(800, 600)
        self.window.setWindowTitle(window_title)
        self.window.setStyleSheet(
            "background-color: rgb(244, 244, 244);\n" "color: rgb(27, 28, 28);"
        )

    def setup_title(self, title: str, height: int):
        self.window.title = QLabel(self.window)
        self.window.title.setGeometry(QRect(170, height, 450, 50))
        self.window.title.setAlignment(Qt.AlignCenter)
        self.window.title.setText(title)
        self.window.title.setStyleSheet(
            "\n" "color: rgb(0, 0, 0);\n" 'font: 18pt ".SF NS Text";'
        )
