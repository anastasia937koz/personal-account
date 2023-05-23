from handlers.window import Window
from PyQt6.QtGui import QPixmap


class Account(Window):
    def __init__(self, path, db, name):
        super().__init__(path, db, name)
        self.form.exit.clicked.connect(self.exit)

    def setter(self, name, surname, birth, email, photo, login):
        self.form.login.setText(login)
        self.form.name.setText(name)
        self.form.surname.setText(surname)
        self.form.birth.setText(birth)
        self.form.email.setText(email)
        photo1 = QPixmap(photo)
        self.form.photo.setPixmap(photo1)

    def exit(self):
        Window.open_windows["Личный кабинет"]["window"].hide()
        Window.open_windows["Войти"]["object"].cleaning()
        Window.open_windows["Войти"]["window"].show()
