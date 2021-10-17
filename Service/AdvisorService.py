import random
import string
from Domain.Advisor import Advisor
from Enum.Permission import Permission
from Repository.UserRepository import *

# every actions in the context of an advisor
class AdvisorService:
  def __init__(self, tenant, userRepository, loggingRepository):
    self.tenant = tenant
    self.userRepository = userRepository
    self.loggingRepository = loggingRepository
  
  def CreateAdvisor(self):
    if not self.tenant.HasPermission(Permission.ManageAdvisor):
      print("Unauthorized")
      return

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

  # helpers
  def GetAndValidateAdvisor(self):
    username = input("please enter username: ").lower()
    user = self.userRepository.GetUser(username)
    if type(user) is not Advisor:
      raise ValueError("User is not an advisor")

    return user

