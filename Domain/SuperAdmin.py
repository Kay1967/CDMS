from Domain.SysAdmin import SysAdmin
from Enum.Permission import Permission

class SuperAdmin(SysAdmin):
  def __init__(self, username, password):
    self.username = username
    self.password = password
    self.name = 'superadmin'
    self.admin = 1
    self.SetPermissions()
  
  
  def SetPermissions(self):
    self.hasPermissions = [
    Permission.UpdateAdvisorPassword,
    Permission.ViewAllUsers,
    Permission.ManageAdvisor,
    Permission.UpdateSysAdminPassword,
    Permission.ManageSysAdmin,
    Permission.UpdateClientInfo,
    Permission.ManageClient,
    Permission.DeleteClient
  ]
