
from cabrenter.interfaces.database_access_interface import DataAccessInterface, CabDatabaseInterface
from cabrenter.entities.cab import Cab
from typing import List, Dict
import pyodbc


class DataAccessSQL(DataAccessInterface):

    DRIVER = "{ODBC Driver 17 for SQL Server}"

    def __init__(self, server: str, database: str, username: str, password: str, port: int = 1432):
        self.connection_string = f"""DRIVER={self.DRIVER};SERVER={server};PORT={port};DATABASE={database};UID={username};PWD={password}"""
        self.suitable_cabs = []

    def get_city_cabs(self, city: str) -> List[CabDatabaseInterface]:
        cabs = []
        with pyodbc.connect(self.connection_string) as conn:
            with conn.cursor() as cursor:
                cursor.execute(f"SELECT City, IsAvailable FROM dbo.Cabcenter WHERE City = '{city}'")
                row = cursor.fetchone()
                while row:
                    cab_dict = {
                        "city": row[0],
                        "is_available": row[1]
                    }
                    cabs.append(cab_dict)
                    row = cursor.fetchone()
        return cabs 

    def insert_cab(self, cab: Cab) -> Cab:

        with pyodbc.connect(self.connection_string) as conn:
            with conn.cursor() as cursor:
                cursor.execute(f"INSERT INTO Cabcenter (City, IsAvailable) VALUES ('{cab.city}', {int(cab.is_available)});")
                cursor.commit()
        return cab

    def build(self):
        with pyodbc.connect(self.connection_string) as conn:
            with conn.cursor() as cursor:

                if cursor.tables(table='Cabcenter', tableType='TABLE').fetchone():
                    pass
                else:
                    cursor.execute(f"""
                            CREATE TABLE Cabcenter (
                            CabID INT IDENTITY(1,1) PRIMARY KEY,
                            City VARCHAR(255),
                            IsAvailable BIT
                        )"""
                    )
                    cursor.commit()
    
