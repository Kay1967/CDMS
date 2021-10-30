from datetime import datetime as dt
from Domain.User import *
from Domain.Client import *
from Domain.Advisor import Advisor
from Enum.Permission import Permission
from Repository.UserRepository import *
from Repository.ClientRepository import *

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

    try:
      advisor = Advisor(None, None, None, False, None)
      advisor.UpdateUsername(input("please enter username: "))
      advisor.fullname = input("please enter fullname: ")
      advisor.lastLogin = dt.now().strftime("%d-%m-%Y")
      advisor.GenerateAndUpdatePassword()
    except ValueError as error: print(error); return

    self.userRepository.CreateUser(advisor.username, advisor.password, advisor.fullname, "0", advisor.lastLogin)  
    self.loggingRepository.CreateLog(self.tenant.username, f"New advisor added: {username}", "Success", 0)
    print(f"Created new advisor: {advisor.username}\nPassword : {advisor.password}") 

  def ViewAdvisorInfo(self, advisor):
    if not self.tenant.HasPermission(Permission.ManageAdvisor):
      print("Unauthorized")
      return

    print(f'''1. Fullname: {advisor.fullname}\n2. Username: {advisor.username}\n''')
  
  def UpdateAdvisor(self):
    if not self.tenant.HasPermission(Permission.ManageAdvisor):
      print("Unauthorized")
      return

    try: advisor = self.GetAndValidateAdvisor() 
    except ValueError as error: print(error); return    

    self.ViewAdvisorInfo(advisor)

    # save fullname to know which client to update even after changing name
    usernameRecord = advisor.username
    stillUpdating = True
    while stillUpdating:
        fieldToUpdate = int(input("Please enter number to select which field to update for client or 0 to exit: "))
        if fieldToUpdate == 1:
          advisor.fullname = input("please enter a new fullname: ")
        if fieldToUpdate == 2:
          advisor.UpdateUsername(input("please enter a new username: "))
        if fieldToUpdate == 0:
          stillUpdating = False

    self.userRepository.UpdateUser(advisor.username, advisor.fullname, usernameRecord)  
    self.loggingRepository.CreateLog(self.tenant.username, f"Advisor updated {usernameRecord}:  {advisor.username}, {advisor.fullname}", "Success", 0)
  
    if usernameRecord != advisor.username:
      print(f"Advisor {usernameRecord} -> {advisor.username} is updated")
    else: 
      print(f"Advisor {usernameRecord} is updated")

  def UpdatePasswordForAdvisor(self):
    # if self.tenant is not Advisor and self.tenant is not SysAdmin and self.tenant is not SuperAdmin:
    # Haspermission is a method that gives back a boolean based on if the tenant has the permission UpdateAdvisorPassword
    if not self.tenant.HasPermission(Permission.UpdateAdvisorPassword):
      print("Unauthorized")
      return

    if type(self.tenant) is Advisor:
      advisor = self.tenant
      print("Password criteria:\nCannot be the same as old password\nBetween 7 and 31 characters\nWith atleast one uppercase, one lowercase and one special\n")
      newPassword = input("please enter a new password: ")
      try: self.tenant.UpdatePassword(newPassword)
      except ValueError as error: print(error); return
    else:
      try:
        advisor = self.GetAndValidateAdvisor()
        advisor.GenerateAndUpdatePassword() 
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
    print(f"Deleted Advisor: {advisor.username}") 

  # helpers
  def GetAndValidateAdvisor(self):
    username = input("please enter username: ")
    user = self.userRepository.GetUser(username)
    if type(user) is not Advisor:
      raise ValueError("User is not an advisor")

    return user

  