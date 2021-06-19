# File for describing the Cab entity.

class Cab:

    def __init__(self, city:str, brand: str, hourly_price: int, is_available: bool = True, id=None) -> None:
        self.city = city
        self.brand = brand
        self.hourly_price = hourly_price
        self.is_available = is_available
        self.id = id