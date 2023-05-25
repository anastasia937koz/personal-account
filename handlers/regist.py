"""File for making new personal account"""
from PyQt6.QtWidgets import QFileDialog, QMessageBox, QLineEdit
from handlers.window import Window



class Registration(Window):
    """Class for making new personal account """
    def __init__(self, path, database, name):
        super().__init__(path, database, name)
        self.form.photo.clicked.connect(self.show_dialog)
        self.form.to_registr.clicked.connect(self.to_regist)
        self.photo_path = ""

    def show_dialog(self):
        """
        show photo path
        :return: none
        """
        fname = QFileDialog.getOpenFileName(self.windows, "Выбрать файл", "/")
        self.photo_path = fname[0]
        way = self.photo_path.split("/")[-1]
        self.form.description.setText(way)

    def to_regist(self):
        """
        making new personal account
        :return: none
        """
        name = self.form.name.text()
        surname = self.form.surname.text()
        birth = self.form.birth.text()
        email = self.form.email.text()
        login = self.form.login.text()
        password = self.form.password.text()
        photo = self.photo_path
        try:
            self.database.add_regist(name, surname, birth, email, photo, login, password)
            Window.open_windows["Личный кабинет"]["object"].setter(
                name, surname, birth, email, photo, login
            )
            self.clear_line_edits()
            Window.open_windows["Регистрация"]["window"].hide()
            Window.open_windows["Личный кабинет"]["window"].show()
        except ValueError:
            box1 = QMessageBox()
            box1.setText("Не верный логин, пароль или почта")
            box1.setStandardButtons(QMessageBox.StandardButton.Ok)
            box1.setIcon(QMessageBox.Icon.Warning)
            box1.exec()

    def clear_line_edits(self):
        for widget in self.windows.findChildren(QLineEdit):
            widget.clear()


