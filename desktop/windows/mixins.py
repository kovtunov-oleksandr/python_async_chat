class StartWindowMixin:

    def return_to_start_window(self, client, curr_window):
        from desktop.windows.start_window import StartWindowHandler
        self.start_window = StartWindowHandler(client)
        self.start_window.setup_window()
        self.start_window.window.show()
        curr_window.close()
