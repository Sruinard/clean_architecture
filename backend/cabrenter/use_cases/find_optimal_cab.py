# File containing the usecase for finding the most suitable cab for a user.
from typing import List

from cabrenter.entities.cab import Cab
from cabrenter.use_cases.find_optimal_cab_repo_interface import \
    MostSuitableCabRepoInterface


class FindMostSuitableCabs:
    def __init__(self, repo: MostSuitableCabRepoInterface):
        self.repo = repo
    
    def get(self, city: str, max_price: int) -> List[Cab]:
        suitable_cabs = self.repo.get_suitable_cabs(
                city=city,
                max_price=max_price,
        )
        sorted_cabs = index_optimization_based_on_price(suitable_cabs)
        return sorted_cabs


def index_optimization_based_on_price(suitable_cabs: List[Cab]) -> List[Cab]:
    return sorted(suitable_cabs, key=lambda x: x.hourly_price, reverse=True)
