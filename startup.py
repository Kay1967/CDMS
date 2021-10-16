from Repository.ClientRepository import ClientRepository
from Repository import UserRepository, ClientRepository
from Service.LoginService import *

class ServiceCollection:
    def __init__(self, dbContext):
        self.dbContext = dbContext

    def ConfigureServices(self):
        self.AddRepositories()
        self.AddServices()

    def AddRepositories(self):
        self.ClientRepository = ClientRepository(self.dbContext)
        self.UserRepository = UserRepository(self.dbContext)
        return

    def AddServices(self):
        self.LoginService = LoginService(self.UserRepository)
        return