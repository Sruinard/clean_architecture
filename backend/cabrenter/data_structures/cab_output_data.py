
class CabOutputData:
    def __init__(self, city: str, is_available: bool, datetime: str):
        self.city = city
        self.is_available = is_available
        self.datetime = datetime

    def to_dict(self):
        return {
            "city": self.city,
            "is_available": self.is_available,
            "datetime": self.datetime
        }