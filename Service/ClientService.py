from Component.UserInterface import *
from Enum.Permission import Permission
from Domain.User import User
from Domain.Advisor import Advisor
from Domain.SuperAdmin import SuperAdmin
from Domain.SysAdmin import SysAdmin
from Domain.Client import Client
from Domain.Address import Address
from tabulate import tabulate
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
      client_dict = {"1.Fullname":client.fullname,
                     "2.Street":client.address.streetname,
                     "3.HouseNo.":client.address.housenumber,
                     "4.Zipcode":client.address.zipcode,
                     "5.City":client.address.city,
                     "6.Email":client.emailaddress,
                     "7.MobileNo.":client.mobilephonenumber}
      #print(client_dict)
      #clients = client_dict.values()
      print(client_dict)

      #return clients

      # print(
      #       f"1. Fullname: {client.fullname}" + " " +
      #       f"2. Street: {client.address.streetname}" + " " +
      #       f"3. HouseNo.: {client.address.housenumber}" + " " +
      #       f"4. Zipcode: {client.address.zipcode}" + " " +
      #       f"5. City: {client.address.city}" + " " +
      #       f"6. Email: {client.emailaddress}" + " " + 
      #       f"7. MobileNo.: {client.mobilephonenumber}"
      #      )
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

  def SearchClientInfo(self):
    if not self.tenant.HasPermission(Permission.ManageClient):
      print("Unauthorized")
      return

    fullname = input("please enter fullname of the client for search: ")
    client1 = self.clientRepository.GetClient(fullname)
    # for c in client1:
    dict_client = {"1.Fullname":client1.fullname,
                   "2.Street":client1.address.streetname,
                   "3.HouseNo.":client1.address.housenumber,
                   "4.Zipcode":client1.address.zipcode,
                   "5.City":client1.address.city,
                   "6.Email":client1.emailaddress,
                   "7.MobileNo.":client1.mobilephonenumber}
    #print(dict_client)
    return dict_client
  
  def UpdateClientInfo(self):
    if not self.tenant.HasPermission(Permission.UpdateClientInfo):
      print("Unauthorized")
      return

    listToUpdate = self.SearchClientInfo()
    print(listToUpdate)
    fullName = input("Please enter fullname of the client for update: ")
    
    address = Address()
    address.streetname = list(listToUpdate.values())[1]
    address.housenumber = list(listToUpdate.values())[2]
    address.zipcode = list(listToUpdate.values())[3]
    address.city = list(listToUpdate.values())[4]
    # fullname = list(listToUpdate.values())[0]
    emailaddress = list(listToUpdate.values())[5]
    mobilephonenumber = list(listToUpdate.values())[6]

    options = {"1": "streetname", "2": "housenumber", "3": "zipcode", "4": "city", "5": "email", "6": "mobile"}
    print(f"options = {options}")
    if options == list(listToUpdate.values())[0]:
      address.UpdateStreetName("please enter new streetname: ")
      clients = Client(fullName, emailaddress, mobilephonenumber, address)
    
      self.clientRepository.UpdateClient(clients.fullname, clients.address.streetname)
      self.loggingRepository.CreateLog(self.tenant.username, f"Client updated: {clients.fullname}", "Success", 0)
      print(f"Client {clients.streetname} for {clients.fullname} is updated")
    elif option == 3 :
      address = Address()
      address.UpdateHouseNumber(input("please enter a new housenumber: "))
      fullname = fullName
      clients = Client(fullname, emailAddress, mobilePhoneNumber, address)
      
      self.clientRepository.UpdateClient(clients.fullname, clients.address.housenumber)
      self.loggingRepository.CreateLog(self.tenant.username, f"Client updated: {clients.fullname}", "Success", 0)
      print(f"Client {clients.housenumber} for {clients.fullname} is updated")
    elif option == 4 :
      address = Address()
      address.UpdateZipCode(input("please enter a new zipcode: "))
      fullname = fullName
      clients = Client(fullname, emailAddress, mobilePhoneNumber, address)
      
      self.clientRepository.UpdateClient(clients.fullname, clients.address.zipcode)
      self.loggingRepository.CreateLog(self.tenant.username, f"Client updated: {clients.fullname}", "Success", 0)
      print(f"Client {clients.zipcode} for {clients.fullname} is updated")
    elif option == 5 :
      address = Address()
      print(address.cities)
      address.UpdateCity(int(input("please enter a number from list of cities: ")))
      fullname = fullName
      clients = Client(fullname, emailAddress, mobilePhoneNumber, address)
      
      self.clientRepository.UpdateClient(clients.fullname, clients.address.zipcode)
      self.loggingRepository.CreateLog(self.tenant.username, f"Client updated: {clients.fullname}", "Success", 0)
      print(f"Client {clients.zipcode} for {clients.fullname} is updated")
    
    elif option == 6:
      emailaddress = input("please enter emailaddress: ")
      fullname = fullName
      clients = Client(fullname, emailaddress, 0, 0)
      
      self.clientRepository.UpdateClient(clients.fullname, clients.emailaddress)
      self.loggingRepository.CreateLog(self.tenant.username, f"Client updated: {clients.fullname}", "Success", 0)
      print(f"Client {clients.emailaddress} for {clients.fullname} is updated")
    elif option == 7:
      mobilePhoneNumber = input("please enter mobilephonenumber: ")
      fullname = fullName
      clients = Client(fullname, emailAddress, mobilePhoneNumber, address)
      
      self.clientRepository.UpdateClient(clients.fullname, clients.mobilephonenumber)
      self.loggingRepository.CreateLog(self.tenant.username, f"Client updated: {clients.fullname}", "Success", 0)
      print(f"Client {clients.mobilephonenumber} for {clients.fullname} is updated")
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
