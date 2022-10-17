from PyQt5 import QtCore, QtWidgets


class Ui_SignUpMenu(object):
    def __init__(self):
        self.ERROR_COLOR = "#a70a3d"
        self.SUCCESS_COLOR = "#94ceb9"

    def returnToStartMenu(self):
        from desktop.windows.start_window.start_window import Ui_AsynchronousChat

        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_AsynchronousChat()
        self.ui.setupUi(self.window)
        self.window.show()

    def clickSignUp(self, Status, Email, Nickname, Password, ConfirmPassword):
        self.readSignUpInfo(Email, Nickname, Password, ConfirmPassword)
        text = "..."
        status = self.showResponse(Status, text)
        # if status success -> show status, close sign up menu
        # elif status failed -> show status, remain sign up menu

    def readSignUpInfo(self, Email, Nickname, Password, ConfirmPassword):
        email = Email.text()
        nickname = Nickname.text()
        password = Password.text()
        password_confirm = ConfirmPassword.text()
        Email.setText("")
        Nickname.setText("")
        Password.setText("")
        ConfirmPassword.setText("")
        # client request is depend on

    def showResponse(self, Status, text):
        # depend on server response insert color into html code (if else)
        self.Status.setText(
            f'<html><head/><body><p><span style=" color:{self.SUCCESS_COLOR};">{text}</span></p></body></html>'
        )
        Status.setVisible(True)
        # depend on server response status might be returned (success/failed)

    def setupUi(self, SignUpMenu):
        SignUpMenu.setObjectName("SignUpMenu")
        SignUpMenu.resize(800, 600)
        SignUpMenu.setWindowTitle("Registration")
        SignUpMenu.setStyleSheet(
            "background-color: rgb(244, 244, 244);\n" "color: rgb(27, 28, 28);"
        )

        self.centralwidget = QtWidgets.QWidget(SignUpMenu)
        self.centralwidget.setObjectName("centralwidget")

        self.Lable = QtWidgets.QLabel(self.centralwidget)
        self.Lable.setGeometry(QtCore.QRect(170, 110, 450, 50))
        self.Lable.setAlignment(QtCore.Qt.AlignCenter)
        self.Lable.setStyleSheet(
            "\n" "color: rgb(0, 0, 0);\n" 'font: 18pt ".SF NS Text";'
        )
        self.Lable.setObjectName("Lable")
        self.Lable.setText("Sign Up")

        self.EmailInput = QtWidgets.QLineEdit(self.centralwidget)
        self.EmailInput.setGeometry(QtCore.QRect(230, 190, 320, 30))
        self.EmailInput.setStyleSheet(
            "border-style: outset;\n"
            "border-color: rgb(192, 192, 192);\n"
            "border-radius: 5px;\n"
            "border-width: 2px;\n"
            'font: 11pt "Ubuntu Regular";\n'
            "color: rgb(128, 128, 128)"
        )
        self.EmailInput.setObjectName("EmailInput")
        self.EmailInput.setPlaceholderText("Email")

        self.NicknameInput = QtWidgets.QLineEdit(self.centralwidget)
        self.NicknameInput.setGeometry(QtCore.QRect(230, 240, 320, 30))
        self.NicknameInput.setObjectName("NicknameInput")
        self.NicknameInput.setPlaceholderText("Nickname")
        self.NicknameInput.setStyleSheet(
            "border-style: outset;\n"
            "border-color: rgb(192, 192, 192);\n"
            "border-radius: 5px;\n"
            "border-width: 2px;\n"
            'font: 11pt "Ubuntu Regular";\n'
            "color: rgb(128, 128, 128)"
        )

        self.PasswordInput = QtWidgets.QLineEdit(self.centralwidget)
        self.PasswordInput.setGeometry(QtCore.QRect(230, 290, 320, 30))
        self.PasswordInput.setEchoMode(QtWidgets.QLineEdit.Password)
        self.PasswordInput.setObjectName("PasswordInput")
        self.PasswordInput.setPlaceholderText("Password")
        self.PasswordInput.setStyleSheet(
            "border-style: outset;\n"
            "border-color: rgb(192, 192, 192);\n"
            "border-radius: 5px;\n"
            "border-width: 2px;\n"
            'font: 11pt "Ubuntu Regular";\n'
            "color: rgb(128, 128, 128)"
        )

        self.ConfirmPasswordInput = QtWidgets.QLineEdit(self.centralwidget)
        self.ConfirmPasswordInput.setGeometry(QtCore.QRect(230, 340, 320, 30))
        self.ConfirmPasswordInput.setEchoMode(QtWidgets.QLineEdit.Password)
        self.ConfirmPasswordInput.setObjectName("ConfirmPasswordInput")
        self.ConfirmPasswordInput.setPlaceholderText("Repeat password")
        self.ConfirmPasswordInput.setStyleSheet(
            "border-style: outset;\n"
            "border-color: rgb(192, 192, 192);\n"
            "border-radius: 5px;\n"
            "border-width: 2px;\n"
            'font: 11pt "Ubuntu Regular";\n'
            "color: rgb(128, 128, 128)"
        )

        self.SignUp = QtWidgets.QPushButton(
            self.centralwidget,
            clicked=lambda: self.clickSignUp(
                self.Status,
                self.EmailInput,
                self.NicknameInput,
                self.PasswordInput,
                self.ConfirmPasswordInput,
            ),
        )
        self.SignUp.setGeometry(QtCore.QRect(320, 410, 140, 40))
        self.SignUp.setStyleSheet(
            "color: rgb(250, 255, 255);\n"
            "background-color: rgb(167, 10, 61);\n"
            "border-style:outset;\n"
            "border-radius:10px;\n"
            'font: 14pt "Arial";'
        )
        self.SignUp.setObjectName("SignUp")
        self.SignUp.setText("Sign Up")

        self.ReturnToStartMenu = QtWidgets.QPushButton(self.centralwidget)
        self.ReturnToStartMenu.clicked.connect(self.returnToStartMenu)
        self.ReturnToStartMenu.clicked.connect(SignUpMenu.close)
        self.ReturnToStartMenu.setGeometry(QtCore.QRect(320, 460, 140, 40))
        self.ReturnToStartMenu.setStyleSheet(
            "color: rgb(250, 255, 255);\n"
            "background-color: rgb(167, 10, 61);\n"
            "border-style: outset;\n"
            "border-radius: 10px;\n"
            'font: 14pt "Arial";'
        )
        self.ReturnToStartMenu.setObjectName("ReturnToStartMenu")
        self.ReturnToStartMenu.setText("Return")

        self.Status = QtWidgets.QLabel(self.centralwidget)
        self.Status.setGeometry(QtCore.QRect(270, 160, 251, 16))
        self.Status.setAlignment(QtCore.Qt.AlignCenter)
        self.Status.setObjectName("Status")
        self.Status.setVisible(False)

        SignUpMenu.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(SignUpMenu)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        SignUpMenu.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(SignUpMenu)
        self.statusbar.setObjectName("statusbar")
        SignUpMenu.setStatusBar(self.statusbar)

        QtCore.QMetaObject.connectSlotsByName(SignUpMenu)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    SignUpMenu = QtWidgets.QMainWindow()
    ui = Ui_SignUpMenu()
    ui.setupUi(SignUpMenu)
    SignUpMenu.show()
    sys.exit(app.exec_())
