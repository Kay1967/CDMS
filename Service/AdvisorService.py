import random
import string
from Domain.User import *
from Domain.Client import *
from Domain.Advisor import Advisor
from Enum.Permission import Permission
from Repository.UserRepository import *
from Repository.ClientRepository import *
from Service.ClientService import ClientService

# every actions in the context of an advisor
class AdvisorService:
  def __init__(self, tenant, userRepository, loggingRepository, clientRepository):
    self.tenant = tenant
    self.userRepository = userRepository
    self.loggingRepository = loggingRepository
    self.clientRepository = clientRepository
  # this must be in user service (talking to davinci)  
  def CreateAdvisor(self):
    if not self.tenant.HasPermission(Permission.ManageAdvisor):
      print("Unauthorized")
      return
    if type(self.tenant) is Advisor:
      print("access denied!")
    userName = input("please enter userName: ")
    
    Password = User.GenerateAndUpdatePassword()
    Fullname = input("please enter fullname: ")
    Admin = 0 
    userData = tuple(userName, Password, Fullname, 0)
    advisor = Advisor(userData)
    self.userRepository.CreateUser(advisor.userName, advisor.Password, advisor.Fullname, Admin)  
    self.loggingRepository.CreateLog(self.tenant.userName, f"New advisor added: {userName}", "Success", 0)

  def UpdatePasswordForAdvisor(self):
    # if self.tenant is not Advisor and self.tenant is not SysAdmin and self.tenant is not SuperAdmin:
    # Haspermission is a method that gives back a boolean based on if the tenant has the permission UpdateAdvisorPassword
    if not self.tenant.HasPermission(Permission.UpdateAdvisorPassword):
      print("Unauthorized")
      return

    if type(self.tenant) is Advisor:
      advisor = self.tenant.username
      newPassword = input("please enter a new password: ")
      try: self.tenant.UpdatePassword(newPassword)
      except ValueError as error: print(error); return
    else:
      try:
        advisor = self.GetAndValidateAdvisor()
        advisor.GenerateAndUpdatePassword() 
        print(f"Password updated for: {advisor.username}\n New password : {advisor.password}") 
      except ValueError as error: print(error); return    
    
    self.userRepository.UpdatePassword(advisor.username, advisor.password)  
    self.loggingRepository.CreateLog(self.tenant.username, f"Updated Password For Advisor: {advisor.username}", "Success", 0)

    print("New Password for " + advisor.username + ". Password: " + advisor.password)

  def DeleteAdvisor(self):
    if not self.tenant.HasPermission(Permission.ManageAdvisor):
      print("Unauthorized")
      return
    
    try: advisor = self.GetAndValidateAdvisor()
    except ValueError as error: print(error); return    

    self.userRepository.DeleteUser(advisor.username)
    self.loggingRepository.CreateLog(self.tenant.username, f"Deleted Advisor: {advisor.username}", "Success", 0)


    
  # 

  # def UpdateClientInfo(self):
  #   if not self.tenant.HasPermission(Permission.UpdateClientInfo):
  #     print("Unauthorized")
  #     return

  #   if type(self.tenant) is Advisor:
  #     clientToUpdate = input("please enter fullname of the client: ")
  #     if clientToUpdate == self.CreateNewClient().fullname:
  #       try: self.GetItemsToUpdate() 
  #       except ValueError as error: print(error); return
  #     else:
  #       try:
  #         advisor = self.GetAndValidateAdvisor()
  #         self.GetItemsToUpdate()  
  #       except ValueError as error: print(error); return    
    
  #   self.tenant.GetItemsToUpdate()
  #   #UpdateClient(NewStreetName, NewHousenNmber, NewZipCode,NewCity, NewEmailAddress, NewMobilePhone)  
  #   self.loggingRepository.CreateLog(self.tenant.username, f"Updated client by Advisor: {advisor.username}", "Success", 0)

  #   print("New Password for " """+ advisor.username + ". Password: " + advisor.password""")

  
  
  # helpers
  def GetAndValidateAdvisor(self):
    username = input("please enter username: ").lower()
    user = self.userRepository.GetUser(username)
    if type(user) is not Advisor:
      raise ValueError("User is not an advisor")

    return user

# helper menu for cities
  