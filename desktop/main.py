import asyncio
import sys
from PyQt5 import QtWidgets
from desktop.windows.start_window import StartWindowHandler


async def main():
    app = QtWidgets.QApplication(sys.argv)
    client = None
    start_window = StartWindowHandler(client)
    start_window.setup_window()
    start_window.window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    asyncio.run(main())
