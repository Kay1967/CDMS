from enum import Enum

# Permissions with Manage are the highest rights 
class Permission(Enum):
    ViewAllUsers = 101
    
    ManageAdvisor = 2
    UpdateAdvisorPassword = 201
    
    ManageSysAdmin = 3
    UpdateSysAdminPassword = 301

    ManageClient = 4
    ViewClient = 401
    CreateClient = 402
    UpdateClientInfo = 402

    ManageLog = 5

    ManageBackup = 6