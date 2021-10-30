from Domain.SysAdmin import SysAdmin
from Enum.Permission import Permission

class SuperAdmin(SysAdmin):
  def __init__(self, username, password, fullname, admin, lastLogin):
    super().__init__(username, password, fullname, admin, lastLogin)
    self.SetPermissions()
  
  def SetPermissions(self):
    self.hasPermissions = [
    Permission.ViewAllUsers,
    Permission.ManageAdvisor,
    Permission.ManageSysAdmin,
    Permission.ManageClient,
    Permission.ManageLog,
    Permission.ManageBackup,
  ]
