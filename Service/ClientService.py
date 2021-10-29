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

  def ViewClientInfo(self, client):
    if not self.tenant.HasPermission(Permission.ViewClient):
      print("Unauthorized")
      return

    # for c in client1:
    print(f'''1. Fullname: {client.fullname}"
"2.Street": {client.address.streetname}\n,
"3.HouseNo.": {client.address.housenumber}\n
"4.Zipcode": {client.address.zipcode}\n
"5.City": {client.address.city}\n
"6.Email": {client.emailaddress}\n
"7.MobileNo.": {client.mobilephonenumber}\n''')
  
  def UpdateClientInfo(self):
    if not self.tenant.HasPermission(Permission.UpdateClientInfo):
      print("Unauthorized")
      return


    try: client = self.GetClient() 
    except ValueError as error: print(error); return    

    self.ViewClientInfo(client)
    
    stillUpdating = False
    while stillUpdating:
        fieldToUpdate = input("Please enter number to select which field to update for client or 0 to exit: ")
        if fieldToUpdate == 1:
          result = intput("please enter a new fullname: ")
          client.UpdateClient(result)
        if fieldToUpdate == 2:
          result = address.UpdateStreetName(input("please enter streetname: "))
          client.UpdateClient(result)
        if fieldToUpdate == 3:
          result= address.UpdateHouseNumber(input("please enter housenumber: "))
          client.UpdateClient(result)
        if fieldToUpdate == 4:
          result = intput("please enter a new zipcode: ")
          client.UpdateClient(result)
        if fieldToUpdate == 5:
          print(address.cities)
          result = address.UpdateCity(int(input("please enter a number from list of cities: ")))
          client.UpdateClient(result)
        if fieldToUpdate == 6:
          result = input("please enter emailaddress: ")
          client.UpdateClient(result)
        if fieldToUpdate == 7:
          result = input("please enter mobilephonenumber: ")
          client.UpdateClient(result)
        if fieldToUpdate == 0:
          stillUpdating = True

      
    self.clientRepository.UpdateClient(result)
    self.loggingRepository.CreateLog(self.tenant.username, f"Client updated: {client.fullname}", "Success", 0)
    print(f"Client {fullname} for {client.fullname} is updated")
    
  
  def DeleteClientRecord(self):
    if not self.tenant.HasPermission(Permission.ManageClient):
      print("Unauthorized")
      return

    try: sysAdmin = self.GetAndValidateSysAdmin()
    except ValueError as error: print(error); return    

    self.clientRepository.DeleteClient(sysAdmin.username)
    self.loggingRepository.CreateLog(self.tenant.username, f"Deleted Client: {sysAdmin.username}", "Success", 0)
    print(f"Deleted Client: {sysAdmin.username}") 

  # helpers
  def GetClient(self):
    fullname = input("please enter username: ").lower()
    client = self.userRepository.GetUser(fullname)

    return client

