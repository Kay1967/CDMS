from enum import Enum
from Domain.SuperAdmin import SuperAdmin
from Enum.Permission import Permission
from Repository.UserRepository import *
# every actions in the context of an advisor
class AdvisorService:
  def __init__(self, userRepository, tenant):
    self.userRepository = userRepository
    self.tenant = tenant

  def UpdatePasswordForAdvisor(self, username, newPassword):
    # if self.tenant is not Advisor and self.tenant is not SysAdmin and self.tenant is not SuperAdmin:
    if self.tenant.HasPermission(Permission.UpdateAdvisorPassword):
      print("Unauthorized")
      return
      
    user = self.userRepository.GetUser(username)
    if user is not Advisor:
      print("User is not an advisor")
      return 
    
