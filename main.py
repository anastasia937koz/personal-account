"""File that is responsible for open file """
from PyQt6.QtWidgets import QApplication, QMessageBox, QTableWidgetItem
from dotenv import dotenv_values
from db.database import DataBase
from handlers.account import Account
from handlers.forgot_password import Password
from handlers.new_password import NewPassword
from handlers.regist import Registration
from handlers.sign_up import SignUp


config = dotenv_values(".env")

db = DataBase(config)
win = QApplication([])

login = SignUp("designs/regist.ui", db, "Войти")
account = Account("designs/personal_data.ui", db, "Личный кабинет")
regist = Registration("designs/registration.ui", db, "Регистрация")
forgot_password = Password("designs/password.ui", db, "Забыли пароль")
new_password = NewPassword("designs/new_password.ui", db, "Новый пароль")
login.show()
win.exec()
