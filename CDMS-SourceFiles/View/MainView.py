from Enum.Permission import Permission

class MainView:
  def __init__(self, tenant, loginService, advisorService, userService, clientService, sysAdminService, logService, backupService):
    self.loginService = loginService
    self.advisorService = advisorService
    self.userService = userService
    self.clientService = clientService
    self.sysAdminService = sysAdminService
    self.logService = logService
    self.backupService = backupService
    self.tenant = tenant

  def GetMenu(self):
    view = []
    for permission in Permission:
      if Permission.ViewClient == permission and self.tenant.HasPermission(permission):
        view.append([len(view)+1, 'View all clients', self.clientService.GetAllClients])
        view.append([len(view)+1, 'Search client', self.clientService.ViewAndGetClientInfo])
      if Permission.CreateClient == permission and self.tenant.HasPermission(permission):
        view.append([len(view)+1, 'Add new client', self.clientService.CreateNewClient])
      if Permission.UpdateClientInfo == permission and self.tenant.HasPermission(permission):
        view.append([len(view)+1, 'Update client', self.clientService.UpdateClientInfo])
      if Permission.ManageClient == permission and self.tenant.HasPermission(permission):
        view.append([len(view)+1, 'Delete client', self.clientService.DeleteClientRecord])
      
      if Permission.ViewAllUsers == permission and self.tenant.HasPermission(permission):
        view.append([len(view)+1, 'View all users', self.userService.GetAllUsers])
      
      if Permission.ManageAdvisor == permission and self.tenant.HasPermission(permission):
        view.append([len(view) + 1, 'Add new advisor', self.advisorService.CreateAdvisor])
        view.append([len(view) + 1, 'Update advisor', self.advisorService.UpdateAdvisor])
        view.append([len(view)+1, 'Delete advisor', self.advisorService.DeleteAdvisor])
      if Permission.UpdateAdvisorPassword == permission and self.tenant.HasPermission(permission):
        view.append([len(view)+1, 'Update password for advisor', self.advisorService.UpdatePasswordForAdvisor])

      if Permission.ManageSysAdmin == permission and self.tenant.HasPermission(permission):
        view.append([len(view) + 1, 'Add new admin', self.sysAdminService.CreateSysAdmin])
        view.append([len(view) + 1, 'Update admin', self.sysAdminService.UpdateSysAdmin])
        view.append([len(view)+1, 'Delete admin', self.sysAdminService.DeleteSysAdmin])
      if Permission.UpdateSysAdminPassword == permission and self.tenant.HasPermission(permission):
        view.append([len(view)+1, 'Update password for admin', self.sysAdminService.UpdatePasswordForSysAdmin])

      if Permission.ManageBackup == permission and self.tenant.HasPermission(permission):
        view.append([len(view)+1, 'Create backup', self.backupService.CreateBackup])

      if Permission.ManageLog ==  permission and self.tenant.HasPermission(permission):
        view.append([len(view)+1, 'View all Logs', self.logService.ViewAllLogs])
        userLogAggregate = self.logService.GetUserLogAggregate()
        if userLogAggregate.countUnseenSuspiciousActivity > 0:
          print(f"\n!!!! {userLogAggregate.countUnseenSuspiciousActivity} suspicous activities logged after your last login ({userLogAggregate.userLastLogin})\n") 


    view.append([0, 'Exit', self.loginService.close])

    return view