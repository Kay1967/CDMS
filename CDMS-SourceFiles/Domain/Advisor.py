from Domain.User import User
from Enum.Permission import Permission

class Advisor(User):
  def __init__(self, username, password, fullname, admin, lastLogin):
    # if user_data[3] != 0:
    #   print("User should be Advisor")
    #   return
    super().__init__(username, password, fullname, admin, lastLogin)
  