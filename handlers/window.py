from others import resource_path

from PyQt6 import uic


class Window:
    open_windows = {}

    def __init__(self, path, db, name):
        self.name = name
        self.db = db
        # path = "design/registration.ui"
        Form, Windows = uic.loadUiType(resource_path(path))

        self.windows = Windows()
        self.form = Form()
        self.form.setupUi(self.windows)
        Window.open_windows[name] = {
            "window": self.windows,
            "form": self.form,
            "object": self,
        }

    def show(self):
        self.windows.show()
