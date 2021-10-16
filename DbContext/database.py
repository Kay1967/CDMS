import sqlite3
from Component.UserInterface import *
from termcolor import colored

# Database
# --------------------------------------------------------------------
class db:
    def __init__(self, db_name, client_table_name, users_table_name):
        self.db_name = db_name
        self.client_table_name = client_table_name
        self.users_table_name = users_table_name

        self.loggedin = 0
        self.loggedin_user = None
        self.admin_is_loggedin = 0

        self.reset()

    def reset(self):
        self.conn = sqlite3.connect(self.db_name) 
        self.cur = self.conn.cursor()

        # create client table if it does not exist
        tb_create = "CREATE TABLE client (person_id int, fullname CHAR)"
        try:
            self.cur.execute(tb_create)
            # add sample records to the db manually
            self.cur.execute("INSERT INTO client (person_id, fullname) VALUES (1, 'Lili Anderson')")
            self.cur.execute("INSERT INTO client (person_id, fullname) VALUES (2, 'Anne Banwarth')")
            self.conn.commit()
        except: 
            None

        # create user table if it does not exist
        tb_create = "CREATE TABLE users (username TEXT, password TEXT, fullname TEXT, admin INT);"
        try:
            self.cur.execute(tb_create)
            # add sample records to the db manually
            self.cur.execute("INSERT INTO users (username, password, fullname, admin) VALUES ('bob.l', 'B0b!23', 'Bob Larson', 1)")
            self.cur.execute("INSERT INTO users (username, password, fullname, admin) VALUES ('ivy_russel', 'ivy@R123' , 'Ivy Russel', 0)")
            self.conn.commit()
        except: 
            None
      
        # create logging table
        # tb_create = "CREATE TABLE logging (username varchar, date varchar, time varchar, description_of_activity varchar, additionalInfo varchar, supicious varchar, read varchar)"
        # try:
        #     self.cur.execute(tb_create)
        #     self.conn.commit()
        # except:
        #     None

    def not_implemented(self, func):
        print(func.__name__ + ' method is Not implemented')
    
def escape_sql_meta(sql_query):
    pass



