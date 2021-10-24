from termcolor import colored
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

      clientData = tuple(fullname, emailAddress, mobilePhoneNumber)
      client = Client(clientData, address)
        
    except ValueError as error: print(error); return
     
    
    self.clientRepository.CreateClient(client.fullName, client.address.streetName, client.address.houseNumber, client.address.zipCode, client.address.City, client.emailAddress, client.mobilePhoneNumber)  
    self.loggingRepository.CreateLog(self.tenant, f"New client added: {fullname}","Success", 0)
  
  def SearchClientInfo(self):
    fullName = input("please enter fullname of the client: ")
    if fullName == self.clientRepository.GetClient(fullname):
      print(self.clientRepository.GetClient(fullname).clientRecords)
  # this in user service (talking to davinci)
  def DeleteClientRecord(self):
    if not self.tenant.HasPermission(Permission.ManageClient):
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