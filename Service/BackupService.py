import pathlib
import shutil
from datetime import datetime as dt
import os
from zipfile import ZipFile

from Enum.Permission import Permission 


class BackUpService:
    def __init__(self, tenant, loggingRepository):
        self.tenant = tenant
        self.databasePath = (os.getcwd() + "\mycompany.db").replace("\\", "/")
        self.backupPath = (os.getcwd() + "\Backup\\").replace("\\", "/")
        self.loggingRepository = loggingRepository
    
    def CreateBackup(self):
        if not self.tenant.HasPermission(Permission.ManageBackup):
          print("Unauthorized")
          return

        dateOfBackup = dt.today().strftime('%d-%m-%Y-%H-%M')
        zipObj = ZipFile(f"Backup/{dateOfBackup}.zip", 'w')
        zipObj.write('mycompany.db')
        zipObj.close()

        self.loggingRepository.CreateLog(self.tenant.username, f"Created backup {dateOfBackup}", "Success", 0)
        print(f"Backup:{dateOfBackup} created")
