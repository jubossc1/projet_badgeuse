from psycopg2 import *


class Badgeuse:
    def __init__(self):
        self.conn = self.connect()
        self.cur = self.conn.cursor()
        self.cur.execute("select version()")
        # Si le tableau n'est pas encore créé dans la base de donnée psql:
        # self.cur.execute("CREATE TABLE users (id serial PRIMARY KEY, name varchar(150), last_name varchar(150),"
        #                 " password varchar(150), email varchar(150), peremption DATE DEFAULT CURRENT_DATE);")

    def connect(self):
        conn = connect(
            host="localhost",
            database="badgeuse",
            user="postgres",
            password="Pbadgeuse2022!")
        return conn

    def f_add(self, n, l, p, e):
        self.cur.execute("INSERT INTO users (name, last_name, password, email) VALUES (%s, %s, %s, %s)",
                         (n, l, p, e))

    def add_user(self):
        name = input("Enter your first name:        ")
        last_name = input("Enter your last name:         ")
        password = input("Enter a password:             ")
        email = input("Enter your email:             ")
        self.cur.execute("INSERT INTO users (name, last_name, password, email) VALUES (%s, %s, %s, %s)",
                         (name, last_name, password, email))

    def check_card(self, password):
        try:
            self.cur.execute(f"SELECT * FROM users WHERE password = '{password}';")
            print(self.cur.fetchall())
        except:
            print("ERROR")

    def check_name(self, name):
        try:
            self.cur.execute(f"SELECT * FROM users WHERE name = '{name}';")
            print(self.cur.fetchall())
        except:
            print("ERROR")

    def check_lname(self, lname):
        try:
            self.cur.execute(f"SELECT * FROM users WHERE last_name = '{lname}';")
            print(self.cur.fetchall())
        except:
            print("ERROR")

    def select_all(self):
        self.cur.execute("SELECT * FROM users;")
        print(self.cur.fetchall())

    def test(self):
        while True:
            x = int(input("Press 1 to enter a user, press 2 to see the list of the existing users, "
                          "press 3 to look if someone is in the database, press 4 to stop the programme.\n"))
            if x == 2:
                self.select_all()
            elif x == 1:
                self.add_user()
            elif x == 3:
                y = int(input("Press 1 to check a name, 2 to check a last name and 3 to check a password.\n"))
                if y == 1:
                    self.check_name(input("Enter your first name:    "))
                if y == 2:
                    self.check_lname(input("Enter your last name:    "))
                if y == 3:
                    self.check_card(input("Enter your password:      "))
            elif x == 4:
                break

    def stop(self):
        # Pour que le code effectue un changement sur la base de donnée:
        # self.conn.commit()     #A désactiver en phase de test

        self.cur.close()
        self.conn.exit()
