from cabrenter.interfaces.cab_interface import CabRepoInterface
from cabrenter.entities.cab import Cab
from typing import List
import pymongo

class CabRepository(CabRepoInterface):

    DATABASE_NAME = "cabcenter"
    COLLECTION = "cabs"

    def __init__(self, connection_string: str, port: int = 27016):
        self.client = pymongo.MongoClient(connection_string, port=port) 
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
        cabs_collection = self.client[self.DATABASE_NAME][self.COLLECTION] 
        cabs = cabs_collection.find({})
        print(cabs)
        for cab in cabs:
            cab = Cab.from_dict(cab)
            if CabRepository.is_available_cab(cab) and CabRepository.is_in_city_cab(cab, filters.get("city", "")):
                self.suitable_cabs.append(cab)
        return self.suitable_cabs 
        
    
