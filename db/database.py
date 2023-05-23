"""
File for communicating with postgreSQL db and providing queries
"""

import base64
import psycopg2



class DataBase:
    """Class for communicating with database"""
    def __init__(self, config):
        self.data_base = psycopg2.connect(
            user=config["DB_USER"],
            password=config["DB_PASSWORD"],
            host=config["DB_HOST"],
            port=config["DB_PORT"],
            database=config["DB_DB"],
        )

        self.cur = self.data_base.cursor()

    def encode_password(self, password):
        """
        Encode password
        :param password:sequence of symbols
        :return:encoded password
        """
        encoded_bytes = base64.b64encode(password.encode("utf-8"))
        encoded_password = encoded_bytes.decode("utf-8")
        return encoded_password

    def decode_password(self, encoded_password):
        """
        decode password
        :param encoded_password: encoded sequence of symbols
        :return: decoded password
        """
        decoded_bytes = base64.b64decode(encoded_password.encode("utf-8"))
        decoded_password = decoded_bytes.decode("utf-8")
        return decoded_password

    def check_login_password(self, login, password):
        """
        verification of the existence of the login and password in database
        :param login: username
        :param password: sequence of symbols
        :return: True or False
        """
        # True, если такой пользователь существует, False в противном случае  select
        self.cur.execute(
            f"""SELECT login, password FROM sign_up INNER JOIN info ON sign_up.id = info.sign_up_id
                         WHERE sign_up.login='{login}' or info.email='{login}' 
                         and sign_up.password='{self.encode_password(password)}' """
        )
        return bool(self.cur.fetchone())

    def check_data(self, email, login, password):
        """
        verification of the existence of the login and password in database

        :param email: sequence of symbols
        :param login: username
        :param password: sequence of symbols
        :return:
        """
        self.cur.execute(f"""SELECT email FROM info WHERE email='{email}' """)
        if (
            self.check_login_password(login, password)
            or self.cur.fetchone() is not None
        ):
            return False

        return True

    def add_regist(self, *args):
        """

        :param args: list of userdata
        :return: none
        """
        name, surname, birth, email, photo, login, password=args
        if self.check_data(email, login, password):
            self.cur.execute(
                f"""INSERT INTO sign_up(login, password)
                 VALUES ('{login}', '{self.encode_password(password)}') RETURNING id"""
            )
            data1 = self.cur.fetchone()[0]
            if photo == "":
                self.cur.execute(
                    f"""INSERT INTO info(sign_up_id, name, surname, birth, email) 
                    VALUES({data1},'{name}', '{surname}', '{birth}', '{email}') """
                )
            else:
                self.cur.execute(
                    f"""INSERT INTO info(sign_up_id, name, surname, birth, email, photo) 
                    VALUES({data1},'{name}', '{surname}', '{birth}', '{email}', '{photo}') """
                )

            self.data_base.commit()
        else:
            raise ValueError()

    def get_user_data(self, login, password):
        """
        get userdata
        :param login: username
        :param password: sequence of symbols
        :return:userdata
        """
        self.cur.execute(
            f"""SELECT sign_up. id FROM sign_up INNER JOIN info ON sign_up.id = info.sign_up_id
         WHERE sign_up.login='{login}' or info.email='{login}' 
         and sign_up.password='{self.encode_password(password)}' """
        )
        user_id = self.cur.fetchone()[0]
        self.cur.execute(
            f"""SELECT name, surname, birth, email, photo FROM info WHERE sign_up_id='{user_id}'"""
        )
        data = self.cur.fetchone()
        return data

    def new_password(self, password, email):
        """
        changing password
        :param password: sequence of symbols
        :param email: sequence of symbols
        :return: none
        """
        password = self.cur.execute(
            f"""UPDATE sign_up  SET password='{self.encode_password(password)}' 
            WHERE  EXISTS (SELECT 1 
              FROM info 
              WHERE info.sign_up_id = sign_up.id 
              AND info.email = '{email}');"""
        )
        self.data_base.commit()

    def search_email(self, email):
        """
        get user email
        :param email: sequence of symbols
        :return: none
        """
        self.cur.execute(f"""SELECT email FROM info WHERE email='{email}'""")
        mail = self.cur.fetchone()
        if mail is None:
            return False
        return True
