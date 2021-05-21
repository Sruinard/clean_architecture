from typing import List

from cabrenter.entities.cab import Cab
from cabrenter.interfaces.cab_interface import CabRepoInterface
from cabrenter.interfaces.database_access_interface import DataAccessInterface


class CabRepository(CabRepoInterface):

    DATABASE_NAME = "cabcenter"
    COLLECTION = "cabs"

    def __init__(self, database_access: DataAccessInterface):
        self.database_access = database_access
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
        city_cabs = self.database_access.get_city_cabs(city=filters.get("city"))
        for cab in city_cabs:
            cab = Cab.from_dict(cab)
            if CabRepository.is_available_cab(cab):
                self.suitable_cabs.append(cab)
        return self.suitable_cabs 
