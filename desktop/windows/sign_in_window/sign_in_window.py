from PyQt5 import QtCore, QtWidgets


class Ui_SignInMenu(object):
    def __init__(self):
        self.ERROR_COLOR = "#a70a3d"
        self.SUCCESS_COLOR = "#94ceb9"

    def returnToStartMenu(self):
        from desktop.windows.start_window.start_window import Ui_AsynchronousChat

        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_AsynchronousChat()
        self.ui.setupUi(self.window)
        self.window.show()

    def clickSignIn(self, Status, Nickname, Password):
        self.readSignInInfo(Nickname, Password)
        text = "..."
        status = self.showResponse(Status, text)
        # if status success -> show status, close sign in menu
        # elif status failed -> show status, remain sign in menu

    def readSignInInfo(self, Nickname, Password):
        nickname = Nickname.text()
        password = Password.text()
        Nickname.setText("")
        Password.setText("")

    def showResponse(self, Status, text):
        # depend on server response insert color into html code (if else)
        self.Status.setText(
            f'<html><head/><body><p><span style=" color:{self.SUCCESS_COLOR};">{text}</span></p></body></html>'
        )
        Status.setVisible(True)
        # depend on server response status might be returned (success/failed)

    def setupUi(self, SignInMenu):
        SignInMenu.setObjectName("SignInMenu")
        SignInMenu.resize(800, 600)
        SignInMenu.setWindowTitle("Logging in")
        SignInMenu.setStyleSheet(
            "background-color: rgb(244, 244, 244);\n" "color: rgb(27, 28, 28);"
        )

        self.centralwidget = QtWidgets.QWidget(SignInMenu)
        self.centralwidget.setObjectName("centralwidget")

        self.Lable = QtWidgets.QLabel(self.centralwidget)
        self.Lable.setGeometry(QtCore.QRect(170, 110, 450, 50))
        self.Lable.setStyleSheet(
            "\n" "color: rgb(0, 0, 0);\n" 'font: 18pt ".SF NS Text";'
        )
        self.Lable.setAlignment(QtCore.Qt.AlignCenter)
        self.Lable.setObjectName("Lable")
        self.Lable.setText("Sign In")

        self.NicknameInput = QtWidgets.QLineEdit(self.centralwidget)
        self.NicknameInput.setGeometry(QtCore.QRect(230, 190, 320, 30))
        self.NicknameInput.setStyleSheet(
            "border-style: outset;\n"
            "border-color: rgb(192, 192, 192);\n"
            "border-radius: 5px;\n"
            "border-width: 2px;\n"
            'font: 11pt "Ubuntu Regular";\n'
            "color: rgb(128, 128, 128)"
        )
        self.NicknameInput.setObjectName("NicknameInput")
        self.NicknameInput.setPlaceholderText("Nickname")

        self.PasswordInput = QtWidgets.QLineEdit(self.centralwidget)
        self.PasswordInput.setGeometry(QtCore.QRect(230, 240, 320, 30))
        self.PasswordInput.setStyleSheet(
            "border-style: outset;\n"
            "border-color: rgb(192, 192, 192);\n"
            "border-radius: 5px;\n"
            "border-width: 2px;\n"
            'font: 11pt "Ubuntu Regular";\n'
            "color: rgb(128, 128, 128)"
        )
        self.PasswordInput.setEchoMode(QtWidgets.QLineEdit.Password)
        self.PasswordInput.setObjectName("PasswordInput")
        self.PasswordInput.setPlaceholderText("Password")

        self.SignIn = QtWidgets.QPushButton(
            self.centralwidget,
            clicked=lambda: self.clickSignIn(
                self.Status, self.NicknameInput, self.PasswordInput
            ),
        )
        self.SignIn.setGeometry(QtCore.QRect(320, 310, 140, 40))
        self.SignIn.setStyleSheet(
            "color: rgb(250, 255, 255);\n"
            "background-color: rgb(167, 10, 61);\n"
            "border-style: outset;\n"
            "border-radius: 10px;\n"
            'font: 14pt "Arial";'
        )
        self.SignIn.setObjectName("SignIn")
        self.SignIn.setText("Sign In")

        self.ReturnToStartMenu = QtWidgets.QPushButton(self.centralwidget)
        self.ReturnToStartMenu.clicked.connect(self.returnToStartMenu)
        self.ReturnToStartMenu.clicked.connect(SignInMenu.close)
        self.ReturnToStartMenu.setGeometry(QtCore.QRect(320, 360, 140, 40))
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
        self.Status.setGeometry(QtCore.QRect(270, 160, 251, 22))
        self.Status.setStyleSheet('font: 11pt "Ubuntu Regular";')
        self.Status.setAlignment(QtCore.Qt.AlignCenter)
        self.Status.setObjectName("Status")
        self.Status.setVisible(False)

        SignInMenu.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(SignInMenu)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        SignInMenu.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(SignInMenu)
        self.statusbar.setObjectName("statusbar")
        SignInMenu.setStatusBar(self.statusbar)

        QtCore.QMetaObject.connectSlotsByName(SignInMenu)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    SignInMenu = QtWidgets.QMainWindow()
    ui = Ui_SignInMenu()
    ui.setupUi(SignInMenu)
    SignInMenu.show()
    sys.exit(app.exec_())
