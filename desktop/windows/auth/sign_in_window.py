from PyQt5.QtCore import QRect, Qt
from PyQt5.QtWidgets import QLabel, QLineEdit, QPushButton
from desktop.windows import BaseWindow, StartWindowMixin


class SignInWindow(BaseWindow, StartWindowMixin):
    def click_sign_in(self, nickname: QLineEdit, password: QLineEdit):
        sign_in_info = self.read_sign_in_info(nickname, password)
        # for client request

    def read_sign_in_info(self, nickname: QLineEdit, password: QLineEdit) -> str:
        sign_in_info = f"{nickname.text()}, {password.text()}"
        nickname.setText("")
        password.setText("")
        return sign_in_info

    def setup_nickname_input(self) -> QLineEdit:
        self.window.nickname_input = QLineEdit(self.window)
        self.window.nickname_input.setGeometry(QRect(230, 190, 320, 30))
        self.window.nickname_input.setPlaceholderText("Nickname")
        self.window.nickname_input.setStyleSheet(
            "border-style: outset;\n"
            "border-color: rgb(192, 192, 192);\n"
            "border-radius: 5px;\n"
            "border-width: 2px;\n"
            'font: 11pt "Ubuntu Regular";\n'
            "color: rgb(128, 128, 128)"
        )
        return self.window.nickname_input

    def setup_password_input(self) -> QLineEdit:
        self.window.password_input = QLineEdit(self.window)
        self.window.password_input.setGeometry(QRect(230, 240, 320, 30))
        self.window.password_input.setEchoMode(QLineEdit.Password)
        self.window.password_input.setPlaceholderText("Password")
        self.window.password_input.setStyleSheet(
            "border-style: outset;\n"
            "border-color: rgb(192, 192, 192);\n"
            "border-radius: 5px;\n"
            "border-width: 2px;\n"
            'font: 11pt "Ubuntu Regular";\n'
            "color: rgb(128, 128, 128)"
        )
        return self.window.password_input

    def setup_sign_in_button(self, nickname, password):
        self.window.sign_in = QPushButton(
            self.window, clicked=lambda: self.click_sign_in(nickname, password)
        )
        self.window.sign_in.setGeometry(QRect(320, 310, 140, 40))
        self.window.sign_in.setText("Sign In")
        self.window.sign_in.setStyleSheet(
            "color: rgb(250, 255, 255);\n"
            "background-color: rgb(167, 10, 61);\n"
            "border-style: outset;\n"
            "border-radius: 10px;\n"
            'font: 14pt "Arial";'
        )

    def setup_return_button(self):
        self.window.return_to_start_menu_but = QPushButton(
            self.window,
            clicked=lambda: self.return_to_start_window(self.client, self.window),
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

    def setup_server_response_label(self):
        self.window.server_response = QLabel(self.window)
        self.window.server_response.setGeometry(QRect(270, 160, 251, 22))
        self.window.server_response.setStyleSheet('font: 11pt "Ubuntu Regular";')
        self.window.server_response.setAlignment(Qt.AlignCenter)
        self.window.server_response.setVisible(False)
        # for show server_response to user after click sign_in

    def setup_sign_in_window(self):
        self.setup_window("Logging In")
        self.setup_title("Sign In", 110)
        nickname = self.setup_nickname_input()
        password = self.setup_password_input()
        self.setup_server_response_label()
        self.setup_sign_in_button(nickname, password)
        self.setup_return_button()
