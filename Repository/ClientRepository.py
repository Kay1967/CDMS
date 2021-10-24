import sqlite3
# from Domain.Advisor import Advisor
# from Domain.SysAdmin import SysAdmin
from Helper.EncryptionHelper import EncryptionHelper
# from Repository.UserRepository import UserRepository

class ClientRepository:
  def __init__ (self, db):
    self.dbContext = db
    
  def GetAllClients(self):
    sql_statement = f"SELECT * FROM client"
    self.dbContext.cur.execute(sql_statement)
    clientRecords = self.dbContext.cur.fetchall()
  
  def CreateClient(self, fullname, streetname, housenumber, zipcode, city, emailaddress, mobilephone):
    print((fullname, streetname, housenumber, zipcode, city, emailaddress, mobilephone))
    encryptedValues = EncryptionHelper.GetEncryptedTuple((streetname, housenumber, zipcode, city, mobilephone))
    print(encryptedValues)
    sql_statement = '''INSERT INTO client VALUES (fullname = ?, streetname = ?, housenumber = ?, zipcode = ?, city = ?, emailaddress = ?, mobilephone = ?)'''
    self.dbContext.cur.execute(sql_statement, encryptedValues)
    self.dbContext.conn.commit()
 
  #Generic for updating info of clients 
  def UpdateClient(self, fullname, NewStreetName, NewHousenNmber, NewZipCode,
                         NewCity, NewEmailAddress, NewMobilePhone):
    sql_statement = '''UPDATE client WHERE fullname =?'''
    self.dbContext.cur.execute(sql_statement, encryptedValues)
    self.dbContext.conn.commit()

  def DeleteClient(self):
    encryptedValues = EncryptionHelper.GetEncryptedTuple((fullname,))
    sql_statement = '''DELETE FROM client WHERE fullname =?'''
    self.dbContext.cur.execute(sql_statement, encryptedValues)
    self.dbContext.conn.commit()
