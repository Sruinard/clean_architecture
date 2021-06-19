# File containing endpoint request models.
from pydantic import BaseModel

class CabConfiguration(BaseModel):
    city: str
    hourly_price: int 
    brand: str