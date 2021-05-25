from datetime import datetime
from typing import List
import json

from cabrenter.data_structures.response_model import CabResponseModel
from cabrenter.entities.cab import Cab
from cabrenter.interfaces.cab_interface import CabRepoInterface


class CabSelector:
    def __init__(self, repo: CabRepoInterface):
        self.repo = repo
    
    def get(self, request_object) -> List[Cab]:
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
    
    def post(self, request_object) -> Cab:
        cab_data = json.loads(request_object.json())
        cab = self.repo.post(
            city=cab_data.get("city"), 
            is_available=cab_data.get("is_available")
        )
        return CabResponseModel(
            city=cab.city,
            is_available=cab.is_available,
            datetime=datetime.now().strftime("%H:%M:%S")
        )

        