import sqlite3
from Domain.Advisor import Advisor
from Domain.SysAdmin import SysAdmin

class UserRepository:

  def __init__ (self, db):
    self.dbContext = db

  def GetUser(self, username):
    sql_statement = f"SELECT * from users WHERE username='{username}'"
    #sql_statement = f'SELECT * from users WHERE username="{username}" AND password="{password}"'
    self.dbContext.cur.execute(sql_statement)
    user = self.dbContext.cur.fetchone()
    
    if user[3] == 1:
      return SysAdmin(user)
    else:
      return Advisor(user)

  def GetAllUsers(self):
    sql_statement = f"SELECT * FROM users"
    self.dbContext.cur.execute(sql_statement)
    userRecords = self.dbContext.cur.fetchall()

    allUsers = []
    for user in userRecords:
     if user[3] == 1:
      allUsers.append(SysAdmin(user))
    else:
      allUsers.append(Advisor(user))

    return allUsers 

  # Generic for updating password for all users
  def UpdatePassword(self, username, newPassword):
    sql_statement = f"UPDATE users SET password='{newPassword}' WHERE username ='{username}'"
    self.dbContext.cur.execute(sql_statement)
    self.dbContext.conn.commit()

  def CreateUser(self, username, password, fullname, admin):
    sql_statement = f"INSERT INTO users VALUES (username ='{username}', password ='{password}', fullname ='{fullname}', admin = '{admin}'"
    self.dbContext.cur.execute(sql_statement)
    self.dbContext.conn.commit()
  
  def DeleteUser(self, username):
    sql_statement = f"DELETE FROM users WHERE username ='{username}'"
    self.dbContext.cur.execute(sql_statement)
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


