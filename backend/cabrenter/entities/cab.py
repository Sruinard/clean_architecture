import abc
from typing import Dict

class Cab:

    def __init__(self, city: str, is_available: bool = True) -> None:
        self.city = city
        self.is_available = is_available
    
    @classmethod
    def from_dict(cls, cab_dict: Dict):
        cab = Cab(
            city=cab_dict["city"],
            is_available=cab_dict["is_available"]
        )
        return cab
    
    def to_dict(self):
        return {
            "city": self.city,
            "is_available": self.is_available
        }