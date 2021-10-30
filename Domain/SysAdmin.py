from Domain.Advisor import Advisor
from Enum.Permission import Permission

class SysAdmin(Advisor):
  def __init__(self, username, password, fullname, admin, lastLogin):
    if admin != True:
      raise ValueError("User should be System administrator")

    super().__init__(username, password, fullname, admin, lastLogin)
    self.SetPermissions()

  def SetPermissions(self):
    self.hasPermissions = [
    Permission.ViewAllUsers,
    Permission.ManageAdvisor,
    Permission.ManageClient,
    Permission.UpdateSysAdminPassword,
    Permission.ManageLog,
    Permission.ManageBackup,
  ]