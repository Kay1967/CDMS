# from termcolor import colored
# #from View.AdminView import *
# #from Service.ClientService import *
# import sqlite3
# #from DbContext.database import *
# #from Component.UserInterface import *
# class ClientService:

# import string
# from Domain.SuperAdmin import SuperAdmin
# from Domain.SysAdmin import SysAdmin
# from Domain.Advisor import Advisor
# from Enum.Permission import Permission
# from Repository.ClientRepository import *

# class ClientService:
#   def __init__(self, tenant, clientRepository, userRepository, loggingRepository):
#     self.tenant = tenant
#     self.clientRepository = clientRepository
#     self.userRepository = userRepository
#     self.loggingRepository = loggingRepository
  
  # def CreateClient(self):
  #   if not self.tenant.HasPermission(Permission.ManageClient):
  #     print("Unauthorized")
  #     return

  # def UpdateClientInfo(self):
  #   # if self.tenant is not Advisor and self.tenant is not SysAdmin and self.tenant is not SuperAdmin:
  #   # Haspermission is a method that gives back a boolean based on if the tenant has the permission UpdateAdvisorPassword
  #   if not self.tenant.HasPermission(Permission.UpdateClientInfo):
  #     print("Unauthorized")
  #     return

  #   if type(self.tenant) is Advisor:
  #     advisor = self.tenant.username
  #     fullNameToUpdate = input("please enter fullname of the client: ")
  #     if self.clientRepository.GetAllClients().fullName == fullNameToUpdate:
  #       try: self.tanant.GetItemsToUpdate() 
  #       except ValueError as error: print(error); return
  #     else:
  #       try:
  #         advisor = self.GetAndValidateAdvisor()
  #         advisor.GetItemsToUpdate()  
  #       except ValueError as error: print(error); return    
    
  #   self.clientRepository.UpdateClient(self, fullname, streetname, housenumber, zipcode, city, emailaddress, mobilephone)  
  #   self.loggingRepository.CreateLog(self.tenant.username, f"Updated client by Advisor: {advisor.username}", "Success", 0)

  #   print("New Password for " """+ advisor.username + ". Password: " + advisor.password""")



  # def GetItemsToUpdate(self):
  #   ItemToUpdate = self.clientRepository.clientsInfo

  #   for item in ItemToUpdate:
  #         if item == ItemToUpdate[1]:
  #           newStreetname = input("please enter a new streetname: ")
  #           self.tenant.Updateclient(newStreetname)
  #         if item == ItemToUpdate[2]:
  #           newHousenumber = input("please enter a new housenumber: ")
  #           self.tenant.Updateclient(ewHousenumber)
  #         if item == ItemToUpdate[3]:
  #           newZipcode = input("please enter a new zipcode: ")
  #           self.tenant.Updateclient(newZipcode)
  #         if item == ItemToUpdate[4]:
  #           newCity = input("please enter a new city: ")
  #           self.tenant.Updateclient(newCity)
  #         if item == ItemToUpdate[5]:
  #           newEmailaddress = input("please enter a new emailaddress: ")
  #           self.tenant.Updateclient(newEmailaddress)
  #         if item == ItemToUpdate[6]:
  #           newMobilephone = input("please enter a new mobilephone: ")
  #           self.tenant.Updateclient(newMobilephone ) 




# clientsInfo = ['fullname', 'streetname', 'housenumber', 'zipcode', 'city', 'emailaddress', 'mobilephone']
    # for info in clientsinfo:
    #   if info == clientsInfo[1]:
    #     encryptedValues = EncryptionHelper.GetEncryptedTuple((streetname,))
    #     sql_statement = '''UPDATE client SET streetname=? WHERE fullname =?'''
    #   if info == clientsInfo[2]:
    #     encryptedValues = EncryptionHelper.GetEncryptedTuple((housenumber,))
    #     sql_statement = '''UPDATE client SET housenumber=? WHERE fullname =?'''
    #   if info == clientsInfo[3]:
    #     encryptedValues = EncryptionHelper.GetEncryptedTuple((zipcode,))
    #     sql_statement = '''UPDATE client SET zipcode=? WHERE fullname =?'''
    #   if info == clientsInfo[4]:
    #     encryptedValues = EncryptionHelper.GetEncryptedTuple((city,))
    #     sql_statement = '''UPDATE client SET city=? WHERE fullname =?'''
    #   if info == clientsInfo[5]:
    #     encryptedValues = EncryptionHelper.GetEncryptedTuple((emailaddress,))
    #     sql_statement = '''UPDATE client SET emailaddress=? WHERE fullname =?'''
    #   if info == clientsInfo[6]:
    #     encryptedValues = EncryptionHelper.GetEncryptedTuple((mobilephone,))
    #     sql_statement = '''UPDATE client SET mobilephone=? WHERE fullname =?'''
  
  # def GetClient(self, fullname):
  #   queryParameters = EncryptionHelper.GetEncryptedTuple((fullname,))
  #   sql_statement = '''SELECT * FROM client WHERE fullname =?''' 
  #   self.dbContext.cur.execute(sql_statement)
  #   clientRecords = self.dbContext.cur.fetchone()
  #   if userEncrypted is None:
  #     return 

  # def GetUser(self, username):
  #   queryParameters = EncryptionHelper.GetEncryptedTuple((username,))
  #   sql_statement = '''SELECT * from users WHERE username=?'''
  #   self.dbContext.cur.execute(sql_statement, queryParameters)
  #   userEncrypted = self.dbContext.cur.fetchone()
  #   if userEncrypted is None:
  #     return
  
  # def GetClientForUser(self):
  #     self.UserRepository.GetUser(username)

from termcolor import colored
from Component.UserInterface import *
from Enum.Permission import Permission
from Domain.User import User
from Domain.Advisor import Advisor
from Domain.SuperAdmin import SuperAdmin
from Domain.SysAdmin import SysAdmin
from Domain.Client import Client
from View.ClientView import *
import sqlite3

class ClientService:
  def __init__ (self, tenant, clientRepository, loggingRepository):
    self.clientRepository = clientRepository
    self.tenant = tenant
    self.loggingRepository = loggingRepository
    

  def CreateNewClient(self):
    if not self.tenant.HasPermission(Permission.ManageClient):
      print("Unauthorized")
      return
    
    fullName = input("please enter fullname: ")
    streetName = input("please enter streetname: ")
    houseNumber = input("please enter housenumber: ")
    zipCode = input("please enter zipcode: ")
    try: Client.UpdatezipCode(self, zipCode)
    except ValueError as error: print(error); return
    City = self.selectCity()
    emailAddress = input("please enter emailaddress: ")
    mobilePhoneNumber = input("please enter mobilephonenumber: ")
    try: Client.UpdateMobilePhoneNumber(self, mobilePhoneNumber)
    except ValueError as error: print(error); return
    clientData = tuple(fullName, streetName, houseNumber, zipCode, City, emailAddress, mobilePhoneNumber)
    client = Client(clientData) 
    
    self.clientRepository.CreateClient(client.fullName, client.streetName, client.houseNumber, client.zipCode, client.City, client.emailAddress, client.mobilePhoneNumber)  
    self.loggingRepository.CreateLog(self.tenant, f"New client added: {fullname}","Success", 0)
  
  def SearchClientInfo(self):
    fullName = input("please enter fullname of the client: ")
    if fullName == self.clientRepository.GetClient(fullname):
      print(self.clientRepository.GetClient(fullname).clientRecords)
  # this in user service (talking to davinci)
  def DeleteClientRecord(self):
    if not self.tenant.HasPermission(Permission.DeleteClient):
      print("Unauthorized")
      return
    
    if type(self.tenant) is Advisor:
      print("advisor cannot delete client")    

    self.clientRepository.DeleteClient(fullname)
    self.loggingRepository.CreateLog(self.tenant.username, f"Deleted Client: {fullName}", "Success", 0)
      
    if type(self.tenant) is Advisor:
      self.tenant.CreateClient(fullName, streetName, houseNumber, zipCode, city, emailAddress, mobilePhoneNumber)
      
    
    self.clientRepository.CreateClient(fullName, streetName, houseNumber, zipCode, city, emailAddress, mobilePhoneNumber)  
    self.loggingRepository.CreateLog(self.tenant.username, f"Created client", "Success", 0)

    print("New client is added")
  
  def selectCity(self):
    print('Select a city')
    print('_________________________________\n')
    ClientView.GetMenu(self)