from enum import Enum

class Permission(Enum):
    UpdateAdvisorPassword = 1
    ViewAllUsers = 2
    ManageAdvisor = 3
    UpdateSysAdminPassword = 4
    ManageSysAdmin = 5
    