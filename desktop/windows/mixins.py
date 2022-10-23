class StartWindowMixin:

    def return_to_start_window(self, client, curr_window):
        from desktop.windows.start_window import StartWindow
        self.start_window = StartWindow(client)
        self.start_window.setup_start_window()
        self.start_window.window.show()
        curr_window.close()
