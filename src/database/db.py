import psycopg2 as postDB
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import asyncio


class DataBase():
    def __init__(self, dbname, host, user, password, port):
        self.dbname = dbname
        self.host = host
        self.user = user
        self.password = password
        self.port = port

        
    async def createconnection(self):
        try:
            self.connection = postDB.connect(dbname=self.dbname, user=self.dbname, password=self.password, host=self.host, port=self.port)
            self.cursor = self.connection.cursor()
            print('____Connection and cursor to DB created____')
        except (Exception, Error):
            self.connection.close()
            self.cursor.close()
            await self.logger.debug(f'____Alert: cant connect to data base with error ____\n {Error}')
    async def closeconnection(self):
        self.cursor.close()
        self.connection.close()
    async def select_data(self, mode:str):
        if self.connection:
            pass
    async def insert_data(self):
        pass
    async def create_table(self):
        pass
    async def update_data(self):
        pass
    async def update_table(self):
        pass


