from handlers.window import Window
from PyQt6.QtWidgets import QMessageBox


class New_password(Window):
    def __init__(self, path, db, name):
        super().__init__(path, db, name)
        self.form.save.clicked.connect(self.check_password)

    def set_email(self, email):
        self.email = email

    def check_password(self):
        if self.form.new_password.text() == self.form.new_password2.text():
            self.db.new_password(self.form.new_password.text(), self.email)
            self.windows.hide()
            Window.open_windows["Войти"]["window"].show()

        else:
            box1 = QMessageBox()
            box1.setText("Пароли не совпадают")
            box1.setStandardButtons(QMessageBox.StandardButton.Ok)
            box1.setIcon(QMessageBox.Icon.Warning)
            box1.exec()
