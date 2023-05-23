import psycopg2

import base64


class Data_base:
    def __init__(self):
        self.db = psycopg2.connect(
        user="postgres",
        password="937023",
        host="localhost",
        port="5432",
        database="account"
    )
        self.cur = self.db.cursor()

    def encode_password(self, password):
        encoded_bytes = base64.b64encode(password.encode('utf-8'))
        encoded_password = encoded_bytes.decode('utf-8')
        return encoded_password

    def decode_password(self, encoded_password):
        decoded_bytes = base64.b64decode(encoded_password.encode('utf-8'))
        decoded_password = decoded_bytes.decode('utf-8')
        return decoded_password

    def check_login_password(self, login, password):
        # True, если такой пользователь существует, False в противном случае  select
        self.cur.execute(
            f"""SELECT login, password FROM sign_up INNER JOIN info ON sign_up.id = info.sign_up_id
                         WHERE sign_up.login='{login}' or info.email='{login}' and sign_up.password='{self.encode_password(password)}' """)
        if self.cur.fetchone():
            return True
        else:
            return False

    def check_data(self, email, login, password):
        self.cur.execute(f"""SELECT email FROM info WHERE email='{email}' """)
        if self.check_login_password(login, password) or self.cur.fetchone() is not None:
            return False
        else:
            return True

    def add_regist(self, name, surname, birth, email, photo, login, password):

        if self.check_data(email, login, password):
            self.cur.execute(
                f"""INSERT INTO sign_up(login, password) VALUES ('{login}', '{self.encode_password(password)}') RETURNING id""")
            data1=self.cur.fetchone()[0]
            if photo == "":
                data2 = self.cur.execute(
                    f"""INSERT INTO info(sign_up_id, name, surname, birth, email) VALUES({data1},'{name}', '{surname}', '{birth}', '{email}') """)
            else:
                data2 = self.cur.execute(
                    f"""INSERT INTO info(sign_up_id, name, surname, birth, email, photo) VALUES({data1},'{name}', '{surname}', '{birth}', '{email}', '{photo}') """)

            self.db.commit()
        else:
            raise ValueError()

    def get_user_data(self, login, password):
        self.cur.execute(f"""SELECT sign_up. id FROM sign_up INNER JOIN info ON sign_up.id = info.sign_up_id
         WHERE sign_up.login='{login}' or info.email='{login}' and sign_up.password='{self.encode_password(password)}' """)
        id = self.cur.fetchone()[0]
        self.cur.execute(
            f"""SELECT name, surname, birth, email, photo FROM info WHERE sign_up_id='{id}'""")
        data = self.cur.fetchone()
        return data

    def new_password(self, password, email):
        password=self.cur.execute(
            f"""UPDATE sign_up  SET password='{self.encode_password(password)}' WHERE  EXISTS (SELECT 1 
              FROM info 
              WHERE info.sign_up_id = sign_up.id 
              AND info.email = '{email}');"""
        )
        self.db.commit()

    def search_email(self,email ):
        self.cur.execute(f"""SELECT email FROM info WHERE email='{email}'""")
        mail=self.cur.fetchone()
        if mail is None:
            return False
        else:
            return True






