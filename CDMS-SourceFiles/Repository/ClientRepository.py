from Helper.EncryptionHelper import EncryptionHelper
from Record.ClientRecord import ClientRecord

class ClientRepository:
  def __init__ (self, db, loggingRepository, tenant):
    self.dbContext = db
    self.loggingRepository = loggingRepository
    self.tenant = tenant

  def GetClient(self, fullname):
    queryParameters = EncryptionHelper.GetEncryptedTuple((fullname,))
    sql_statement = '''SELECT * from client WHERE fullname=?'''
    try: clientTuples = self.dbContext.executeAndFetchOne(sql_statement, queryParameters)
    except Exception as error: self.loggingRepository.CreateLog(self.tenant.username, f"{self.GetClient.__name__}", f"DatabaseException {error}", 1)

    if clientTuples is None:
      raise ValueError("Client not found")
    
    clientRecord = ClientRecord(clientTuples)       
    return clientRecord.ToClientDomain()      
  
  def GetAllClients(self):
    sql_statement = f"SELECT * FROM client"
    try: clientTuples = self.dbContext.executeAndFetchAll(sql_statement, None)
    except Exception as error: self.loggingRepository.CreateLog(self.tenant.username, f"{self.GetAllClients.__name__}", f"DatabaseException {error}", 1); return

    allClients = []
    for encryptedClientTuple in clientTuples:
      clientRecord = ClientRecord(encryptedClientTuple)       
      allClients.append(clientRecord.ToClientDomain())      

    return allClients
    

  def CreateClient(self, fullname, streetname, housenumber, zipcode, city, emailaddress, mobilephone):
    encryptedValues = EncryptionHelper.GetEncryptedTuple((fullname, streetname, housenumber, zipcode, city, emailaddress, mobilephone))
    sql_statement = '''INSERT INTO client (fullname, streetname, housenumber, zipcode, city, emailaddress, mobilephone) VALUES (?,?,?,?,?,?,?)'''
    try: self.dbContext.executeAndCommit(sql_statement, encryptedValues)
    except Exception as error: self.loggingRepository.CreateLog(self.tenant.username, f"{self.CreateClient.__name__}", f"DatabaseException {error}", 1); return
 
  #Generic for updating info of clients 
  def UpdateClient(self, fullname, streetname, housenumber, zipcode, city, emailaddress, mobilephone, fullnameRecord):
    encryptedValues = EncryptionHelper.GetEncryptedTuple((fullname, streetname, housenumber, zipcode, city, emailaddress, mobilephone, fullnameRecord))
    sql_statement = '''UPDATE client SET fullname=?, streetname=?, housenumber=?, zipcode=?, city=?, emailaddress=?, mobilephone=? WHERE fullname =?'''
    try: self.dbContext.executeAndCommit(sql_statement, encryptedValues)
    except Exception as error: self.loggingRepository.CreateLog(self.tenant.username, f"{self.UpdateClient.__name__}", f"DatabaseException {error}", 1); return

  def DeleteClient(self, fullname):
    encryptedValues = EncryptionHelper.GetEncryptedTuple((fullname,))
    sql_statement = '''DELETE FROM client WHERE fullname =?'''
    try: self.dbContext.executeAndCommit(sql_statement, encryptedValues)
    except Exception as error: self.loggingRepository.CreateLog(self.tenant.username, f"{self.DeleteClient.__name__}", f"DatabaseException {error}", 1); return
