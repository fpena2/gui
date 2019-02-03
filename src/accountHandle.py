import sqlite3
from pathlib import Path
import os

def initSQLpath():
    dataBaseName = "userBase.db"  
    path = os.path.join(os.path.dirname(os.getcwd()), "storage")
    if not os.path.exists(path):
        os.makedirs(path)
    return os.path.join(path, dataBaseName)


class userTools():
    def __init__(self, parent = None):
        self.dataBase = initSQLpath()
        self.connection = None
    
    def openConnection(self):
        try:
            self.connection = sqlite3.connect(self.dataBase)
        except Error as exception:
            print(exception)
    
    def createTable(self):
        self.connection.execute(
            """CREATE TABLE UserBase (Name TEXT, Password TEXT, Organization TEXT);"""
            )

    def closeConncection(self):
        self.connection.commit()
        self.connection.close()


    def pushNewUser(self, dataPacket):
        self.openConnection()

        try:
            dbAbsPath = Path(self.dataBase).resolve(strict=True)
        except FileNotFoundError:
            self.openConnection()
            self.createTable()
        
        cursor = self.connection.cursor() 
        for row in cursor.execute('SELECT Name FROM UserBase'):
            if dataPacket[0] in row : 
                #print("User is already registered")
                return 0 

        sqlEntry = """INSERT INTO UserBase VALUES (?, ?, ?)"""
        cursor.execute(sqlEntry, dataPacket)
        self.closeConncection()


    def loginUser(self, logInfo):
        self.openConnection()
        cursor = self.connection.cursor() 
        for row in cursor.execute('SELECT * FROM UserBase'):
            if (logInfo[0] in row) and (logInfo[1] == row[1]):
                return 1

                

if __name__ == '__main__':
    c = userTools()
    val = ("Mono", "444", "br")
    c.pushNewUser(val)