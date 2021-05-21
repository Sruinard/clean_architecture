from cabrenter.interfaces.cab_interface import CabRepoInterface
from cabrenter.entities.cab import Cab
from typing import List
import pyodbc


class CabRepositorySQL(CabRepoInterface):
    DRIVER = "{ODBC Driver 17 for SQL Server}"

    def __init__(self, server: str, database: str, username: str, password: str, port: int = 1432):
        self.connection_string = f"""DRIVER={self.DRIVER};SERVER={server};PORT={port};DATABASE={database};UID={username};PWD={password}"""
        self.suitable_cabs = []


    @staticmethod
    def is_available_cab(cab: Cab) -> bool:
        return cab.is_available

    @staticmethod
    def is_in_city_cab(cab: Cab, city: str) -> bool:
        is_in_city = False
        if cab.city.lower() == city.lower():
            is_in_city = True
        return is_in_city

        
    def get_suitable_cabs(self, filters) -> List[Cab]:
        with pyodbc.connect(self.connection_string) as conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT City, IsAvailable FROM dbo.Cabcenter")
                row = cursor.fetchone()
                while row:
                    cab = Cab.from_dict({
                        "city": row[0],
                        "is_available": row[1]
                    })
                    if CabRepositorySQL.is_available_cab(cab) and CabRepositorySQL.is_in_city_cab(cab, filters.get("city", "")):
                        self.suitable_cabs.append(cab)
                    row = cursor.fetchone()
        return self.suitable_cabs 
        
    
