
from Domain.Advisor import Advisor
from Enum.Permission import Permission

class SysAdmin(Advisor):
  def __init__(self, user_data):
    # if user_data[3] != 1:
    #   print("User should be System administrator")
    #   return
    super().__init__(user_data)
    self.SetPermissions()

  def SetPermissions(self):
    self.hasPermissions = [
    Permission.UpdateAdvisorPassword,
    Permission.ViewAllUsers,
    Permission.ManageAdvisor,
    Permission.UpdateSysAdminPassword
  ]
  # def __init__(self):
  
  # def GetUsers(self):

  # def CreateAdvisor(self):
    
  # def UpdateAdvisor(self):
  # def DeleteAdvisor(self):

  # def ResetAndGetPasswordForAdvisor(self):
  # def CreateBackup(self):
  # def GetLogFile(self):