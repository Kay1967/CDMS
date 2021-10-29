from Domain.User import *
from Domain.SuperAdmin import *
from Enum.Permission import Permission

class UserService:
  def __init__(self, tenant, userRepository):
    self.tenant = tenant
    self.userRepository = userRepository
    
  def GetAllUsers(self):
    if not self.tenant.HasPermission(Permission.ViewAllUsers):
      print("Unauthorized")
      return
    allUsers = self.userRepository.GetAllUsers()
    for user in allUsers:
      print(f"Fullname: {user.fullname} \n" +
            f"Username: {user.username} \n" +
            f"Role: {type(user).__name__}\n")