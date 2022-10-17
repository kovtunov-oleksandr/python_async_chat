from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from desktop.windows.sign_up_window.sign_up_window import Ui_SignUpMenu
from desktop.windows.sign_in_window.sign_in_window import Ui_SignInMenu


class Ui_AsynchronousChat(QMainWindow):
    def openSignInMenu(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_SignInMenu()
        self.ui.setupUi(self.window)
        self.window.show()

    def openSignUpMenu(self):
        self.window1 = QtWidgets.QMainWindow()
        self.ui = Ui_SignUpMenu()
        self.ui.setupUi(self.window1)
        self.window1.show()

    def setupUi(self, AsynchronousChat):
        AsynchronousChat.setObjectName("AsynchronousChat")
        AsynchronousChat.setWindowTitle("Welcome Menu")
        AsynchronousChat.resize(800, 600)
        AsynchronousChat.setStyleSheet(
            "background-color: rgb(244, 244, 244);\n" "color: rgb(27, 28, 28);"
        )

        self.centralwidget = QtWidgets.QWidget(AsynchronousChat)
        self.centralwidget.setObjectName("centralwidget")

        self.Lable = QtWidgets.QLabel(self.centralwidget)
        self.Lable.setGeometry(QtCore.QRect(170, 160, 450, 50))
        self.Lable.setAlignment(QtCore.Qt.AlignCenter)
        self.Lable.setObjectName("Lable")
        self.Lable.setText("Welcome to BeetrootAcademy Chat!")
        self.Lable.setStyleSheet(
            "\n" "color: rgb(0, 0, 0);\n" 'font: 18pt ".SF NS Text";'
        )

        self.SignIn = QtWidgets.QPushButton(self.centralwidget)
        self.SignIn.setText("Sign In")
        self.SignIn.setGeometry(QtCore.QRect(310, 260, 181, 41))
        self.SignIn.setStyleSheet(
            "color: rgb(250, 255, 255);\n"
            "background-color: rgb(167, 10, 61);\n"
            "border-style: outset;\n"
            "border-radius: 10px;\n"
            'font: 14pt "Arial";'
        )
        self.SignIn.setObjectName("Sign In")
        self.SignIn.clicked.connect(self.openSignInMenu)
        self.SignIn.clicked.connect(AsynchronousChat.close)

        self.SignUp = QtWidgets.QPushButton(self.centralwidget)
        self.SignUp.setText("Sign Up")
        self.SignUp.setGeometry(QtCore.QRect(310, 310, 181, 41))
        self.SignUp.setStyleSheet(
            "color: rgb(250, 255, 255);\n"
            "background-color: rgb(167, 10, 61);\n"
            "border-style:outset;\n"
            "border-radius:10px;\n"
            'font: 14pt "Arial";'
        )
        self.SignUp.setObjectName("Sign Up")
        self.SignUp.clicked.connect(self.openSignUpMenu)
        self.SignUp.clicked.connect(AsynchronousChat.close)

        AsynchronousChat.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(AsynchronousChat)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        AsynchronousChat.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(AsynchronousChat)
        self.statusbar.setObjectName("statusbar")
        AsynchronousChat.setStatusBar(self.statusbar)


def main():
    if __name__ == "__main__":
        import sys

        app = QtWidgets.QApplication(sys.argv)
        AsynchronousChat = QtWidgets.QMainWindow()
        ui = Ui_AsynchronousChat()
        ui.setupUi(AsynchronousChat)
        AsynchronousChat.show()
        sys.exit(app.exec_())


main()
