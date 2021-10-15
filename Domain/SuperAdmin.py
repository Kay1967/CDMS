from Domain.SysAdmin import SysAdmin

class SuperAdmin(SysAdmin):
  def __init__(self, username, password):
    self.username = username
    self.password = password
    self.name = 'superadmin'
    self.admin = 1