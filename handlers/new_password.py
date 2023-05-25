"""File for updating password"""
from PyQt6.QtWidgets import QMessageBox
from handlers.window import Window



class NewPassword(Window):
    """Class foe updatind new password"""
    def __init__(self, path, database, name):
        super().__init__(path, database, name)
        self.email=None
        self.form.save.clicked.connect(self.check_password)

    def set_email(self, email):
        """
        password memorization
        :param email:sequence of symbols
        :return:none
        """
        self.email = email

    def check_password(self):
        """
        checking of matching new password
        :return:none
        """
        if self.form.new_password.text() == self.form.new_password2.text():
            self.database.new_password(self.form.new_password.text(), self.email)
            self.windows.hide()
            Window.open_windows["Войти"]["window"].show()

        else:
            box1 = QMessageBox()
            box1.setText("Пароли не совпадают")
            box1.setStandardButtons(QMessageBox.StandardButton.Ok)
            box1.setIcon(QMessageBox.Icon.Warning)
            box1.exec()
