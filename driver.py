from databaseProvider import DatabaseProvider


class Drivers:
    def __init__(self, rides: dict, db_provider: DatabaseProvider):
        self.db_provider = db_provider
        self.rides = rides

    def available_drivers(self):
        return self.db_provider.get_available_rides(self.rides)


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

driver = Drivers(ride_details, DatabaseProvider())
print(driver.available_drivers())
