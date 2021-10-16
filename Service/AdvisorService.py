import random
import string
from Domain.SuperAdmin import SuperAdmin
from Enum.Permission import Permission
from Repository.UserRepository import *

# every actions in the context of an advisor
class AdvisorService:
  def __init__(self, userRepository, tenant):
    self.userRepository = userRepository
    self.tenant = tenant

  def UpdatePasswordForAdvisor(self):
    # if self.tenant is not Advisor and self.tenant is not SysAdmin and self.tenant is not SuperAdmin:
    # Haspermission is a method that gives back a boolean based on if the tenant has the permission UpdateAdvisorPassword
    if not self.tenant.HasPermission(Permission.UpdateAdvisorPassword):
      print("Unauthorized")
      return

    if self.tenant is Advisor:
      username = self.tenant.username
      newPassword = input("please enter a new password: ")
      self.tenant.UpdatePassword(newPassword)
    else:
      username = input("please enter username: ").lower() 
      user = self.userRepository.GetUser(username)
      if user is not Advisor:
        print("User is not an advisor")
        return 
      newPassword = ''.join(random.choice(string.ascii_lowercase) for i in range(10))
      user.UpdatePassword(newPassword)
    
    self.userRepository.UpdatePassword(username, newPassword)  
    print("New Password for " + username + ". Password: " + newPassword)
