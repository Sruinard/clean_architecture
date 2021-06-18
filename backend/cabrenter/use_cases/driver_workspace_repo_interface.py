from typing import List
from cabrenter.entities.cab import Cab

class DriverWorkspaceRepoInterface:

    def get_cab(self, driver_id, cab_id) -> List[Cab]:
        raise NotImplementedError()

    def get_cabs(self, driver_id) -> List[Cab]:
        raise NotImplementedError()

    def add_cab(self, cab: Cab, driver_id: int) -> List[Cab]:
        raise NotImplementedError()
