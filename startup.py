from Repository.ClientRepository import ClientRepository
from Repository.UserRepository import UserRepository
from Repository.LoggingRepository import LoggingRepository
from Service.AdvisorService import AdvisorService
from Service.UserService import UserService
from Service.LoginService import *

class ServiceCollection:
    def __init__(self, dbContext):
        self.dbContext = dbContext

    # In between solution for loading services and repositories to define tenant
    def ConfigureLoginDependencies(self):
        self.UserRepository = UserRepository(self.dbContext)
        self.LoginService = LoginService(self.UserRepository)

    # Called when user is logged in, to load other services when tenant (user) is defined
    def ConfigureServicesOnLogin(self):
        if self.LoginService.tenant is None:
            return
        self.AddRepositories()
        self.AddServices()

    def AddRepositories(self):
        self.ClientRepository = ClientRepository(self.dbContext)
        self.LoggingRepository = LoggingRepository(self.dbContext)
        return

    def AddServices(self):
        self.AdvisorService = AdvisorService(self.LoginService.tenant, self.UserRepository, self.LoggingRepository)
        self.UserService = UserService(self.LoginService.tenant, self.UserRepository)
        return