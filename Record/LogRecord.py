from Helper.EncryptionHelper import EncryptionHelper


class LogRecord:

    def __init__(self, encryptedLogTuple):
        logTuple = EncryptionHelper.GetDecryptedTuple(encryptedLogTuple)
        self.username = 
        self.date =
        self.time
        self.descriptionActi

