from typing import List
from cabrenter.entities.cab import Cab

class CabDatabaseInterface:
    city: str
    is_available: bool

class DataAccessInterface:

    def get_city_cabs(self, city: str) -> List[CabDatabaseInterface]:
        raise NotImplementedError()

    def insert_cab(self, cab: Cab) -> Cab:
        raise NotImplementedError()