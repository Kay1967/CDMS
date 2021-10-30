from Domain.UserLogAggregate import UserLogAggregate
from Enum.Permission import Permission

class LogService:
    def __init__(self, tenant, logRepository):
        self.logRepository =  logRepository
        self.tenant = tenant

    def ViewAllLogs(self):
        if not self.tenant.HasPermission(Permission.ManageLog):
          print("Unauthorized")
          return

        userLogAggregate = self.GetUserLogAggregate()
        if userLogAggregate.countUnseenSuspiciousActivity > 0:
          print(f"\n!!!! {userLogAggregate.countUnseenSuspiciousActivity} suspicous activities logged after your last login ({userLogAggregate.userLastLogin})\n") 

        for log in userLogAggregate.logs:
            print(f"Done by: {log.username} \n" +
            f"Date: {log.date} \n" +
            f"Time: {log.time}\n" +
            f"Description Of Activity: {log.descriptionOfActivity} \n" +
            f"Additional Info: {log.additionalInfo} \n" +
            f"Suspicious: {log.suspicious} \n" +
            f"--------------------------------------------------------")

    def GetUserLogAggregate(self):
        logs = self.logRepository.GetAllLogs()
        return UserLogAggregate(logs, self.tenant.lastLogin)