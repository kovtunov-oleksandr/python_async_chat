from PyQt5.QtCore import QRect
from PyQt5.QtWidgets import QLabel, QPushButton
from desktop.windows import BaseWindow
from desktop.windows.auth.sign_up_window import SignUpWindow
from desktop.windows.auth.sign_in_window import SignInWindow


class StartWindow(BaseWindow):
    def __init__(self, client):
        super().__init__(client)
        self.client = client

    def open_sign_in_menu(self):
        self.window = SignInWindow(self.client)
        self.window.setup_ui()
        self.window.show()
        self.close()

    def open_sign_up_menu(self):
        self.window = SignUpWindow(self.client)
        self.window.setup_ui()
        self.window.show()
        self.close()

    def setup_ui(self):
        self.setWindowTitle("Welcome Menu")
        self.resize(800, 600)
        self.setStyleSheet(
            "background-color: rgb(244, 244, 244);\n" "color: rgb(27, 28, 28);"
        )

        self.title = QLabel(self)
        self.title.setGeometry(QRect(170, 160, 450, 50))
        self.title.setText("Welcome to BeetrootAcademy Chat!")
        self.title.setStyleSheet(
            "\n" "color: rgb(0, 0, 0);\n" 'font: 18pt ".SF NS Text";'
        )

        self.sign_in = QPushButton(self, clicked=self.open_sign_in_menu)
        self.sign_in.setText("Sign In")
        self.sign_in.setGeometry(QRect(310, 260, 181, 41))
        self.sign_in.setStyleSheet(
            "color: rgb(250, 255, 255);\n"
            "background-color: rgb(167, 10, 61);\n"
            "border-style: outset;\n"
            "border-radius: 10px;\n"
            'font: 14pt "Arial";'
        )

        self.sign_up = QPushButton(self, clicked=self.open_sign_in_menu)
        self.sign_up.setText("Sign Up")
        self.sign_up.setGeometry(QRect(310, 310, 181, 41))
        self.sign_up.setStyleSheet(
            "color: rgb(250, 255, 255);\n"
            "background-color: rgb(167, 10, 61);\n"
            "border-style:outset;\n"
            "border-radius:10px;\n"
            'font: 14pt "Arial";'
        )
