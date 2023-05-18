from modelDriver import DriverModel
import random


class Drivers:
    def __init__(self, rides: dict, driver_model: DriverModel):
        self.driver_model = driver_model
        self.rides = rides
        self._drivers = []

    def generate_coordinates(self):
        latitude = round(random.uniform(-90, 90), 6)
        longitude = round(random.uniform(-180, 180), 6)
        return latitude, longitude

    def find_nearest_drivers(self):
        self._drivers = self.driver_model.get_available_drivers(self.rides)
        for driver in self._drivers:
            print(driver)
            print(self.generate_coordinates())


ride_details = {
    "passenger_id": 1,
    "pickup_address": "Empire State Building",
    "pickup_latitude": 40.748817,
    "pickup_longitude": -73.985428,
    "drop_address": "Central Park, New York, NY 10022, USA",
    "drop_latitude": 40.782865,
    "drop_longitude": -73.965355,
    "estimate_duration": "1:20:00",
 }

driver = Drivers(ride_details, DriverModel())
print(driver.find_nearest_drivers())
