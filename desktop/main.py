import asyncio
import sys
from PyQt5 import QtWidgets
from desktop.windows.start_window import StartWindow


async def main():
    app = QtWidgets.QApplication(sys.argv)
    client = None
    start_window = StartWindow(client)
    start_window.setup_start_window()
    start_window.window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    asyncio.run(main())
