from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import QPushButton

0

class Ui_ChatWindow(object):

    def setupUi(self, ChatWindow):
        ChatWindow.setObjectName("ChatWindow")
        ChatWindow.resize(500, 600)
        ChatWindow.setStyleSheet("background-color: rgb(176, 255, 250);")
        self.centralwidget = QtWidgets.QWidget(ChatWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_send_msg = QtWidgets.QPushButton(self.centralwidget)
        self.btn_send_msg.setGeometry(QtCore.QRect(440, 510, 51, 27))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setKerning(False)
        self.btn_send_msg.setFont(font)
        self.btn_send_msg.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_send_msg.setStyleSheet("background-color: rgb(255, 242, 99);")
        self.btn_send_msg.setLocale(QtCore.QLocale(QtCore.QLocale.Ukrainian, QtCore.QLocale.Ukraine))
        self.btn_send_msg.setObjectName("btn_send_msg")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 0, 481, 481))
        self.plainTextEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 490, 421, 61))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")
        ChatWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ChatWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 21))
        self.menubar.setObjectName("menubar")
        ChatWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ChatWindow)
        self.statusbar.setObjectName("statusbar")
        ChatWindow.setStatusBar(self.statusbar)

        self.retranslateUi(ChatWindow)
        QtCore.QMetaObject.connectSlotsByName(ChatWindow)

    def retranslateUi(self, ChatWindow):
        _translate = QtCore.QCoreApplication.translate
        ChatWindow.setWindowTitle(_translate("ChatWindow", "MainWindow"))
        self.btn_send_msg.setText(_translate("ChatWindow", ">>>"))
        self.btn_send_msg.clicked.connect(self.send_message)
        self.btn_send_msg.setShortcut('Return')

    def send_message(self):
        self.plainTextEdit.appendPlainText(
            self.lineEdit.text()
        )

        self.lineEdit.clear()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ChatWindow = QtWidgets.QMainWindow()
    ui = Ui_ChatWindow()
    ui.setupUi(ChatWindow)
    ChatWindow.show()
    sys.exit(app.exec_())
