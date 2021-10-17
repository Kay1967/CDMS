import sqlite3
from Domain.Advisor import Advisor
from Domain.SysAdmin import SysAdmin
from Helper.EncryptionHelper import EncryptionHelper

class UserRepository:

  def __init__ (self, db):
    self.dbContext = db

  def GetUser(self, username):
    queryParameters = EncryptionHelper.GetEncryptedTuple((username,))
    sql_statement = '''SELECT * from users WHERE username=?'''
    self.dbContext.cur.execute(sql_statement, queryParameters)
    userEncrypted = self.dbContext.cur.fetchone()
    if userEncrypted is None:
      return

    user = EncryptionHelper.GetDecryptedTuple(userEncrypted)
    if user[3] == "1":
      return SysAdmin(user)
    else:
      return Advisor(user)

  def GetAllUsers(self):
    sql_statement = f"SELECT * FROM users"
    self.dbContext.cur.execute(sql_statement)
    userRecords = self.dbContext.cur.fetchall()

    allUsers = []
    for encryptedUser in userRecords:
      user = EncryptionHelper.GetDecryptedTuple(encryptedUser)
      if user[3] == "1":
        allUsers.append(SysAdmin(user))
      else:
        allUsers.append(Advisor(user))

    return allUsers 

  # Generic for updating password for all users
  def UpdatePassword(self, username, newPassword):
    encryptedValues = EncryptionHelper.GetEncryptedTuple((newPassword, username))
    sql_statement = '''UPDATE users SET password=? WHERE username =?'''
    self.dbContext.cur.execute(sql_statement, encryptedValues)
    self.dbContext.conn.commit()

  def CreateUser(self, username, password, fullname, admin):
    encryptedValues = EncryptionHelper.GetEncryptedTuple((username, password, fullname, admin))
    sql_statement = '''INSERT INTO users VALUES (username =?, password =?, fullname =?, admin = ?)'''
    self.dbContext.cur.execute(sql_statement, encryptedValues)
    self.dbContext.conn.commit()
  
  def DeleteUser(self, username):
    encryptedValues = EncryptionHelper.GetEncryptedTuple((username,))
    sql_statement = '''DELETE FROM users WHERE username =?'''
    self.dbContext.cur.execute(sql_statement, encryptedValues)
    self.dbContext.conn.commit()

  def show_all_clients(self):
    self.not_implemented(self.show_all_clients)
  def add_new_client(self):
    self.not_implemented(self.add_new_client)
    
  def delete_client(self):
    self.not_implemented(self.delete_client)  
  
  def add_new_user(self, userName, Password):
      self.dbContext.append(username, password)
      self.dbContext.save()

  def make_a_user_admin(self):
    self.not_implemented(self.make_a_user_admin)

  

  def change_password(self):
    self.not_implemented(self.change_password)

  def close():
    self.conn.close()

  def logout(self):
    self.loggedin = 0
    self.loggedin_user = None
    self.admin_is_loggedin = 0 


