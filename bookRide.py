
from faker import Faker
from databaseProvider import DatabaseProvider
import random


class BookRide:
    def __init__(
        self,
        ride_details: dict,
        passenger_details: dict,
        driver_details: dict,
        db_provider: DatabaseProvider
    ) -> str:
        self.ride_details = ride_details
        self.passenger_details = passenger_details
        self.driver_details = driver_details
        self.db_provider = db_provider

    def confirm_booking(self):
        status = self.db_provider.insert_ride(ride_details)
        if status:
            # print(f" Booking confirmed for {self.passenger_details.name}")
            print(f" Booking confirmed for {self.passenger_details['name']}")

    def find_distance(self):
        print('')


class Utils:
    def generate_coordinates(self):
        latitude = round(random.uniform(-90, 90), 6)
        longitude = round(random.uniform(-180, 180), 6)
        return latitude, longitude


util1 = Utils()

latitude, longitude = util1.generate_coordinates()
print("Latitude:", latitude)
print("Longitude:", longitude)
print("------------------")


ride_details = {
    "driver_id": 1,
    "passenger_id": 2,
    "pickup_address": "Empire State Building",
    "pickup_latitude": 40.748817,
    "pickup_longitude": -73.985428,
    "drop_address": "Central Park, New York, NY 10022, USA",
    "drop_latitude": 40.782865,
    "drop_longitude": -73.965355,
    "estimate_duration": "1:20:00",
    "start_time": "2023-05-17 05:34:56",
    "end_time": "2023-05-17 06:54:56",
}


passenger_details = {
    "name": "Leslie",
    "phone_number": "374-154-5760",
}

driver_details = {
    "name": "Leslie",
    "phone_number": "374-154-5760"
}

rideOne = BookRide(
        ride_details,
        passenger_details,
        driver_details,
        DatabaseProvider()
    )
rideOne.confirm_booking()
