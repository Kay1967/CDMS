from Domain.User import User
from Repository.ClientRepository import ClientRepository
from Repository.PermissionRepository import PermissionRepository
from Repository.UserRepository import UserRepository
from Repository.LoggingRepository import LoggingRepository
from Service.BackupService import BackUpService
from Service.ClientService import *
from Service.AdvisorService import AdvisorService
from Service.LogService import LogService
from Service.SysAdminService import SysAdminService
from Service.UserService import UserService
from Service.LoginService import *

class ServiceCollection:
    def __init__(self, dbContext):
        self.dbContext = dbContext

    # In between solution for loading services and repositories to define tenant
    def ConfigureLoginDependencies(self):
        self.LoggingRepository = LoggingRepository(self.dbContext)
        self.PermissionRepository = PermissionRepository(self.dbContext)
        self.UserRepository = UserRepository(self.dbContext, self.LoggingRepository)
        self.LoginService = LoginService(self.UserRepository, self.LoggingRepository, self.PermissionRepository)

    # Called when user is logged in, to reload other services when tenant (user) is defined
    def ConfigureServicesOnLogin(self):
        if not self.LoginService.loggedin:
            return
        self.AddRepositories()
        self.AddServices()

    def AddRepositories(self):
        self.LoggingRepository = LoggingRepository(self.dbContext, self.LoginService.tenant)
        self.UserRepository = UserRepository(self.dbContext, self.LoggingRepository, self.LoginService.tenant)
        self.ClientRepository = ClientRepository(self.dbContext, self.LoggingRepository, self.LoginService.tenant)
        return

    def AddServices(self):
        self.AdvisorService = AdvisorService(self.LoginService.tenant, self.UserRepository, self.LoggingRepository, self.ClientRepository)
        self.UserService = UserService(self.LoginService.tenant, self.UserRepository, self.LoggingRepository)
        self.ClientService = ClientService(self.LoginService.tenant, self.ClientRepository, self.LoggingRepository)
        self.SysAdminService = SysAdminService(self.LoginService.tenant, self.UserRepository, self.LoggingRepository)
        self.LogService = LogService(self.LoginService.tenant, self.LoggingRepository)
        self.BackupService = BackUpService(self.LoginService.tenant, self.LoggingRepository)
        return