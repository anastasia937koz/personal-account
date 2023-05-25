"""File for password reset"""

from random import randint
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from PyQt6.QtWidgets import QMessageBox
from handlers.window import Window




class Password(Window):
    """class for password reset by generated """
    def __init__(self, path, database, name):
        super().__init__(path, database, name)
        self.code=None
        self.form.sent_email.clicked.connect(self.sent_code)
        self.form.sent.clicked.connect(self.check_code)

    def generate_code(self):
        """
        generate code that consists of 6 symbols
        :return: code of 6 symbols
        """
        code = randint(100000, 999999)
        return code

    def sent_code(self):
        """
        send code to email
        :return: none
        """
        email = self.form.email.text()
        if self.database.search_email(email):
            self.code = self.generate_code()
            # Параметры подключения к SMTP-серверу
            smtp_server = "smtp.mail.ru"  # Укажите адрес SMTP-сервера
            smtp_port = 587  # Укажите порт SMTP-сервера
            smtp_username = "nastya937kozlova@mail.ru"  # Укажите вашу почту
            smtp_password = "cZgCJBGxRxzLKC8XwWVh"  # Укажите ваш пароль

            # Создание MIME-сообщения
            msg = MIMEMultipart()
            msg["From"] = "nastya937kozlova@mail.ru"  # Укажите адрес отправителя
            msg["To"] = email  # Укажите адрес получателя
            msg["Subject"] = "Код "  # Укажите тему сообщения

            # Добавление текстовой части сообщения
            text = f"Код для подтверждения пароля:{self.code}"
            msg.attach(MIMEText(text, "plain"))

            # Отправка сообщения через SMTP-сервер
            # try:
            with smtplib.SMTP(smtp_server, smtp_port) as server:
                server.starttls()
                server.login(smtp_username, smtp_password)
                server.send_message(msg)
        else:
            box1 = QMessageBox()
            box1.setText("Пользователя с такой почтой не существует")
            box1.setStandardButtons(QMessageBox.StandardButton.Ok)
            box1.setIcon(QMessageBox.Icon.Warning)
            box1.exec()

    def check_code(self):
        """
        checking that the sent code matches the entered code
        :return:none
        """
        if self.form.code.text() == str(self.code):
            Window.open_windows["Новый пароль"]["object"].set_email(
                self.form.email.text()
            )
            self.windows.hide()
            Window.open_windows["Новый пароль"]["window"].show()
        else:
            box1 = QMessageBox()
            box1.setText("Код не верный")
            box1.setStandardButtons(QMessageBox.StandardButton.Ok)
            box1.setIcon(QMessageBox.Icon.Warning)
            box1.exec()

            # print('Сообщение успешно отправлено!')
        # except Exception as e:
        #     print('Ошибка при отправке сообщения:', str(e))
