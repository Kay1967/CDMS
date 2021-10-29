import sqlite3
from Domain.Client import Client
from Helper.EncryptionHelper import EncryptionHelper
from Record.ClientRecord import ClientRecord

class ClientRepository:
  def __init__ (self, db):
    self.dbContext = db

  def GetClient(self, fullname):
    queryParameters = EncryptionHelper.GetEncryptedTuple((fullname,))
    sql_statement = '''SELECT * from client WHERE fullname=?'''
    self.dbContext.cur.execute(sql_statement, queryParameters)
    clientTuples = self.dbContext.cur.fetchone()
    if clientTuples is None:
      raise ValueError("Client not found")
    
    clientRecord = ClientRecord(clientTuples)       
    return clientRecord.ToClientDomain()      
  
  def GetAllClients(self):
    sql_statement = f"SELECT * FROM client"
    self.dbContext.cur.execute(sql_statement) 
    clientTuples = self.dbContext.cur.fetchall()
    allClients = []
    for encryptedClientTuple in clientTuples:
      clientRecord = ClientRecord(encryptedClientTuple)       
      allClients.append(clientRecord.ToClientDomain())      

    return allClients
    

  def CreateClient(self, fullname, streetname, housenumber, zipcode, city, emailaddress, mobilephone):
    encryptedValues = EncryptionHelper.GetEncryptedTuple((fullname, streetname, housenumber, zipcode, city, emailaddress, mobilephone))
    sql_statement = '''INSERT INTO client (fullname, streetname, housenumber, zipcode, city, emailaddress, mobilephone) VALUES (?,?,?,?,?,?,?)'''
    self.dbContext.cur.execute(sql_statement, encryptedValues)
    self.dbContext.conn.commit()
 
  #Generic for updating info of clients 
  def UpdateClient(self, fullname, client_data):
    encryptedValues = EncryptionHelper.GetEncryptedTuple((client_data))
    sql_statement = '''UPDATE client SET client_data=? WHERE fullname =?'''
    self.dbContext.cur.execute(sql_statement, encryptedValues)
    self.dbContext.conn.commit()
  # def UpdateClient(self, fullname, clientTuple):
   
  #   sql_statement = '''UPDATE client WHERE fullname =?'''
  #   self.dbContext.cur.execute(sql_statement, encryptedValues)
  #   self.dbContext.conn.commit()

  def DeleteClient(self, fullname):
    encryptedValues = EncryptionHelper.GetEncryptedTuple((fullname,))
    sql_statement = '''DELETE FROM client WHERE fullname =?'''
    self.dbContext.cur.execute(sql_statement, encryptedValues)
    self.dbContext.conn.commit()
