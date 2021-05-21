from datetime import datetime
from typing import List

from cabrenter.data_structures.response_model import CabResponseModel
from cabrenter.entities.cab import Cab
from cabrenter.interfaces.cab_interface import CabRepoInterface


class CabSelector:
    def __init__(self, repo: CabRepoInterface):
        self.repo = repo
    
    def process_request(self, request_object) -> List[Cab]:
        suitable_cabs = self.repo.get_suitable_cabs(filters=request_object.filters)
        cabs = []
        for cab in suitable_cabs:
            cab_data = CabResponseModel(
                city=cab.city, 
                is_available=cab.is_available, 
                datetime=datetime.now().strftime("%H:%M:%S")
            )
            cabs.append(cab_data)     
        return cabs
        