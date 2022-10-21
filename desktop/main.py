import asyncio
from PyQt5 import QtWidgets
from desktop.windows.start_window import StartWindow


async def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    client = None
    start_window = StartWindow(client)
    start_window.setup_ui()
    start_window.window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    asyncio.run(main())
