from Record.UserRecord import UserRecord
from Helper.EncryptionHelper import EncryptionHelper

class UserRepository:

  def __init__ (self, db):
    self.dbContext = db

  def GetUser(self, username):
    queryParameters = EncryptionHelper.GetEncryptedTuple((username,))
    sql_statement = '''SELECT * from users WHERE LOWER(username)=LOWER(?)'''
    self.dbContext.cur.execute(sql_statement, queryParameters)
    userEncrypted = self.dbContext.cur.fetchone()
    if userEncrypted is None:
      raise ValueError("User not found")

    userRecord = UserRecord(userEncrypted)
    return userRecord.ToUserDomain()

  def GetAllUsers(self):
    sql_statement = f"SELECT * FROM users"
    self.dbContext.cur.execute(sql_statement)
    userRecords = self.dbContext.cur.fetchall()

    allUsers = []
    for userRecord in userRecords:
      userRecord = UserRecord(userRecord)
      allUsers.append(userRecord.ToUserDomain())

    return allUsers 

  # Generic for updating password for all users
  def UpdatePassword(self, username, newPassword):
    encryptedValues = EncryptionHelper.GetEncryptedTuple((newPassword, username))
    sql_statement = '''UPDATE users SET password=? WHERE username =?'''
    self.dbContext.cur.execute(sql_statement, encryptedValues)
    self.dbContext.conn.commit()

  def CreateUser(self, username, password, fullname, admin, lastLogin):
    encryptedValues = EncryptionHelper.GetEncryptedTuple((username, password, fullname, admin, lastLogin.strftime("%d-%m-%Y")))
    sql_statement = '''INSERT INTO users (username, password, fullname, admin, last_login) VALUES (?,?,?,?,?)'''
    self.dbContext.cur.execute(sql_statement, encryptedValues)
    self.dbContext.conn.commit()
  
  def UpdateUser(self, username, fullname, usernameRecord):
    encryptedValues = EncryptionHelper.GetEncryptedTuple((username, fullname, usernameRecord))
    sql_statement = '''UPDATE users SET username=?, fullname=? WHERE username =?'''
    self.dbContext.cur.execute(sql_statement, encryptedValues)
    self.dbContext.conn.commit()
  
  def DeleteUser(self, username):
    encryptedValues = EncryptionHelper.GetEncryptedTuple((username,))
    sql_statement = '''DELETE FROM users WHERE username =?'''
    self.dbContext.cur.execute(sql_statement, encryptedValues)
    self.dbContext.conn.commit()

  def UpdateLastLogin(self, loginDate, username):
    encryptedValues = EncryptionHelper.GetEncryptedTuple((loginDate.strftime("%d-%m-%Y"), username))
    sql_statement = '''UPDATE users SET last_login=? WHERE username=?'''
    self.dbContext.cur.execute(sql_statement, encryptedValues)
    self.dbContext.conn.commit()    