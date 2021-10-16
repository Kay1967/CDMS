
from Domain.Advisor import Advisor
from Enum.Permission import Permission

class SysAdmin(Advisor):
    hasPermissions = [
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