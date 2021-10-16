from Enum.Permission import Permission
class UserService:
  def __init__(self, tenant, userRepository):
    self.tenant = tenant
    self.userRepository = userRepository

  def GetAllUsers(self):
    if not self.tenant.HasPermission(Permission.ViewAllUsers):
      print("Unauthorized")
      return
    print(self.userRepository.GetAllUsers())