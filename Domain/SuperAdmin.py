from Domain.SysAdmin import SysAdmin
from Enum.Permission import Permission

class SuperAdmin(SysAdmin):
  def __init__(self, username, password):
    super().__init__(username, password, 'superadmin', True)
    self.SetPermissions()
  
  
  def SetPermissions(self):
    self.hasPermissions = [
    Permission.ViewAllUsers,
    Permission.ManageAdvisor,
    Permission.ManageSysAdmin,
    Permission.ManageClient,
  ]
