from cabrenter.interfaces.database_access_interface import DataAccessInterface, CabDatabaseInterface
from cabrenter.entities.cab import Cab
from typing import List
import pymongo

class DataAccessCosmos(DataAccessInterface):

    DATABASE_NAME = "cabcenter"
    COLLECTION = "cabs"

    def __init__(self, connection_string: str, port: int = 27016):
        self.client = pymongo.MongoClient(connection_string, port=port) 

    def get_city_cabs(self, city: str) -> List[CabDatabaseInterface]:
        cabs_collection = self.client[self.DATABASE_NAME][self.COLLECTION] 
        cabs = cabs_collection.find({
            "city": {
                "$eq": city
            }
        })
        return cabs
    
    def insert_cab(self, cab: Cab) -> Cab:
        cabs_collection = self.client[self.DATABASE_NAME][self.COLLECTION] 
        cabs_collection.insert_one(
            {
                "city": cab.city,
                "is_available": cab.is_available
            }
        )
        return cab
        
    
