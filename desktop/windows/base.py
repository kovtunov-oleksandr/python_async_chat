from PyQt5.QtWidgets import QMainWindow


class BaseWindow(QMainWindow):
    def __init__(self, client):
        super().__init__()
        self.client = client
