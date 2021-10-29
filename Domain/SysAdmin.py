from Domain.Advisor import Advisor
from Enum.Permission import Permission

class SysAdmin(Advisor):
  def __init__(self, username, password, fullname, admin, lastLogin):
    # if user_data[3] != 1:
    #   print("User should be System administrator")
    #   return
    super().__init__(username, password, fullname, admin, lastLogin)
    self.SetPermissions()

  def SetPermissions(self):
    self.hasPermissions = [
    Permission.ViewAllUsers,
    Permission.ManageAdvisor,
    Permission.ManageClient,
    Permission.UpdateSysAdminPassword,
    Permission.ManageLog,
  ]
  # 
  
  # def DeleteAdvisor(self):

  # def ResetAndGetPasswordForAdvisor(self):
  # def CreateBackup(self):
  # def GetLogFile(self):