from Enum.Permission import Permission
from termcolor import colored

class MainView:
  def __init__(self, tenant, loginService, advisorService, userService, clientService):
    self.loginService = loginService
    self.advisorService = advisorService
    self.userService = userService
    self.clientService = clientService
    #self.clientService = clientService
    self.tenant = tenant

  def GetMenu(self):
    view = []
    for permission in Permission:
      if Permission.ViewClient == permission and self.tenant.HasPermission(permission):
        view.append([len(view)+1, 'View all clients', self.clientService.GetAllClients])
      if Permission.ViewClient == permission and self.tenant.HasPermission(permission):
        view.append([len(view)+1, 'Search client', self.clientService.SearchClientInfo])
      if Permission.CreateClient == permission and self.tenant.HasPermission(permission):
        view.append([len(view)+1, 'Add new client', self.clientService.CreateNewClient])
      if Permission.UpdateClientInfo == permission and self.tenant.HasPermission(permission):
        view.append([len(view)+1, 'Update client', self.clientService.UpdateClient])
      if Permission.ManageClient == permission and self.tenant.HasPermission(permission):
        view.append([len(view)+1, 'Delete client', self.clientService.DeleteClientRecord])
      
      if Permission.ViewAllUsers == permission and self.tenant.HasPermission(permission):
        view.append([len(view)+1, 'View all users', self.userService.GetAllUsers])
      
      if Permission.ManageAdvisor == permission and self.tenant.HasPermission(permission):
        view.append([len(view)+1, 'Add new advisor', self.advisorService.CreateAdvisor])
        view.append([len(view)+1, 'Delete advisor', self.advisorService.DeleteAdvisor])
      if Permission.UpdateAdvisorPassword == permission and self.tenant.HasPermission(permission):
        view.append([len(view)+1, 'Update password for advisor', self.advisorService.UpdatePasswordForAdvisor])
    view.append([0, 'Exit', self.loginService.close])

    return view