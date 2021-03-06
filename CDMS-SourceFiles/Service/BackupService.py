from datetime import datetime as dt
from zipfile import ZipFile

from Enum.Permission import Permission 


class BackUpService:
    def __init__(self, tenant, loggingRepository):
        self.tenant = tenant
        self.loggingRepository = loggingRepository
    
    def CreateBackup(self):
        if not self.tenant.HasPermission(Permission.ManageBackup):
          print("Unauthorized")
          self.loggingRepository.CreateLog(self.tenant.username, f"{self.CreateBackup.__name__}", "Unauthorized", 1)
          return

        dateOfBackup = dt.today().strftime('%d-%m-%Y-%H-%M')
        zipObj = ZipFile(f"Backup/{dateOfBackup}.zip", 'w')
        zipObj.write('mycompany.db')
        zipObj.close()

        self.loggingRepository.CreateLog(self.tenant.username, f"Created backup {dateOfBackup}", "Success", 0)
        print(f"Backup:{dateOfBackup} created")
