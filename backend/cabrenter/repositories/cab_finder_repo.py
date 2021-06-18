import pymongo
from cabrenter.entities.cab import Cab
from cabrenter.use_cases.find_optimal_cab_repo_interface import MostSuitableCabRepoInterface


class MostSuitableCabCosmos(MostSuitableCabRepoInterface):
    DATABASE_NAME = "cabcenter"
    COLLECTION = "cabs"

    def __init__(self, connection_string: str, port: int = 27016):
        self.client = pymongo.MongoClient(connection_string, port=port) 

    def get_suitable_cabs(self, city, max_price):
        cabs_collection = self.client[self.DATABASE_NAME][self.COLLECTION] 
        cabs = cabs_collection.find({
            "city": {
                "$eq": city
            },
            "hourly_price": {
                "$lte": max_price
            }

        })
        return [Cab(city=cab.get("city"), brand=cab.get("brand"), hourly_price=cab.get("hourly_price"), id=str(cab.get("_id"))) for cab in cabs]
