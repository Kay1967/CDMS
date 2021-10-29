class UserLogAggregate:
    hasUnseenSuspiciousActivity = False
    def __init__(self, listLogs, userLastLogin):
        self.logs = listLogs
        self.userLastLogin = userLastLogin
        for log in self.logs:
            if log.suspicious == True:
                self.hasUnseenSuspiciousActivity = True

class Log:
    def __init__(self, username, date, time, descriptionOfActivity, additionalInfo, suspicious):
        self.username = username
        self.date = date
        self.time = time
        self.descriptionOfActivity = descriptionOfActivity 
        self.additionalInfo = additionalInfo
        self.suspicious = suspicious
