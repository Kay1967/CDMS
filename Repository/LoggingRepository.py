import sqlite3
from datetime import datetime as dt
from Helper.EncryptionHelper import EncryptionHelper

class LoggingRepository:
    def __init__ (self, db):
        self.dbContext = db

    def GetAllLogs(self):
        sql_statement = '''INSERT INTO logging (username, date, time, description_of_activity, additional_info, supicious) VALUES (?,?,?,?,?,?)'''
        encryptedValues = EncryptionHelper.GetDecryptedString((username, date, time, description_of_activity, additional_info, suspicious))
        sql_statement = '''INSERT INTO logging (username, date, time, description_of_activity, additional_info, supicious) VALUES (?,?,?,?,?,?)'''
        self.dbContext.cur.execute(sql_statement, encryptedValues)
        self.dbContext.conn.commit()

    def CreateLog(self, username, description_of_activity, additional_info, suspicious):
        today =  dt.now()
        date = today.strftime("%d-%m-%Y")
        time = today.strftime("%H:%M:%S")
        
        encryptedValues = EncryptionHelper.GetEncryptedTuple((username, date, time, description_of_activity, additional_info, suspicious))
        sql_statement = '''INSERT INTO logging (username, date, time, description_of_activity, additional_info, supicious) VALUES (?,?,?,?,?,?)'''
        self.dbContext.cur.execute(sql_statement, encryptedValues)
        self.dbContext.conn.commit()