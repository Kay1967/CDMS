from Helper.EncryptionHelper import EncryptionHelper
from Domain.Advisor import Advisor
from Domain.SysAdmin import SysAdmin

class UserRecord:
    def __init__(self, encryptedUserTuple):
        userTuple = EncryptionHelper.GetDecryptedTuple(encryptedUserTuple)

        self.username = userTuple[0]
        self.password= userTuple[1]
        self.fullname = userTuple[2]
        self.admin = userTuple[3]
        self.last_login = userTuple[4]

    def ToUserDomain(self):
        isAdmin = self.admin == "1" 
        if isAdmin:
            return SysAdmin(self.username, self.password, self.fullname, isAdmin, self.last_login)
        return Advisor(self.username, self.password, self.fullname, isAdmin, self.last_login)
    