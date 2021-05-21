from typing import List

class CabDatabaseInterface:
    city: str
    is_available: bool

class DataAccessInterface:

    def get_city_cabs(self, city: str) -> List[CabDatabaseInterface]:
        raise NotImplementedError()