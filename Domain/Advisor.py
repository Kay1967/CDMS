from Domain.User import User
from Enum.Permission import Permission

class Advisor(User):
  def __init__(self, user_data):
    # if user_data[3] != 0:
    #   print("User should be Advisor")
    #   return
    super().__init__(user_data)
    self.SetPermissions()
  
  

  def SetPermissions(self):
    self.hasPermissions = [
    Permission.UpdateAdvisorPassword
  ]

  # def GetClient(self, ):
  # def CreateClient(self, newUsername, newPassword):
  #   self.add_new_user(self)
  #   # self.newUsername = username
  #   # self.newPassword = password
    

    

  # def UpdateClient(self, ):
  # def UpdatePassword(self, ):