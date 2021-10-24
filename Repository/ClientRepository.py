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
    return self.dbContext.cur.fetchall()
  
  def CreateClient(self, fullname, streetname, housenumber, zipcode, city, emailaddress, mobilephone):
    encryptedValues = EncryptionHelper.GetEncryptedTuple((fullname, streetname, housenumber, zipcode, city, emailaddress, mobilephone))
    sql_statement = '''INSERT INTO client (fullname, streetname, housenumber, zipcode, city, emailaddress, mobilephone) VALUES (?,?,?,?,?,?,?)'''
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
