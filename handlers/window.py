"""File for making window"""
from PyQt6 import uic
from others import resource_path



class Window:
    """Class for making window"""
    open_windows = {}
    def __init__(self, path, database, name):
        self.name = name
        self.database = database
        # path = "design/registration.ui"
        form, windows = uic.loadUiType(resource_path(path))

        self.windows = windows()
        self.form = form()
        self.form.setupUi(self.windows)
        Window.open_windows[name] = {
            "window": self.windows,
            "form": self.form,
            "object": self,
        }

    def show(self):
        """
        show window
        :return: none
        """
        self.windows.show()
