from Component.UserInterface import *
from Enum.Permission import Permission
from Domain.User import User
from Domain.Advisor import Advisor
from Domain.SuperAdmin import SuperAdmin
from Domain.SysAdmin import SysAdmin
from Domain.Client import Client
from Domain.Address import Address
import sqlite3

class ClientService:
  def __init__ (self, tenant, clientRepository, loggingRepository):
    self.clientRepository = clientRepository
    self.tenant = tenant
    self.loggingRepository = loggingRepository
    

  def GetAllClients(self):
    if not self.tenant.HasPermission(Permission.ViewClient):
      print("Unauthorized")
      return

    allClients = self.clientRepository.GetAllClients()
    for client in allClients:
      print(f"Fullname: {client.fullname}" + " " +
            f"Zipcode: {client.address.zipcode}" + " " +
            f"Street: {client.emailaddress}" + " " +
            f"MobileNo.: {client.mobilephonenumber}")
    #print(tabulate([tableAllClients], ['Fullname', 'Street', 'House No.', 'Zipcode', 'City', 'Email', 'Mobile No.']))
    
    #   clientHeaders = ['Fullname', 'Street', 'House No.', 'Zipcode', 'City', 'Email', 'Mobile No.']
    #   clientInfo = [client.fullname, client.streetname, client.housenumber, client.zipcode, client.city, client.emailaddress, client.mobilephonenumber]
    #   clientTable = [clientHeaders, clientInfo]
    #   print(tabulate(clientTable))
      # print(f"Fullname: {user.fullname} " +
      #       f"Username: {user.username} \n" +
      #       f"Role: {type(user).__name__}\n")

  def CreateNewClient(self):
    if not self.tenant.HasPermission(Permission.CreateClient):
      print("Unauthorized")
      return
    
    try:
      fullname = input("please enter fullname: ")

      address = Address()
      address.UpdateStreetName(input("please enter streetname: "))
      address.UpdateHouseNumber(input("please enter housenumber: "))
      address.UpdateZipCode(input("please enter zipcode: "))
      print(address.cities)
      address.UpdateCity(int(input("please enter a number from list of cities: ")))

      emailAddress = input("please enter emailaddress: ")
      mobilePhoneNumber = input("please enter mobilephonenumber: ")
      client = Client(fullname, emailAddress, mobilePhoneNumber, address)
    except ValueError as error: print(error); return
     
    self.clientRepository.CreateClient(client.fullname, client.address.streetname, client.address.housenumber, client.address.zipcode, client.address.city, client.emailaddress, client.mobilephonenumber)  
    self.loggingRepository.CreateLog(self.tenant, f"New client added: {fullname}","Success", 0)
    print(f"New client {client.fullname} is added")
#f"1. Fullname: {client.fullname}" + " " +
  def UpdateClient(self):

    clients = Client(fullname, emailAddress, mobilePhoneNumber, address)
    for client in clients:
      print(
            f"2. Street: {client.address.streetname}" + " " +
            f"3. Housenumber: {client.address.housenumber}" + " " +
            f"4. Zipcode: {clien.address.zipcode}" + " " +
            f"5. City: {client.address.city}" + " " +
            f"6. Emailaddress: {client.emailaddress}" + " " +
            f"7. Mobilenumber: {client.mobilephonenumber}")
    
    chooseOption = int(input("please enter an number: "))      
    if chooseOption == 2:
      fullName = intpu("please enter fullname of the client: ")
     # if fullName == self.client.fullname:
        #streetName = self.CreateNewClient(address.UpdateStreetName)

    
    # 1. Get Client domain
    # 2. Show client info with number before example: 1. Fullname: Bob larson 2. Street: Streetname
    # 3. Ask for user input which value to change, (Typing 1 means update fullname) 
    # 4. Ask for new value
    # 5. Update domain
    # 6. Call clientRespository.UpdateClient with domain values 
    pass
  
  def SearchClientInfo(self):
    if not self.tenant.HasPermission(Permission.ManageClient):
      print("Unauthorized")
      return

    fullname = input("please enter fullname of the client: ")
    if fullname == self.clientRepository.GetClient(fullname):
      print(self.clientRepository.GetClient(fullname).clientRecords)
  # this in user service (talking to davinci)
  def DeleteClientRecord(self):
    if not self.tenant.HasPermission(Permission.ManageClient):
      print("Unauthorized")
      return
    
    if type(self.tenant) is Advisor:
      print("advisor cannot delete client")    
    fullname = input("please enter fullname of the client: ")
    self.clientRepository.DeleteClient(fullname)
    self.loggingRepository.CreateLog(self.tenant.username, f"Deleted Client: {fullname}", "Success", 0)
      
    # if type(self.tenant) is Advisor:
    #   self.tenant.CreateClient(fullName, streetName, houseNumber, zipCode, city, emailAddress, mobilePhoneNumber)
      
    
    # self.clientRepository.CreateClient(fullName, streetName, houseNumber, zipCode, city, emailAddress, mobilePhoneNumber)  
    # self.loggingRepository.CreateLog(self.tenant.username, f"Created client", "Success", 0)

  def DeleteClient():
    pass

  def selectCity(self):
    print('Select a city')
    print('_________________________________\n')
    ClientView.GetMenu(self)