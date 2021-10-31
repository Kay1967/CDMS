from Domain.User import *
from Domain.SuperAdmin import *
from Enum.Permission import Permission

class UserService:
  def __init__(self, tenant, userRepository, loggingRepository):
    self.tenant = tenant
    self.userRepository = userRepository
    self.loggingRepository = loggingRepository
    
  def GetAllUsers(self):
    if not self.tenant.HasPermission(Permission.ViewAllUsers):
      self.loggingRepository.CreateLog(self.tenant.username, f"{self.CreateSysAdmin.__name__}", "Unauthorized", 1)
      return
    allUsers = self.userRepository.GetAllUsers()
    for user in allUsers:
      print(f"Fullname: {user.fullname} \n" +
            f"Username: {user.username} \n" +
            f"Role: {type(user).__name__}\n")