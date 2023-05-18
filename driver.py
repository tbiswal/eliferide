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

    """
    Find nearest driver to the passenger

    Returns:
        int: The driver id
    """

    def find_nearest_driver_id(self) -> int:
        self._drivers = self.driver_model.get_available_drivers(self.rides)
        lat1 = self.rides["pickup_latitude"]
        lon1 = self.rides["pickup_longitude"]
        driver_id_with_dist = {}

        # Find the avialable drivers and their lat and lon
        for driver in self._drivers:
            lat2, lon2 = self.generate_coordinates()
            driver_id_with_dist[driver] = self.utils.calculate_distance(
                lat1, lon1, lat2, lon2)

        min_pairs = min(driver_id_with_dist.items(), key=lambda item: item[1])
        return min_pairs[0]
