from typing import List

import pymongo
from bson.objectid import ObjectId
from cabrenter.entities.cab import Cab
from cabrenter.use_cases.driver_workspace_repo_interface import DriverWorkspaceRepoInterface

class DriverWorkspaceCosmos(DriverWorkspaceRepoInterface):
    DATABASE_NAME = "cabcenter"
    COLLECTION = "cabs"

    def __init__(self, connection_string: str, port: int = 27016):
        self.client = pymongo.MongoClient(connection_string, port=port) 


    def add_cab(self, cab: Cab, driver_id: int) -> List[Cab]:
        cabs_collection = self.client[self.DATABASE_NAME][self.COLLECTION] 

        _ = cabs_collection.insert_one({
            "city": cab.city,
            "brand": cab.brand,
            "hourly_price": cab.hourly_price,
            "is_available": True,
            "driver_id": driver_id
        })
        return cab

    def get_cabs(self, driver_id: int) -> List[Cab]:
        cabs_collection = self.client[self.DATABASE_NAME][self.COLLECTION] 
        cabs = cabs_collection.find({
            "driver_id": {
                "$eq": driver_id
            }
        })
        return [Cab(city=cab.get("city"), brand=cab.get("brand"), hourly_price=cab.get("hourly_price"), id=str(cab.get("_id"))) for cab in cabs]

    def get_cab(self, driver_id: int, cab_id: int) -> List[Cab]:
        cabs_collection = self.client[self.DATABASE_NAME][self.COLLECTION] 
        cab = cabs_collection.find_one({
            "driver_id": {
                "$eq": driver_id
            },
            "_id": {
                "$eq": ObjectId(cab_id)
            }

        })
        return [Cab(city=cab.get("city"), brand=cab.get("brand"), hourly_price=cab.get("hourly_price"), id=str(cab.get("_id")))]

