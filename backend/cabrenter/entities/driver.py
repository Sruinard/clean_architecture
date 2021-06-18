

class Driver:
    def __init__(self, name, email, phone, operating_city, cab=None, driver_id=None) -> None:
        self.name = name
        self.email = email
        self.phone = phone
        self.operating_city = operating_city
        self.cab = cab
        self.driver_id = driver_id
