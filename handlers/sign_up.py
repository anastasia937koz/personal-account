from handlers.window import Window
from PyQt6.QtWidgets import QMessageBox

class Sign_up(Window):
    def __init__(self, path, db, name):
        super().__init__(path, db, name)
        self.form.enter.clicked.connect(self.enter)
        self.form.registration.clicked.connect(self.regist)
        self.form.forgotten_password.clicked.connect(self.password)




    def enter(self):
        if  self.db.check_login_password(self.form.login.text(), self.form.password.text()):
            name, surname, birth, email, photo = self.db.get_user_data(self.form.login.text(), self.form.password.text())
            Window.open_windows["Личный кабинет"]['object'].setter(name, surname, birth, email, photo, self.form.login.text())
            Window.open_windows["Войти"]["window"].hide()
            Window.open_windows["Личный кабинет"]["window"].show()
        else:
            box1 = QMessageBox()
            box1.setText('Не верный логин или пароль')
            box1.setStandardButtons(QMessageBox.StandardButton.Ok)
            box1.setIcon(QMessageBox.Icon.Warning)
            box1.exec()

    def regist(self):
        Window.open_windows["Войти"]["window"].hide()
        Window.open_windows["Регистрация"]["window"].show()


    def password(self):
        Window.open_windows["Войти"]["window"].hide()
        Window.open_windows["Забыли пароль"]["window"].show()

    def cleaning(self):
        self.form.login.setText("")
        self.form.password.setText("")



