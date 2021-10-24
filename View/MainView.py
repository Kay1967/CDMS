from Enum.Permission import Permission
from termcolor import colored

class MainView:
  def __init__(self, tenant, loginService, advisorService, userService):
    self.loginService = loginService
    self.advisorService = advisorService
    self.userService = userService
    #self.clientService = clientService
    self.tenant = tenant

  def GetMenu(self):
    view = []
    for permission in Permission:
      if Permission.UpdateAdvisorPassword == permission and self.tenant.HasPermission(permission):
        view.append([len(view)+1, 'Update password for advisor', self.advisorService.UpdatePasswordForAdvisor])
      if Permission.ViewAllUsers == permission and self.tenant.HasPermission(permission):
        view.append([len(view)+1, 'View all users', self.userService.GetAllUsers])
      if Permission.ManageAdvisor == permission and self.tenant.HasPermission(permission):
        view.append([len(view)+1, 'Delete advisor', self.advisorService.DeleteAdvisor])
       # Add advisor
      if Permission.ManageAdvisor == permission and self.tenant.HasPermission(permission):
        view.append([len(view)+1, 'Add new advisor', self.advisorService.CreateAdvisor])
      if Permission.ManageClient == permission and self.tenant.HasPermission(permission):
        view.append([len(view)+1, 'Add new client', self.advisorService.CreateNewClient])
      if Permission.ManageClient == permission and self.tenant.HasPermission(permission):
        view.append([len(view)+1, 'Search client', self.advisorService.SearchClientInfo])
      # if Permission.UpdateClientInfo == permission and self.tenant.HasPermission(permission):
      #   view.append([len(view)+1, 'Update client', self.advisorService.UpdateClientInfo])
      if Permission.DeleteClient == permission and self.tenant.HasPermission(permission):
        view.append([len(view)+1, 'Delete client', self.advisorService.DeleteClientRecord])
    view.append([0, 'Exit', self.loginService.close])

    return view