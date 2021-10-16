from Domain.SysAdmin import SysAdmin
from Enum.Permission import Permission

class SuperAdmin(SysAdmin):
  hasPermissions = [
    Permission.UpdateAdvisorPassword
  ]  
  
  def __init__(self, username, password):
    self.username = username
    self.password = password
    self.name = 'superadmin'
    self.admin = 1