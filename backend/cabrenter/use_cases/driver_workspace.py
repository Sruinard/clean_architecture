from typing import List

from cabrenter.entities.cab import Cab
from cabrenter.use_cases.driver_workspace_repo_interface import DriverWorkspaceRepoInterface

class DriverWorkspace:
    def __init__(self, repo: DriverWorkspaceRepoInterface):
        self.repo = repo

    def get_cab(self, driver_id, cab_id) -> List[Cab]:
        cab = self.repo.get_cab(
            driver_id=driver_id,
            cab_id=cab_id
        )
        return cab

    def get_cabs(self, driver_id) -> List[Cab]:
        cab = self.repo.get_cabs(
            driver_id=driver_id,
        )
        return cab

    def add_cab(self, driver_id, city, brand, hourly_price):
        cab = self.repo.add_cab(
            cab=Cab(
                city=city,
                brand=brand,
                hourly_price=hourly_price,
            ),
            driver_id=driver_id
        )
        return cab

