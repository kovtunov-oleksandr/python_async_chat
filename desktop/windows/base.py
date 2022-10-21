from PyQt5.QtWidgets import QMainWindow


class BaseWindow:
    def __init__(self, client):
        self.client = client

    @staticmethod
    def create_window():
        return QMainWindow()
