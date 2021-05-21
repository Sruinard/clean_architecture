from cabrenter.entities.cab import Cab
from typing import List


class CabRepoInterface:

    @staticmethod
    def is_available_cab(cab: Cab) -> bool:
        pass

    @staticmethod
    def is_in_city_cab(cab: Cab, city: str) -> bool:
        pass

    def get_suitable_cabs(self, filters) -> List[Cab]:
        pass