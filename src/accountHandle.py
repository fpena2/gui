import sqlite3
import os

def initSQLpath():
    dataBaseName = "userBase.db"  
    path = os.path.join(os.path.dirname(os.getcwd()), "storage")
    if not os.path.exists(path):
        os.makedirs(path)
    return os.path.join(path, dataBaseName)


class createUser():
    def __init__(self, parent = None):
        self.dataBase = initSQLpath()
        self.connection = None
        self.openConnection()
    
    def openConnection(self):
        try:
            self.connection = sqlite3.connect(self.dataBase)
        except Error as exception:
            print(exception)

    def closeConncection(self):
        self.connection.commit()
        self.connection.close()
    
    def pushDatabase(self, dataPacket):
        userID, password, organization = dataPacket

        # cursor = self.connection.cursor()
        # cursor.execute("SELECT count(*) FROM sqlite_master WHERE type='table' AND name='{UserBase}';")
        # index = cursor.fetchall()[0][0]

        # print(index)
        # if index == 0:
        #     self.connection.execute(
        #         """CREATE TABLE UserBase (
        #             Name TEXT PRIMARY KEY NOT NULL, 
        #             Password TEXT NOT NULL,
        #             Organization TEXT NOT NULL
        #         );"""
        #     )
        # else:
        #     print("table present")



    def accessDatabase(self, passToSearch):
        pass 