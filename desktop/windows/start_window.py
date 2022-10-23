from PyQt5.QtCore import QRect
from PyQt5.QtWidgets import QPushButton
from desktop.windows import BaseWindow, StartWindowMixin
from desktop.windows.auth import *


class StartWindow(BaseWindow, StartWindowMixin):
    def open_sign_in_menu(self):
        sign_in_window = SignInWindow(self.client)
        sign_in_window.setup_sign_in_window()
        sign_in_window.window.show()
        self.window.close()

    def open_sign_up_menu(self):
        sign_up_window = SignUpWindow(self.client)
        sign_up_window.setup_sign_up_window()
        sign_up_window.window.show()
        self.window.close()

    def setup_sign_in_button(self):
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

    def setup_sign_up_button(self):
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

    def setup_start_window(self):
        self.setup_window("Start Window")
        self.setup_title("Welcome to BeetrootAcademy Chat!", 160)
        self.setup_sign_in_button()
        self.setup_sign_up_button()
