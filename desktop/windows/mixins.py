class StartWindowMixin:

    def return_to_start_menu(self, client, curr_window):
        from desktop.windows.start_window import StartWindow
        self.next_window = StartWindow(client)
        self.next_window.setup_ui()
        self.next_window.window.show()
        curr_window.close()
