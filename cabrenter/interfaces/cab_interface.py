from cabrenter.entities.cab import Cab
from typing import List


class CabRepoInterface:

    @classmethod
    def is_available_cab(cab: Cab) -> bool:
        pass

    @classmethod
    def is_in_city_cab(cab: Cab, city: str) -> bool:
        pass

    @classmethod    
    def get_suitable_cabs(self, filters) -> List[Cab]:
        pass