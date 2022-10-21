from PyQt5.QtCore import QRect, Qt
from PyQt5.QtWidgets import QLabel, QLineEdit, QPushButton
from desktop.windows import BaseWindow, StartWindowMixin


class SignInWindow(BaseWindow, StartWindowMixin):
    def __init__(self, client):
        super().__init__(client)
        self.window = self.create_window()

    def click_sign_in(self, nickname: QLineEdit, password: QLineEdit):
        sign_in_info = self.read_sign_in_info(nickname, password)
        # for client request

    def read_sign_in_info(self, nickname: QLineEdit, password: QLineEdit):
        sign_in_info = f"{nickname.text()};;{password.text()}"
        nickname.setText("")
        password.setText("")
        return sign_in_info

    def setup_ui(self):
        self.window.resize(800, 600)
        self.window.setWindowTitle("Logging in")
        self.window.setStyleSheet(
            "background-color: rgb(244, 244, 244);\n" "color: rgb(27, 28, 28);"
        )

        self.window.title = QLabel(self.window)
        self.window.title.setGeometry(QRect(170, 110, 450, 50))
        self.window.title.setStyleSheet(
            "\n" "color: rgb(0, 0, 0);\n" 'font: 18pt ".SF NS Text";'
        )
        self.window.title.setAlignment(Qt.AlignHCenter)
        self.window.title.setText("Sign In")

        self.window.nickname_input = QLineEdit(self.window)
        self.window.nickname_input.setGeometry(QRect(230, 190, 320, 30))
        self.window.nickname_input.setStyleSheet(
            "border-style: outset;\n"
            "border-color: rgb(192, 192, 192);\n"
            "border-radius: 5px;\n"
            "border-width: 2px;\n"
            'font: 11pt "Ubuntu Regular";\n'
            "color: rgb(128, 128, 128)"
        )
        self.window.nickname_input.setPlaceholderText("Nickname")

        self.window.password_input = QLineEdit(self.window)
        self.window.password_input.setGeometry(QRect(230, 240, 320, 30))
        self.window.password_input.setStyleSheet(
            "border-style: outset;\n"
            "border-color: rgb(192, 192, 192);\n"
            "border-radius: 5px;\n"
            "border-width: 2px;\n"
            'font: 11pt "Ubuntu Regular";\n'
            "color: rgb(128, 128, 128)"
        )
        self.window.password_input.setEchoMode(QLineEdit.Password)
        self.window.password_input.setPlaceholderText("Password")

        self.window.sign_in = QPushButton(self.window, clicked=lambda: self.click_sign_in(
            self.window.nickname_input,
            self.window.password_input
        ))
        self.window.sign_in.setGeometry(QRect(320, 310, 140, 40))
        self.window.sign_in.setStyleSheet(
            "color: rgb(250, 255, 255);\n"
            "background-color: rgb(167, 10, 61);\n"
            "border-style: outset;\n"
            "border-radius: 10px;\n"
            'font: 14pt "Arial";'
        )
        self.window.sign_in.setText("Sign In")

        self.window.return_to_start_menu_but = QPushButton(
            self.window, clicked=lambda: self.return_to_start_menu(self.client, self.window)
        )
        self.window.return_to_start_menu_but.setGeometry(QRect(320, 360, 140, 40))
        self.window.return_to_start_menu_but.setStyleSheet(
            "color: rgb(250, 255, 255);\n"
            "background-color: rgb(167, 10, 61);\n"
            "border-style: outset;\n"
            "border-radius: 10px;\n"
            'font: 14pt "Arial";'
        )
        self.window.return_to_start_menu_but.setText("Return")

        self.window.server_response = QLabel(self.window)
        self.window.server_response.setGeometry(QRect(270, 160, 251, 22))
        self.window.server_response.setStyleSheet('font: 11pt "Ubuntu Regular";')
        self.window.server_response.setAlignment(Qt.AlignCenter)
        self.window.server_response.setVisible(False)
        # for show server_response to user after click sign_in
