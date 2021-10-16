from Domain.User import User
from Enum.Permission import Permission

class Advisor(User):
  hasPermissions = [
    Permission.UpdateAdvisorPassword
    ]  

  # def GetClient(self, ):
  # def CreateClient(self, newUsername, newPassword):
  #   self.add_new_user(self)
  #   # self.newUsername = username
  #   # self.newPassword = password
    

    

  # def UpdateClient(self, ):
  # def UpdatePassword(self, ):