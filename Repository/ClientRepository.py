import sqlite3
from Domain.Client import Client
from tabulate import tabulate
from Helper.EncryptionHelper import EncryptionHelper
# from Repository.UserRepository import UserRepository

class ClientRepository:
  def __init__ (self, db):
    self.dbContext = db

  def GetClient(self, fullname):
    queryParameters = EncryptionHelper.GetEncryptedTuple((fullname,))
    sql_statement = '''SELECT * from users WHERE fullname=?'''
    self.dbContext.cur.execute(sql_statement, queryParameters)
    clientEncrypted = self.dbContext.cur.fetchone()
    if clientEncrypted is None:
      raise ValueError("Client not found")

    
  def GetAllClients(self):
    sql_statement = f"SELECT * FROM client"
    self.dbContext.cur.execute(sql_statement) 
    clientRecords = self.dbContext.cur.fetchall()
    #decryptedList = EncryptionHelper.GetDecryptedTuple(clientRecords)
    allClients = []
    for encryptedClient in clientRecords:
      client = EncryptionHelper.GetDecryptedTuple(encryptedClient)
      
      allClients.append(Client(client[0], client[1], client[2], client[3]))
      

    return allClients
    

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

  def DeleteClient(self, fullname):
    encryptedValues = EncryptionHelper.GetEncryptedTuple((fullname,))
    sql_statement = '''DELETE FROM client WHERE fullname =?'''
    self.dbContext.cur.execute(sql_statement, encryptedValues)
    self.dbContext.conn.commit()
