
from faker import Faker
from modelRide import RideModel
from modelDriver import DriverModel
from utils import Utils
from driver import Drivers


class BookRide:
    def __init__(
        self,
        ride_details: dict,
        ride_model: RideModel,
        drivers: Drivers
    ) -> str:
        self.ride_details = ride_details
        self.ride_model = ride_model
        self.drivers = drivers

    def confirm_booking(self):
        # Find driver for cheapest price and add to ride_details collection
        ride_details["driver_id"] = self.drivers.find_nearest_driver_id()
        status = self.ride_model.insert_ride(ride_details)
        passenger_id = self.ride_details["passenger_id"]

        if status:
            print(f" Booking confirmed for {passenger_id}")
        else:
            print(f" There is an issue while booking ride for {passenger_id}")


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

driver = Drivers(ride_details, DriverModel(), Utils())
ride = BookRide(ride_details, RideModel(), driver)
ride.confirm_booking()
