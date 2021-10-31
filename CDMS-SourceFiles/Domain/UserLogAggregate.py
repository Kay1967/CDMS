import datetime 

class UserLogAggregate:
    countUnseenSuspiciousActivity = 0
    def __init__(self, listLogs, userLastLogin):
        self.logs = listLogs
        self.userLastLogin = userLastLogin
        for log in self.logs:
            if log.suspicious == True and self.userLastLogin.date() < datetime.date.today():
                self.countUnseenSuspiciousActivity = self.countUnseenSuspiciousActivity + 1

class Log:
    def __init__(self, username, date, time, descriptionOfActivity, additionalInfo, suspicious):
        self.username = username
        self.date = date
        self.time = time
        self.descriptionOfActivity = descriptionOfActivity 
        self.additionalInfo = additionalInfo
        self.suspicious = bool(suspicious)
