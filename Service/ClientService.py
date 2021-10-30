from Component.UserInterface import *
from Enum.Permission import Permission
from Domain.Client import Client
from Domain.Address import Address

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
      
      print(client_dict)

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

  def ViewAndGetClientInfo(self):
    if not self.tenant.HasPermission(Permission.ViewClient):
      print("Unauthorized")
      return

    client = self.GetClient()      
    
    print(f'''1. Fullname: {client.fullname}\n
2.Street: {client.address.streetname}\n
3.HouseNo.: {client.address.housenumber}\n
4.Zipcode: {client.address.zipcode}\n
5.City: {client.address.city}\n
6.Email: {client.emailaddress}\n
7.MobileNo.: {client.mobilephonenumber}\n''')

    return client
  
  def UpdateClientInfo(self):
    if not self.tenant.HasPermission(Permission.UpdateClientInfo):
      print("Unauthorized")
      return   

    client = self.ViewAndGetClientInfo()

    # save fullname to know which client to update even after changing name
    fullnameRecord = client.fullname
    stillUpdating = True
    while stillUpdating:
        fieldToUpdate = int(input("Please enter number to select which field to update for client or 0 to exit: "))
        if fieldToUpdate == 1:
          client.fullname = input("please enter a new fullname: ")
        if fieldToUpdate == 2:
          client.address.UpdateStreetName(input("please enter streetname: "))
        if fieldToUpdate == 3:
          client.address.UpdateHouseNumber(input("please enter housenumber: "))
        if fieldToUpdate == 4:
          client.address.UpdateZipCode(input("please enter a new zipcode: "))
        if fieldToUpdate == 5:
          client.address.UpdateCity(int(input("please enter a number from list of cities: ")))
        if fieldToUpdate == 6:
          client.UpdateEmailAdress(input("please enter emailaddress: "))
        if fieldToUpdate == 7:
          client.UpdateMobilePhoneNumber(input("please enter mobilephonenumber: +31-6"))
        if fieldToUpdate == 0:
          stillUpdating = False

    self.clientRepository.UpdateClient(client.fullname, client.address.streetname, client.address.housenumber, client.address.zipcode, client.address.city, client.emailaddress, client.mobilephonenumber, fullnameRecord)  
    self.loggingRepository.CreateLog(self.tenant.username, f"Client updated {fullnameRecord}:  {client.fullname}, {client.address.streetname}, {client.address.housenumber}, {client.address.zipcode}, {client.address.city}, {client.emailaddress}, {client.mobilephonenumber}", "Success", 0)
  
    if fullnameRecord != client.fullname:
      print(f"Client {fullnameRecord} -> {client.fullname} is updated")
    else: 
      print(f"Client {fullnameRecord} is updated")

  
  def DeleteClientRecord(self):
    if not self.tenant.HasPermission(Permission.ManageClient):
      print("Unauthorized")
      return

    client = self.GetClient()   

    self.clientRepository.DeleteClient(client.fullname)
    self.loggingRepository.CreateLog(self.tenant.username, f"Deleted Client: {client.fullname}", "Success", 0)
    print(f"Deleted Client: {client.fullname}") 

  # helpers
  def GetClient(self):
    fullname = input("please enter fullname of the client: ")

    try: client = self.clientRepository.GetClient(fullname)
    except ValueError as error: print(error); return 

    return client

