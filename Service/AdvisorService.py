from Repository.UserRepository import *
# every actions in the context of an advisor
class AdvisorService:
  def __init__(self, userRepository, tenant):
    self.userRepository = userRepository
    self.tenant = tenant

  def UpdatePasswordForAdvisor(self, username, newPassword):
    if tenant is not Advisor and tenant is not SysAdmin and tenant is not SuperAdmin:
      print("Unauthorized")
    user = self.userRepository.GetUser(username)
    if user is not Advisor:
      print("User is not an advisor")
      return 
    
