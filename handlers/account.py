"""File for entrance in personal account"""
from PyQt6.QtGui import QPixmap
from handlers.window import Window



class Account(Window):
    """Class for making personal account"""
    def __init__(self, path, database, name):
        super().__init__(path, database, name)
        self.form.exit.clicked.connect(self.exit)

    def setter(self,*args):
        """
        setting data about person
        :param args:list of userdata
        :return:none
        """
        name, surname, birth, email, photo, login =args
        self.form.login.setText(login)
        self.form.name.setText(name)
        self.form.surname.setText(surname)
        self.form.birth.setText(birth)
        self.form.email.setText(email)
        photo1 = QPixmap(photo)
        self.form.photo.setPixmap(photo1)

    def exit(self):
        """
        open sign up window for new user
        :return: none
        """
        Window.open_windows["Личный кабинет"]["window"].hide()
        Window.open_windows["Войти"]["object"].cleaning()
        Window.open_windows["Войти"]["window"].show()
