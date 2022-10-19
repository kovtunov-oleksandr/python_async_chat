import asyncio
from PyQt5 import QtWidgets
from desktop.windows.start_window import StartWindow


async def main():
    if __name__ == "__main__":
        import sys
        app = QtWidgets.QApplication(sys.argv)
        client = None
        window = StartWindow(client)
        window.setup_ui()
        window.show()
        sys.exit(app.exec_())


asyncio.run(main())
