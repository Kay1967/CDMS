from datetime import datetime as dt
from Component.UserInterface import *

class LoginService:
  loggedin = False
  def __init__ (self, userRepository, loggingRepository):
    self.userRepository = userRepository
    self.loggingRepository = loggingRepository

  def login(self):
    username = input("please enter username: ")
    password = input("please enter password: ")
    
    try:
      user = self.userRepository.GetUser(username)
      if user == None or user.password != password:  # An empty result evaluates to False.
          raise ValueError(f"Login Try with: Username: {username} {password} ", False)
      else:
          self.loggedin = True
          self.tenant = user
          self.userRepository.UpdateLastLogin(dt.now(), self.tenant.username)
    except ValueError as error: self.CreateLogFromException(self.CreateNewClient.__name__, error); return    

  def close():
    pass

  def logout(self):
    self.loggedin = 0
    self.loggedin_user = None
    self.admin_is_loggedin = 0 


  def close(self):
    self.userRepository.close()

  def CreateLogFromException(self, descriptionOfActivity, exception):
    showUser = exception.args[1]
    if showUser:
      print(exception.args[0])
    else:
      print("something went wrong")
    self.loggingRepository.CreateLog(self.tenant.username, descriptionOfActivity, f"ValueError:{exception.args[0]}", "1")
