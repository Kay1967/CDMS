from Enum.Permission import Permission
from termcolor import colored

class MainView:
  def __init__(self, tenant, loginService, advisorService, userService):
    self.loginService = loginService
    self.advisorService = advisorService
    self.userService = userService
    self.tenant = tenant

  def GetMenu(self):
    view = []
    for permission in Permission:
      if Permission.UpdateAdvisorPassword == permission and self.tenant.HasPermission(permission):
        view.append([len(view)+1, 'Update password for advisor', self.advisorService.UpdatePasswordForAdvisor])
      if Permission.ViewAllUsers == permission and self.tenant.HasPermission(permission):
        view.append([len(view)+1, 'View all users', self.userService.GetAllUsers])
      if Permission.ManageAdvisor == permission and self.tenant.HasPermission(permission):
        # Add advisor
        view.append([len(view)+1, 'Delete advisor', self.advisorService.DeleteAdvisor])

    view.append([0, 'Exit', self.loginService.close])

    return view