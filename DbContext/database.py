import sqlite3
from Helper.EncryptionHelper import EncryptionHelper

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
        tb_create = "CREATE TABLE client (person_id CHAR, fullname CHAR)"
        try:
            self.cur.execute(tb_create)
            # add sample records to the db manually
            self.cur.execute('''INSERT INTO client (person_id, fullname) VALUES (?, ?)''', EncryptionHelper.GetEncryptedTuple((1, 'Lili Anderson')))
            self.cur.execute('''INSERT INTO client (person_id, fullname) VALUES (?, ?)''', EncryptionHelper.GetEncryptedTuple((2, 'Anne Banwarth')))
            self.conn.commit()
        except: 
            None

        # create user table if it does not exist
        tb_create = "CREATE TABLE users (username TEXT, password TEXT, fullname TEXT, admin TEXT);"
        try:
            self.cur.execute(tb_create)
            # add sample records to the db manually
            self.cur.execute('''INSERT INTO users (username, password, fullname, admin) VALUES (?, ?, ?, ?)''', EncryptionHelper.GetEncryptedTuple(('bob.l', 'B0b!23', 'Bob Larson', 1)))
            self.cur.execute('''INSERT INTO users (username, password, fullname, admin) VALUES (?, ?, ?, ?)''', EncryptionHelper.GetEncryptedTuple(('ivy_russel', 'ivy@R123' , 'Ivy Russel', 0)))
            self.conn.commit()
        except: 
            None
      
        #create logging table
        tb_create = "CREATE TABLE logging (username TEXT, date TEXT, time TEXT, description_of_activity TEXT, additional_info TEXT, supicious TEXT)"
        try:
            #self.cur.execute('''INSERT INTO users (username, date, time, description_of_activity, additional_info, supicious) VALUES (?, ?, ?, ?)''', EncryptionHelper.GetEncryptedTuple(('bob.l', 'B0b!23', 'Bob Larson', 1)))
            self.cur.execute(tb_create)
            self.conn.commit()
        except:
            None

    def not_implemented(self, func):
        print(func.__name__ + ' method is Not implemented')
    
def escape_sql_meta(sql_query):
    pass



