"""File for entrance an account"""
from PyQt6.QtWidgets import QMessageBox
from handlers.window import Window



class SignUp(Window):
    """Class for entrance an existing account"""
    def __init__(self, path, database, name):
        super().__init__(path, database, name)
        self.form.enter.clicked.connect(self.enter)
        self.form.registration.clicked.connect(self.regist)
        self.form.forgotten_password.clicked.connect(self.password)

    def enter(self):
        """
        entrance an existing account
        :return: none
        """
        if self.database.check_login_password(
            self.form.login.text(), self.form.password.text()
        ):
            name, surname, birth, email, photo = self.database.get_user_data(
                self.form.login.text(), self.form.password.text()
            )
            Window.open_windows["Личный кабинет"]["object"].setter(
                name, surname, birth, email, photo, self.form.login.text()
            )
            Window.open_windows["Войти"]["window"].hide()
            Window.open_windows["Личный кабинет"]["window"].show()
        else:
            box1 = QMessageBox()
            box1.setText("Не верный логин или пароль")
            box1.setStandardButtons(QMessageBox.StandardButton.Ok)
            box1.setIcon(QMessageBox.Icon.Warning)
            box1.exec()

    def regist(self):
        """
        open registration window
        :return: none
        """
        Window.open_windows["Войти"]["window"].hide()
        Window.open_windows["Регистрация"]["window"].show()

    def password(self):
        """
        open window for making new password
        :return: none
        """
        Window.open_windows["Войти"]["window"].hide()
        Window.open_windows["Забыли пароль"]["window"].show()

    def cleaning(self):
        """
        cleaning window from text
        :return: none
        """
        self.form.login.setText("")
        self.form.password.setText("")
