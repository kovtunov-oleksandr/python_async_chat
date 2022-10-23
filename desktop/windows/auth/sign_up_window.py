from PyQt5.QtCore import QRect, Qt
from PyQt5.QtWidgets import QLabel, QLineEdit, QPushButton
from desktop.windows import BaseWindow, StartWindowMixin


class SignUpWindow(BaseWindow, StartWindowMixin):
    def click_sign_up(
        self,
        email: QLineEdit,
        nickname: QLineEdit,
        password: QLineEdit,
        confirm_password: QLineEdit,
    ):
        sign_up_info = self.read_sign_up_info(email, nickname, password, confirm_password)
        # for client request

    def read_sign_up_info(
        self,
        email: QLineEdit,
        nickname: QLineEdit,
        password: QLineEdit,
        confirm_password: QLineEdit,
    ) -> str:
        sign_up_info = f"{email.text()}, {nickname.text()}, {password.text()}, {confirm_password.text()}"
        email.setText("")
        nickname.setText("")
        password.setText("")
        confirm_password.setText("")
        return sign_up_info

    def setup_email_input(self) -> QLineEdit:
        self.window.email_input = QLineEdit(self.window)
        self.window.email_input.setGeometry(QRect(230, 190, 320, 30))
        self.window.email_input.setPlaceholderText("Email")
        self.window.email_input.setStyleSheet(
            "border-style: outset;\n"
            "border-color: rgb(192, 192, 192);\n"
            "border-radius: 5px;\n"
            "border-width: 2px;\n"
            'font: 11pt "Ubuntu Regular";\n'
            "color: rgb(128, 128, 128)"
        )
        return self.window.email_input

    def setup_nickname_input(self) -> QLineEdit:
        self.window.nickname_input = QLineEdit(self.window)
        self.window.nickname_input.setGeometry(QRect(230, 240, 320, 30))
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
        self.window.password_input.setGeometry(QRect(230, 290, 320, 30))
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

    def setup_confirm_password_input(self) -> QLineEdit:
        self.window.confirm_password_input = QLineEdit(self.window)
        self.window.confirm_password_input.setGeometry(QRect(230, 340, 320, 30))
        self.window.confirm_password_input.setEchoMode(QLineEdit.Password)
        self.window.confirm_password_input.setPlaceholderText("Repeat password")
        self.window.confirm_password_input.setStyleSheet(
            "border-style: outset;\n"
            "border-color: rgb(192, 192, 192);\n"
            "border-radius: 5px;\n"
            "border-width: 2px;\n"
            'font: 11pt "Ubuntu Regular";\n'
            "color: rgb(128, 128, 128)"
        )
        return self.window.confirm_password_input

    def setup_sign_up_button(self, email, nickname, password, confirm_password):
        self.window.sign_up = QPushButton(
            self.window,
            clicked=lambda: self.click_sign_up(
                email, nickname, password, confirm_password
            ),
        )
        self.window.sign_up.setGeometry(QRect(320, 410, 140, 40))
        self.window.sign_up.setText("Sign Up")
        self.window.sign_up.setStyleSheet(
            "color: rgb(250, 255, 255);\n"
            "background-color: rgb(167, 10, 61);\n"
            "border-style:outset;\n"
            "border-radius:10px;\n"
            'font: 14pt "Arial";'
        )

    def setup_return_button(self):
        self.window.return_to_start_menu_but = QPushButton(
            self.window,
            clicked=lambda: self.return_to_start_window(self.client, self.window),
        )
        self.window.return_to_start_menu_but.setGeometry(QRect(320, 460, 140, 40))
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
        self.window.server_response.setGeometry(QRect(270, 160, 251, 16))
        self.window.server_response.setAlignment(Qt.AlignCenter)
        self.window.server_response.setVisible(False)
        # for show server_response to user after click sign_in

    def setup_sign_up_window(self):
        self.setup_window("Registration")
        self.setup_title("Sign Up", 110)
        email = self.setup_email_input()
        nickname = self.setup_nickname_input()
        password = self.setup_password_input()
        confirm_password = self.setup_confirm_password_input()
        self.setup_server_response_label()
        self.setup_sign_up_button(email, nickname, password, confirm_password)
        self.setup_return_button()
