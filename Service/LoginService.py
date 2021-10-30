from datetime import datetime as dt
from Component.UserInterface import *
from Domain.SuperAdmin import SuperAdmin

class LoginService:
  loggedin = False
  def __init__ (self, userRepository):
    self.userRepository = userRepository

  def login(self):
    username = input("please enter username: ")
    password = input("please enter password: ")
    
    user = self.userRepository.GetUser(username)
    if user == None or user.password != password:  # An empty result evaluates to False.
        print("Login failed")
    else:
        self.loggedin = True
        self.tenant = user
        self.userRepository.UpdateLastLogin(dt.now().strftime("%d-%m-%Y"), self.tenant.username)

  def close():
    pass

  def logout(self):
    self.loggedin = 0
    self.loggedin_user = None
    self.admin_is_loggedin = 0 


  def close(self):
    self.userRepository.close()

