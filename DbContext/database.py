import sqlite3
from Helper.EncryptionHelper import EncryptionHelper
from datetime import datetime as dt
from datetime import timedelta

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
        tb_create = "CREATE TABLE client (fullname TEXT, streetname TEXT, housenumber TEXT, zipcode TEXT, city Text, emailaddress Text, mobilephone TEXT)"
        try:
            self.cur.execute(tb_create)
            # add sample records to the db manually
            self.cur.execute('''INSERT INTO client (fullname, streetname, housenumber, zipcode, city, emailaddress, mobilephone) VALUES (?, ?, ?, ?, ?, ?, ?)''', EncryptionHelper.GetEncryptedTuple(('Lili Anderson', 'Duinweg Street', '10', '3067MR', 'The Hague', 'lili@email.com', '+31-6-86453221')))
            self.cur.execute('''INSERT INTO client (fullname, streetname, housenumber, zipcode, city, emailaddress, mobilephone) VALUES (?, ?, ?, ?, ?, ?, ?)''', EncryptionHelper.GetEncryptedTuple(('Anne Banwarth', 'Sleten Street', '28', '3138JC', 'Amsterdam', 'anne@gmail.com', '+31-6-66338899')))
            self.conn.commit()
        except: 
            None

        # create user table if it does not exist
        tb_create = "CREATE TABLE users (username TEXT, password TEXT, fullname TEXT, admin TEXT, last_login TEXT);"
        try:
            self.cur.execute(tb_create)
            # add sample records to the db manually
            lastLogin = dt.now() - timedelta(days=15)
            date = lastLogin.strftime("%d-%m-%Y")
            self.cur.execute('''INSERT INTO users (username, password, fullname, admin, last_login) VALUES (?, ?, ?, ?, ?)''', EncryptionHelper.GetEncryptedTuple(('bob.l', 'B0b!23', 'Bob Larson', 1, date)))
            self.cur.execute('''INSERT INTO users (username, password, fullname, admin, last_login) VALUES (?, ?, ?, ?, ?)''', EncryptionHelper.GetEncryptedTuple(('ivy_russel', 'ivy@R123' , 'Ivy Russel', 0, date)))
            self.cur.execute('''INSERT INTO users (username, password, fullname, admin, last_login) VALUES (?, ?, ?, ?, ?)''', EncryptionHelper.GetEncryptedTuple(('superadmin', 'Admin!23' , 'Super Admin', 1, date)))
            self.conn.commit()
        except: 
            None
      
        #create logging table
        tb_create = "CREATE TABLE logging (username TEXT, date TEXT, time TEXT, description_of_activity TEXT, additional_info TEXT, supicious TEXT)"
        logDate =  dt.now() - timedelta(days=10)
        try:
            # add sample records to the db manually
            self.cur.execute(tb_create)
            logDate =  dt.now() - timedelta(days=10)
            date = logDate.strftime("%d-%m-%Y")
            time = logDate.strftime("%H:%M:%S")

            self.cur.execute('''INSERT INTO logging (username, date, time, description_of_activity, additional_info, supicious) VALUES (?, ?, ?, ?, ?, ?)''', EncryptionHelper.GetEncryptedTuple(('bob.l', date, time, "New advisor added: -ls", "Failed: \nUsername:-ls Password:cd", 1)))
            self.cur.execute('''INSERT INTO logging (username, date, time, description_of_activity, additional_info, supicious) VALUES (?, ?, ?, ?, ?, ?)''', EncryptionHelper.GetEncryptedTuple(('bob.l', date, time, "Update advisor: ivy_russel", "Failed: \nUsername:ivy_russel Password:FROM", 1)))
            self.conn.commit()
        except:
            None

    def executeAndCommit(self, sql_statement, queryParameters):
        try:
            if queryParameters is not None:
                self.cur.execute(sql_statement, queryParameters)
            else:
                self.cur.execute(sql_statement)
            self.conn.commit()
        except Exception as exception: 
            print("something went wrong")
            raise Exception(exception, False)   
        pass

    def executeAndFetchAll(self, sql_statement, queryParameters):
        try:
            if queryParameters is not None:
                self.cur.execute(sql_statement, queryParameters)
            else:
                self.cur.execute(sql_statement)
            records = self.cur.fetchall()
            return records
        except Exception as exception: 
            print("something went wrong")
            raise Exception(exception, False)     

    def executeAndFetchOne(self, sql_statement, queryParameters):
        try:
            if queryParameters is not None:
                self.cur.execute(sql_statement, queryParameters)
            else:
                self.cur.execute(sql_statement)
            record = self.cur.fetchone()
            return record
        except Exception as exception: 
            print("something went wrong")
            raise Exception(exception, False)      

    def not_implemented(self, func):
        print(func.__name__ + ' method is Not implemented')
    
def escape_sql_meta(sql_query):
    pass



