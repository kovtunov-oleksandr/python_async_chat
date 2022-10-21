from PyQt5.QtCore import QRect
from PyQt5.QtWidgets import QLabel, QPushButton
from desktop.windows import BaseWindow, StartWindowMixin
from desktop.windows.auth.sign_up_window import SignUpWindow
from desktop.windows.auth.sign_in_window import SignInWindow


class StartWindow(BaseWindow, StartWindowMixin):
    def __init__(self, client):
        super().__init__(client)
        self.window = self.create_window()

    def open_sign_in_menu(self):
        sign_in_window = SignInWindow(self.client)
        sign_in_window.setup_ui()
        sign_in_window.window.show()
        self.window.close()

    def open_sign_up_menu(self):
        sign_up_window = SignUpWindow(self.client)
        sign_up_window.setup_ui()
        sign_up_window.window.show()
        self.window.close()

    def setup_ui(self):
        self.window.setWindowTitle("Welcome Menu")
        self.window.resize(800, 600)
        self.window.setStyleSheet(
            "background-color: rgb(244, 244, 244);\n" "color: rgb(27, 28, 28);"
        )

        self.window.title = QLabel(self.window)
        self.window.title.setGeometry(QRect(170, 160, 450, 50))
        self.window.title.setText("Welcome to BeetrootAcademy Chat!")
        self.window.title.setStyleSheet(
            "\n" "color: rgb(0, 0, 0);\n" 'font: 18pt ".SF NS Text";'
        )

        self.window.sign_in = QPushButton(self.window, clicked=self.open_sign_in_menu)
        self.window.sign_in.setText("Sign In")
        self.window.sign_in.setGeometry(QRect(310, 260, 181, 41))
        self.window.sign_in.setStyleSheet(
            "color: rgb(250, 255, 255);\n"
            "background-color: rgb(167, 10, 61);\n"
            "border-style: outset;\n"
            "border-radius: 10px;\n"
            'font: 14pt "Arial";'
        )

        self.window.sign_up = QPushButton(self.window, clicked=self.open_sign_up_menu)
        self.window.sign_up.setText("Sign Up")
        self.window.sign_up.setGeometry(QRect(310, 310, 181, 41))
        self.window.sign_up.setStyleSheet(
            "color: rgb(250, 255, 255);\n"
            "background-color: rgb(167, 10, 61);\n"
            "border-style:outset;\n"
            "border-radius:10px;\n"
            'font: 14pt "Arial";'
        )
