
from Domain.Advisor import Advisor
from Enum.Permission import Permission

class SysAdmin(Advisor):
  def __init__(self, user_data):
    super().__init__(user_data)
    self.SetPermissions()
  
  def SetPermissions(self):
    self.hasPermissions = [
    Permission.UpdateAdvisorPassword
  ]
  # def __init__(self):
  
  # def GetUsers(self):

  # def CreateAdvisor(self):
    
  # def UpdateAdvisor(self):
  # def DeleteAdvisor(self):

  # def ResetAndGetPasswordForAdvisor(self):
  # def CreateBackup(self):
  # def GetLogFile(self):