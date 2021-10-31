from Domain.User import User
from Record.UserRecord import UserRecord
from Helper.EncryptionHelper import EncryptionHelper

class UserRepository:

  def __init__ (self, db, loggingRepository, tenant = None):
    self.dbContext = db
    self.loggingRepository = loggingRepository

    tenantIsDefined = isinstance(tenant, User)
    if tenantIsDefined:
      self.tenant = tenant

  def GetUser(self, username, login = False):
    queryParameters = EncryptionHelper.GetEncryptedTuple((username,))
    sql_statement = '''SELECT * from users WHERE LOWER(username)=LOWER(?)'''
    try: userEncrypted = self.dbContext.executeAndFetchOne(sql_statement, queryParameters)
    except Exception as error: 
      if self.tenantIsDefined:
          self.CreateLog(self.tenant.username, f"{self.GetAllLogs.__name__}", f"DatabaseException {error}", 1); return
      else:
          self.CreateLog("Anonymouse", f"{self.GetAllLogs.__name__}", f"DatabaseException {error}", 1); return

    if userEncrypted is None and login is False:
      raise ValueError("User not found", True)
    if userEncrypted is None and login is True:
      raise ValueError("Login failed", True)

    userRecord = UserRecord(userEncrypted)
    return userRecord.ToUserDomain()

  def GetAllUsers(self):
    sql_statement = f"SELECT * FROM users"
    try: userRecords = self.dbContext.executeAndFetchAll(sql_statement, None)
    except Exception as error: self.loggingRepository.CreateLog(self.tenant.username, f"{self.GetAllUsers.__name__}", f"DatabaseException {error}", 1); return

    allUsers = []
    for userRecord in userRecords:
      userRecord = UserRecord(userRecord)
      allUsers.append(userRecord.ToUserDomain())

    return allUsers 

  # Generic for updating password for all users
  def UpdatePassword(self, username, newPassword):
    encryptedValues = EncryptionHelper.GetEncryptedTuple((newPassword, username))
    sql_statement = '''UPDATE users SET password=? WHERE username =?'''
    try: self.dbContext.executeAndCommit(sql_statement, encryptedValues)
    except Exception as error: self.loggingRepository.CreateLog(self.tenant.username, f"{self.UpdatePassword.__name__}", f"DatabaseException {error}", 1)
 
  def CreateUser(self, username, password, fullname, admin, lastLogin):
    encryptedValues = EncryptionHelper.GetEncryptedTuple((username, password, fullname, admin, lastLogin.strftime("%d-%m-%Y")))
    sql_statement = '''INSERT INTO users (username, password, fullname, admin, last_login) VALUES (?,?,?,?,?)'''
    try: self.dbContext.executeAndCommit(sql_statement, encryptedValues)
    except Exception as error: self.loggingRepository.CreateLog(self.tenant.username, f"{self.CreateUser.__name__}", f"DatabaseException {error}", 1)
   
  def UpdateUser(self, username, fullname, usernameRecord):
    encryptedValues = EncryptionHelper.GetEncryptedTuple((username, fullname, usernameRecord))
    sql_statement = '''UPDATE users SET username=?, fullname=? WHERE username =?'''
    try: self.dbContext.executeAndCommit(sql_statement, encryptedValues)
    except Exception as error: self.loggingRepository.CreateLog(self.tenant.username, f"{self.UpdateUser.__name__}", f"DatabaseException {error}", 1)
   
  def DeleteUser(self, username):
    encryptedValues = EncryptionHelper.GetEncryptedTuple((username,))
    sql_statement = '''DELETE FROM users WHERE username =?'''
    try: self.dbContext.executeAndCommit(sql_statement, encryptedValues)
    except Exception as error: self.loggingRepository.CreateLog(self.tenant.username, f"{self.DeleteUser.__name__}", f"DatabaseException {error}", 1)
 
  def UpdateLastLogin(self, loginDate, username):
    encryptedValues = EncryptionHelper.GetEncryptedTuple((loginDate.strftime("%d-%m-%Y"), username))
    sql_statement = '''UPDATE users SET last_login=? WHERE username=?'''
    try: self.dbContext.executeAndCommit(sql_statement, encryptedValues)
    except Exception as error: self.loggingRepository.CreateLog(self.tenant.username, f"{self.UpdateLastLogin.__name__}", f"DatabaseException {error}", 1)
 