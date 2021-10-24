from Enum.Permission import Permission
from Repository.UserRepository import UserRepository
from Service.AdvisorService import AdvisorService
class UserService:
  def __init__(self, tenant, userRepository, advisorService):
    self.tenant = tenant
    self.userRepository = userRepository
    self.advisorService = advisorService

  def GetAllUsers(self):
    if not self.tenant.HasPermission(Permission.ViewAllUsers):
      print("Unauthorized")
      return
    allUsers = self.userRepository.GetAllUsers()
    for user in allUsers:
      print(f"Fullname: {user.name} \n" +
            f"Username: {user.username} \n" +
            f"Role: {type(user).__name__}\n")
      
  # def CreateAdvisor(self):
  #   if not self.tenant.HasPermission(Permission.ManageAdvisor):
  #     print("Unauthorized")
  #     return
  #   username = input("please enter username: ")
  #   password = self.userRepository.UpdatePasswordForAdvisor()
  #   fullname = input("please enter fullname: ")
  #   admin = 3 
  #   self.userRepository.CreateUser(username, password, fullname, admin)  
  #   self.loggingRepository.CreateLog(self.tenant.username, f"New advisor added: {advisor.username}", "Success", 0)


  
  
  
