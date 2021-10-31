from Enum.Permission import Permission
from Helper.EncryptionHelper import EncryptionHelper
from Record.PermissionRecord import PermissionRecord

class PermissionRepository:
    def __init__ (self, db):
        self.dbContext = db

    def GetAllPermissionsForAdvisor(self):
        queryParameters = EncryptionHelper.GetEncryptedTuple(('1',))
        sql_statement = f"SELECT * FROM permission WHERE advisor = ?"
        permissionTuples = self.dbContext.executeAndFetchAll(sql_statement, queryParameters)

        return self.GetPermissions(permissionTuples) 

    def GetAllPermissionsForSysAdmin(self):
        queryParameters = EncryptionHelper.GetEncryptedTuple(('1',))
        sql_statement = f"SELECT * FROM permission WHERE sysadmin =?"
        permissionTuples = self.dbContext.executeAndFetchAll(sql_statement, queryParameters)

        return self.GetPermissions(permissionTuples) 
    
    def GetAllPermissionsForSuperAdmin(self):
        queryParameters = EncryptionHelper.GetEncryptedTuple(('1',))
        sql_statement = f"SELECT * FROM permission WHERE superadmin = ?"
        permissionTuples = self.dbContext.executeAndFetchAll(sql_statement, queryParameters)

        return self.GetPermissions(permissionTuples) 

    def GetPermissions(self, permissionTuples):
        permissions = []
        for permissionTuple in permissionTuples:
            permissionRecord = PermissionRecord(permissionTuple)
            permissions.append(Permission(int(permissionRecord.permissionEnum)))
        return permissions
