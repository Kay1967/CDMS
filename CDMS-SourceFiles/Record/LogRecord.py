from Domain.UserLogAggregate import Log
from Helper.EncryptionHelper import EncryptionHelper


class LogRecord:

    def __init__(self, encryptedLogTuple):
        logTuple = EncryptionHelper.GetDecryptedTuple(encryptedLogTuple)
        self.username = logTuple[0] 
        self.date = logTuple[1]
        self.time = logTuple[2]
        self.description_of_activity = logTuple[3]
        self.additional_info = logTuple[4]
        self.suspicious = logTuple[5] == "1"

    def ToLogDomain(self):
        return Log(self.username, self.date, self.time, self.description_of_activity, self.additional_info, self.suspicious)
