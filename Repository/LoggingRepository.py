import sqlite3
from datetime import datetime as dt
from Domain.UserLogAggregate import UserLogAggregate
from Helper.EncryptionHelper import EncryptionHelper
from Record.LogRecord import LogRecord

class LoggingRepository:
    def __init__ (self, db):
        self.dbContext = db

    def GetAllLogs(self):
        sql_statement = f"SELECT * FROM logging ORDER BY date DESC, time"
        self.dbContext.cur.execute(sql_statement)
        logRecords = self.dbContext.cur.fetchall()

        allLogs = []
        for logRecord in logRecords:
            logRecord = LogRecord(logRecord)
            allLogs.append(logRecord.ToLogDomain())

        return allLogs 

    def CreateLog(self, username, description_of_activity, additional_info, suspicious):
        today =  dt.now()
        date = today.strftime("%d-%m-%Y")
        time = today.strftime("%H:%M:%S")
        
        encryptedValues = EncryptionHelper.GetEncryptedTuple((username, date, time, description_of_activity, additional_info, suspicious))
        sql_statement = '''INSERT INTO logging (username, date, time, description_of_activity, additional_info, supicious) VALUES (?,?,?,?,?,?)'''
        self.dbContext.cur.execute(sql_statement, encryptedValues)
        self.dbContext.conn.commit()