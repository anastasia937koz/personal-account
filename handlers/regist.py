from handlers.window import Window
from PyQt6.QtWidgets import QFileDialog, QMessageBox


class Registration(Window):
    def __init__(self, path, db, name):
        super().__init__(path, db, name)
        self.form.photo.clicked.connect(self.showDialog)
        self.form.to_registr.clicked.connect(self.to_regist)
        self.photo_PATH = ""

    def showDialog(self):
        fname = QFileDialog.getOpenFileName(self.windows, "Выбрать файл", "/")
        self.photo_PATH = fname[0]
        way = self.photo_PATH.split("/")[-1]
        self.form.description.setText(way)

    def to_regist(self):
        name = self.form.name.text()
        surname = self.form.surname.text()
        birth = self.form.birth.text()
        email = self.form.email.text()
        login = self.form.login.text()
        password = self.form.password.text()
        photo = self.photo_PATH
        try:
            self.db.add_regist(name, surname, birth, email, photo, login, password)
            Window.open_windows["Личный кабинет"]["object"].setter(
                name, surname, birth, email, photo, login
            )
            Window.open_windows["Регистрация"]["window"].hide()
            Window.open_windows["Личный кабинет"]["window"].show()
        except ValueError:
            box1 = QMessageBox()
            box1.setText("Не верный логин, пароль или почта")
            box1.setStandardButtons(QMessageBox.StandardButton.Ok)
            box1.setIcon(QMessageBox.Icon.Warning)
            box1.exec()
