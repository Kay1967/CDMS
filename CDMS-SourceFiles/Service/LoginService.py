from datetime import datetime as dt
from Component.UserInterface import *
from Domain.Advisor import Advisor
from Domain.SuperAdmin import SuperAdmin
from Domain.SysAdmin import SysAdmin
from Domain.User import User

class LoginService:
  loggedin = False
  def __init__ (self, userRepository, loggingRepository, permissionRepository):
    self.userRepository = userRepository
    self.loggingRepository = loggingRepository
    self.permissionRepository = permissionRepository

  def login(self):
    username = input("please enter username: ")
    password = input("please enter password: ")

    try:
      user = self.userRepository.GetUser(username, True)
      if user == None or user.password != password:  # An empty result evaluates to False.
          raise ValueError(f"Login Try with: Username: {username} {password} ", False)
      else:
          self.loggedin = True
          self.tenant = user
          self.setPermissions()
          self.userRepository.UpdateLastLogin(dt.now(), self.tenant.username)
    except ValueError as error: self.CreateLogFromException(self.login.__name__, error); return

  def setPermissions(self):
    if type(self.tenant) is Advisor:
        self.tenant.hasPermissions = self.permissionRepository.GetAllPermissionsForAdvisor()
    if type(self.tenant) is SysAdmin:
        self.tenant.hasPermissions = self.permissionRepository.GetAllPermissionsForSysAdmin()
    if type(self.tenant) is SuperAdmin:
        self.tenant.hasPermissions = self.permissionRepository.GetAllPermissionsForSuperAdmin()

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
      print("Login failed")
    self.loggingRepository.CreateLog("Anonymous", descriptionOfActivity, f"ValueError:{exception.args[0]}", "1")
