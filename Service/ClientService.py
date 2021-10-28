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
  
  def UpdateClient(self):
    listToUpdate = self.SearchClientInfo()
    print(listToUpdate)
    pimp = list(listToUpdate.values())[0]
    print(pimp)

    fullName = input("Please enter fullname of the client for update: ")
    
    if fullName != list(listToUpdate.values())[0]:
      raise ValueError("fullname is wrong")
    option1 = int(input("option 1: please enter a number: "))
    option2 = int(input("option 2: please enter a number: "))
    option3 = int(input("option3: please enter a number: "))
    
    if option1 == 5 and option2 == 6 and option3 == 7:
      address = Address()
      print(address.cities)
      address.UpdateCity(int(input("please enter a number from list of cities: ")))
      address.UpdateStreetName(input("please enter a new street: "))
      address.UpdateHouseNumber(input("please enter a new housenumber: "))
      address.UpdateZipCode(input("please enter a new zipcode: "))
      emailAddress = input("please enter emailaddress: ")
      mobilePhoneNumber = input("please enter mobilephonenumber: ")
      fullname = fullName
      
      clients = Client(fullname, emailAddress, mobilePhoneNumber, address)
      
      self.clientRepository.UpdateClient(clients.fullname, clients.address.streetname, clients.address.housenumber, clients.address.zipcode, clients.address.city, clients.emailaddress, clients.mobilephonenumber)
      print(f"Client {clients.fullname} is updated")
    
    elif option1 == 5 and option2 == 0 and option3 == 7:
      address = Address()
      print(address.cities)
      address.UpdateCity(int(input("please enter a number from list of cities: ")))
      address.UpdateStreetName(input("please enter a new street: "))
      address.UpdateHouseNumber(input("please enter a new housenumber: "))
      address.UpdateZipCode(input("please enter a new zipcode: "))
      mobilephonenumber = input("please enter mobilephonenumber: ")
      fullname = fullName
      
      clients = Client(fullname, None, mobilePhoneNumber, address)
      self.clientRepository.UpdateClient(client.fullname, client.address.streetname, client.address.housenumber, client.address.zipcode, client.address.city, client.mobilephonenumber)
    
    elif option1 == 5 and option2 == 6 and option3 == 0:
      address = Address()
      print(address.cities)
      address.UpdateCity(int(input("please enter a number from list of cities: ")))
      address.UpdateStreetName(input("please enter a new street: "))
      address.UpdateHouseNumber(input("please enter a new housenumber: "))
      address.UpdateZipCode(input("please enter a new zipcode: "))
      emailaddress = input("please enter emailaddress: ")
      fullname = fullName
      
      clients = Client(fullname, emailAddress, mobilePhoneNumber, address)
      self.clientRepository.UpdateClient(client.fullname, client.address.streetname, client.address.housenumber, client.address.zipcode, client.address.city, client.emailaddress)
    
    elif option1 == 5 and option2 == 0 and option3 == 0:
      address = Address()
      print(address.cities)
      address.UpdateCity(int(input("please enter a number from list of cities: ")))
      address.UpdateStreetName(input("please enter a new street: "))
      address.UpdateHouseNumber(input("please enter a new housenumber: "))
      address.UpdateZipCode(input("please enter a new zipcode: "))
      fullname = fullName
      
      clients = Client(fullname, emailAddress, mobilePhoneNumber, address)
      self.clientRepository.UpdateClient(client.fullname, client.address.streetname, client.address.housenumber, client.address.zipcode, client.address.city)
   
    elif option1 == 4 and option2 == 6 and option3 == 7:
      address = Address()
      address.UpdateStreetName(input("please enter a new street: "))
      address.UpdateHouseNumber(input("please enter a new housenumber: "))
      address.UpdateZipCode(input("please enter a new zipcode: "))
      emailaddress = input("please enter emailaddress: ")
      mobilephonenumber = input("please enter mobilephonenumber: ")
      fullname = fullName
      
      clients = Client(fullname, emailAddress, mobilePhoneNumber, address)
      self.clientRepository.UpdateClient(client.fullname, client.address.streetname, client.address.housenumber, client.address.zipcode, client.emailaddress, client.mobilephonenumber)
    elif option1 == 4 and option2 == 0 and option3 == 7:
      address = Address()
      address.UpdateStreetName(input("please enter a new street: "))
      address.UpdateHouseNumber(input("please enter a new housenumber: "))
      address.UpdateZipCode(input("please enter a new zipcode: "))
      mobilephonenumber = input("please enter mobilephonenumber: ")
      fullname = fullName
      
      clients = Client(fullname, emailAddress, mobilePhoneNumber, address)
      self.clientRepository.UpdateClient(client.fullname, client.address.streetname, client.address.housenumber, client.address.zipcode, client.mobilephonenumber)
    elif option1 == 4 and option2 == 6 and option3 == 0:
      address = Address()
      address.UpdateStreetName(input("please enter a new street: "))
      address.UpdateHouseNumber(input("please enter a new housenumber: "))
      address.UpdateZipCode(input("please enter a new zipcode: "))
      emailaddress = input("please enter emailaddress: ")
      fullname = fullName
      
      clients = Client(fullname, emailAddress, mobilePhoneNumber, address)
      self.clientRepository.UpdateClient(client.fullname, client.address.streetname, client.address.housenumber, client.address.zipcode, client.emailaddress)
    elif option1 == 4 and option2 == 0 and option3 == 0:
      address = Address()
      address.UpdateStreetName(input("please enter a new street: "))
      address.UpdateHouseNumber(input("please enter a new housenumber: "))
      address.UpdateZipCode(input("please enter a new zipcode: "))
      fullname = fullName
      
      clients = Client(fullname, emailAddress, mobilePhoneNumber, address)
      self.clientRepository.UpdateClient(client.fullname, client.address.streetname, client.address.housenumber, client.address.zipcode)
    elif option1 == 2 and option2 == 6 and option3 == 7:
      address = Address()
      address.UpdateStreetName(input("please enter a new street: "))
      address.UpdateHouseNumber(input("please enter a new housenumber: "))
      emailaddress = input("please enter emailaddress: ")
      mobilephonenumber = input("please enter mobilephonenumber: ")
      fullname = fullName
      
      clients = Client(fullname, emailAddress, mobilePhoneNumber, address)
      self.clientRepository.UpdateClient(client.fullname, client.address.streetname, client.address.housenumber, client.emailaddress, client.mobilephonenumber)
    elif option1 == 2 and option2 == 0 and option3 == 7:
      address = Address()
      address.UpdateStreetName(input("please enter a new street: "))
      address.UpdateHouseNumber(input("please enter a new housenumber: "))
      mobilephonenumber = input("please enter mobilephonenumber: ")
      fullname = fullName
      
      clients = Client(fullname, emailAddress, mobilePhoneNumber, address)
      self.clientRepository.UpdateClient(client.fullname, client.address.streetname, client.address.housenumber, client.mobilephonenumber)
    elif option1 == 2 and option2 == 6 and option3 == 0:
      address = Address()
      address.UpdateStreetName(input("please enter a new street: "))
      address.UpdateHouseNumber(input("please enter a new housenumber: "))
      emailaddress = input("please enter emailaddress: ")
      fullname = fullName
      
      clients = Client(fullname, emailAddress, mobilePhoneNumber, address)
      self.clientRepository.UpdateClient(client.fullname, client.address.streetname, client.address.housenumber, client.emailaddress)
    elif option1 == 2 and option2 == 6 and option3 == 7:
      address = Address()
      address.UpdateStreetName(input("please enter a new street: "))
      address.UpdateHouseNumber(input("please enter a new housenumber: "))
      fullname = fullName
      
      clients = Client(fullname, emailAddress, mobilePhoneNumber, address)
      self.clientRepository.UpdateClient(client.fullname, client.address.streetname, client.address.housenumber)
    elif option1 == 3 and option2 == 6 and option3 == 7:
      address = Address()
      address.UpdateHouseNumber(input("please enter a new housenumber: "))
      emailaddress = input("please enter emailaddress: ")
      mobilephonenumber = input("please enter mobilephonenumber: ")
      fullname = fullName
      
      clients = Client(fullname, emailAddress, mobilePhoneNumber, address)
      self.clientRepository.UpdateClient(client.fullname, client.address.housenumber, client.emailaddress, client.mobilephonenumber)
    elif option1 == 3 and option2 == 0 and option3 == 7:
      address = Address()
      NewHouseNo = address.UpdateHouseNumber(input("please enter a new housenumber: "))
      NewMobilePhoneNo = input("please enter mobilephonenumber: ")
      fullname = fullName
      
      clients = Client(fullname, emailAddress, mobilePhoneNumber, address)
      self.clientRepository.UpdateClient(client.fullname, client.address.housenumber, client.mobilephonenumber)
    elif option1 == 3 and option2 == 6 and option3 == 0:
      address = Address()
      NewHouseNo = address.UpdateHouseNumber(input("please enter a new housenumber: "))
      NewemailAddress = input("please enter emailaddress: ")
      fullname = fullName
      
      clients = Client(fullname, emailAddress, mobilePhoneNumber, address)
      self.clientRepository.UpdateClient(client.fullname, client.address.housenumber, client.emailaddress)
    elif option1 == 3 and option2 == 6 and option3 == 7:
      address = Address()
      address.UpdateHouseNumber(input("please enter a new housenumber: ")) 
      fullname = fullName
      
      clients = Client(fullname, emailAddress, mobilePhoneNumber, address)
      self.clientRepository.UpdateClient(client.fullname, client.address.housenumber)
    elif option1 == 0 and option2 == 6 and option3 == 0:
      NewemailAddress = input("please enter emailaddress: ")
      fullname = fullName
        
      clients = Client(fullname, emailAddress, mobilePhoneNumber, address)
      self.clientRepository.UpdateClient(client.fullname, client.emailaddress) 
    elif option1 == 0 and option2 == 0 and option3 == 7:
      NewMobilePhoneNo = input("please enter mobilephonenumber: ")
      fullname = fullName
      
      clients = Client(fullname, emailAddress, mobilePhoneNumber, address)
      self.clientRepository.UpdateClient(client.fullname, client.mobilephonenumber) 
    # 1. Get Client domain
    # 2. Show client info with number before example: 1. Fullname: Bob larson 2. Street: Streetname
    # 3. Ask for user input which value to change, (Typing 1 means update fullname) 
    # 4. Ask for new value
    # 5. Update domain
    # 6. Call clientRespository.UpdateClient with domain values 
    
  
  
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
