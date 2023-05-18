from modelDriver import DriverModel
from utils import Utils
import random


class Drivers:
    def __init__(self, rides: dict, driver_model: DriverModel, utils: Utils):
        self._drivers = []
        self.driver_model = driver_model
        self.rides = rides
        self.utils = utils

    def generate_coordinates(self):
        latitude = round(random.uniform(-90, 90), 6)
        longitude = round(random.uniform(-180, 180), 6)
        return latitude, longitude

    def find_nearest_driver_id(self):
        self._drivers = self.driver_model.get_available_drivers(self.rides)
        lat1 = self.rides["pickup_latitude"]
        lon1 = self.rides["pickup_longitude"]
        driver_id_with_dist = {}

        for driver in self._drivers:
            lat2, lon2 = self.generate_coordinates()
            driver_id_with_dist[driver] = self.utils.calculate_distance(
                lat1, lon1, lat2, lon2)

        min_pairs = min(driver_id_with_dist.items(), key=lambda item: item[1])
        return min_pairs[0]


# ride_details = {
#     "passenger_id": 1,
#     "pickup_address": "Empire State Building",
#     "pickup_latitude": 40.748817,
#     "pickup_longitude": -73.985428,
#     "drop_address": "Central Park, New York, NY 10022, USA",
#     "drop_latitude": 40.782865,
#     "drop_longitude": -73.965355,
#     "estimate_duration": "1:20:00",
# }

# driver = Drivers(ride_details, DriverModel(), Utils())
# print(driver.find_nearest_driver_id())
