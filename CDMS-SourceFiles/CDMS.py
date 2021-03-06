from Service.LogService import LogService
from startup import ServiceCollection
from Component.UserInterface import UserInterfaceComponent
from DbContext.database import * 
from View.MainView import MainView
from View.LoginView import LoginView
import sqlite3
from termcolor import colored

loginHeading = '''
██████████████████████████████████████████████
█                                            █
█                 MY COMPANY                 █
█                 ----------                 █
█             Administration System          █
█                                            █
██████████████████████████████████████████████


Main Menu'''

def CreateMainMenuHeader(tenantName, tenantTypeName):
    nameAndSpaces =  tenantName + "" * (19 - len(tenantName))
    userTypeAndSpaces = tenantTypeName + "" * (19 - len(tenantTypeName))

    return '''
Welcome
██████████████████████████████████████████████
█                                            █
█    Username:          {0}                  █
█                                            █
█    User type:         {1}                  █
█                                            █
██████████████████████████████████████████████
User Menu'''.format(nameAndSpaces, userTypeAndSpaces)

# GLobal Variables
# --------------------------------------------------------------------
max_input_try = 3
company_db_name = 'mycompany.db'
client_tb_name = 'client'
users_tb_name = 'users'
#---------------------------------------------------------------------
dbContext = db(company_db_name, client_tb_name, users_tb_name)
serviceCollection = ServiceCollection(dbContext)
serviceCollection.ConfigureLoginDependencies()
#-----------------------------------------------------------------------

# View calls Service, and Service calls Repository and Repository reflects always the data layer (database)

if __name__ == "__main__":
    loginView = LoginView(serviceCollection.LoginService)
    loginInterface = UserInterfaceComponent(loginView, True, loginHeading)
    loginInterface.run()
    
    if serviceCollection.LoginService.loggedin:
        serviceCollection.ConfigureServicesOnLogin()
        mainView = MainView(serviceCollection.LoginService.tenant, 
                            serviceCollection.LoginService, 
                            serviceCollection.AdvisorService, 
                            serviceCollection.UserService, 
                            serviceCollection.ClientService, 
                            serviceCollection.SysAdminService,
                            serviceCollection.LogService,
                            serviceCollection.BackupService)
        mainHeading = CreateMainMenuHeader(serviceCollection.LoginService.tenant.fullname, type(serviceCollection.LoginService.tenant).__name__)
        mainInterface = UserInterfaceComponent(mainView, False, mainHeading)
        mainInterface.run()
        dbContext.conn.close()