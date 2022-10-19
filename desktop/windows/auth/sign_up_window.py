from PyQt5.QtCore import QRect, Qt
from PyQt5.QtWidgets import QLabel, QLineEdit, QPushButton
from desktop.windows import BaseWindow


class SignUpWindow(BaseWindow):
    def __init__(self, client):
        super().__init__(client)
        self.client = client

    def return_to_start_menu(self):
        from desktop.windows.start_window import StartWindow
        self.window = StartWindow(self.client)
        self.window.setup_ui()
        self.window.show()
        self.close()

    def click_sign_up(self, email: QLineEdit, nickname: QLineEdit, password: QLineEdit, confirm_password: QLineEdit):
        sign_up_info = self.read_sign_up_info(email, nickname, password, confirm_password)
        # for client request

    def read_sign_up_info(self, email: QLineEdit, nickname: QLineEdit, password: QLineEdit, confirm_password: QLineEdit):
        sign_up_info = f"{email.text()};;{nickname.text()};;{password.text()};;{confirm_password.text()}"
        email.setText("")
        nickname.setText("")
        password.setText("")
        confirm_password.setText("")
        return sign_up_info

    def setup_ui(self):
        self.resize(800, 600)
        self.setWindowTitle("Registration")
        self.setStyleSheet(
            "background-color: rgb(244, 244, 244);\n" "color: rgb(27, 28, 28);"
        )

        self.title = QLabel(self)
        self.title.setGeometry(QRect(170, 110, 450, 50))
        self.title.setAlignment(Qt.AlignCenter)
        self.title.setStyleSheet(
            "\n" "color: rgb(0, 0, 0);\n" 'font: 18pt ".SF NS Text";'
        )
        self.title.setText("Sign Up")

        self.email_input = QLineEdit(self)
        self.email_input.setGeometry(QRect(230, 190, 320, 30))
        self.email_input.setStyleSheet(
            "border-style: outset;\n"
            "border-color: rgb(192, 192, 192);\n"
            "border-radius: 5px;\n"
            "border-width: 2px;\n"
            'font: 11pt "Ubuntu Regular";\n'
            "color: rgb(128, 128, 128)"
        )
        self.email_input.setPlaceholderText("Email")

        self.nickname_input = QLineEdit(self)
        self.nickname_input.setGeometry(QRect(230, 240, 320, 30))
        self.nickname_input.setPlaceholderText("Nickname")
        self.nickname_input.setStyleSheet(
            "border-style: outset;\n"
            "border-color: rgb(192, 192, 192);\n"
            "border-radius: 5px;\n"
            "border-width: 2px;\n"
            'font: 11pt "Ubuntu Regular";\n'
            "color: rgb(128, 128, 128)"
        )

        self.password_input = QLineEdit(self)
        self.password_input.setGeometry(QRect(230, 290, 320, 30))
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setPlaceholderText("Password")
        self.password_input.setStyleSheet(
            "border-style: outset;\n"
            "border-color: rgb(192, 192, 192);\n"
            "border-radius: 5px;\n"
            "border-width: 2px;\n"
            'font: 11pt "Ubuntu Regular";\n'
            "color: rgb(128, 128, 128)"
        )

        self.confirm_password_input = QLineEdit(self)
        self.confirm_password_input.setGeometry(QRect(230, 340, 320, 30))
        self.confirm_password_input.setEchoMode(QLineEdit.Password)
        self.confirm_password_input.setPlaceholderText("Repeat password")
        self.confirm_password_input.setStyleSheet(
            "border-style: outset;\n"
            "border-color: rgb(192, 192, 192);\n"
            "border-radius: 5px;\n"
            "border-width: 2px;\n"
            'font: 11pt "Ubuntu Regular";\n'
            "color: rgb(128, 128, 128)"
        )

        self.sign_up = QPushButton(self, clicked=lambda: self.click_sign_up(
                self.email_input,
                self.nickname_input,
                self.password_input,
                self.confirm_password_input
            ))
        self.sign_up.setGeometry(QRect(320, 410, 140, 40))
        self.sign_up.setStyleSheet(
            "color: rgb(250, 255, 255);\n"
            "background-color: rgb(167, 10, 61);\n"
            "border-style:outset;\n"
            "border-radius:10px;\n"
            'font: 14pt "Arial";'
        )
        self.sign_up.setText("Sign Up")

        self.return_to_start_menu_but = QPushButton(self, clicked=self.return_to_start_menu)
        self.return_to_start_menu_but.setGeometry(QRect(320, 460, 140, 40))
        self.return_to_start_menu_but.setStyleSheet(
            "color: rgb(250, 255, 255);\n"
            "background-color: rgb(167, 10, 61);\n"
            "border-style: outset;\n"
            "border-radius: 10px;\n"
            'font: 14pt "Arial";'
        )
        self.return_to_start_menu_but.setText("Return")

        self.server_response = QLabel(self)
        self.server_response.setGeometry(QRect(270, 160, 251, 16))
        self.server_response.setAlignment(Qt.AlignCenter)
        self.server_response.setVisible(False)
        # for show server_response to user after click sign_in
