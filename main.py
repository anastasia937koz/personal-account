from db.data_base import Data_base

from PyQt6.QtWidgets import QApplication, QMessageBox, QTableWidgetItem

from handlers.account import Account
from handlers.forgot_password import Password
from handlers.new_password import New_password
from handlers.regist import Registration
from handlers.sign_up import Sign_up

db = Data_base()
win = QApplication([])

login=Sign_up('designs/regist.ui', db, "Войти")
account=Account('designs/personal_data.ui', db, "Личный кабинет")
regist=Registration('designs/registration.ui', db, "Регистрация")
forgot_password=Password('designs/password.ui', db, "Забыли пароль")
new_password=New_password('designs/new_password.ui', db, "Новый пароль")
login.show()
win.exec()