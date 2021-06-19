# File defining the interface for the most suitable cab repository.
from typing import List

from cabrenter.entities.cab import Cab


class MostSuitableCabRepoInterface():
    def get_suitable_cabs(self, city: str, max_price: int) -> List[Cab]:
        raise NotImplementedError()
