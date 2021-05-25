from pydantic import BaseModel

class RequestModel:

    def __init__(self, city):
        self.filters = {
            "city": city
        }


class CabModel(BaseModel):
    city: str
    is_available: bool