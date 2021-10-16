import sqlite3

class UserRepository:

  def __init__ (self, db):
    self.dbContext = db

  def GetUser(self, username, password):
    sql_statement = f"SELECT * from users WHERE username='{username}' AND password='{password}'"
    #sql_statement = f'SELECT * from users WHERE username="{username}" AND password="{password}"'
    self.dbContext.cur.execute(sql_statement)
    return self.dbContext.cur.fetchone()
    
  def UpdatePassword(self):
    pass
  def show_all_clients(self):
    self.not_implemented(self.show_all_clients)
  def add_new_client(self):
    self.not_implemented(self.add_new_client)
    
  def delete_client(self):
    self.not_implemented(self.delete_client)  
  
  def show_all_users(self):
    self.not_implemented(self.show_all_users)

  def add_new_user(self, userName, Password):
      self.dbContext.append(username, password)
      self.dbContext.save()

  def make_a_user_admin(self):
    self.not_implemented(self.make_a_user_admin)

  def delete_user(self):
    self.not_implemented(self.delete_user)

  def change_password(self):
    self.not_implemented(self.change_password)

  def close():
    self.conn.close()

  def logout(self):
    self.loggedin = 0
    self.loggedin_user = None
    self.admin_is_loggedin = 0 


