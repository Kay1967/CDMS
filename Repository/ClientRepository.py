import sqlite3

class ClientRepository:
  def __init__ (self, db):
    self.dbContext = db

  def GetAllClients(self):
    self.not_implemented(self.GetAllClients)
      
  def CreateClient(self):
    self.not_implemented(self.CreateClient)
      
  def DeleteClient(self):
    self.not_implemented(self.DeleteClient)