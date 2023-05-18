
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
            print(f" Booking confirmed for passenge: {passenger_id}")
        else:
            print(f" There is an issue while booking ride for passenger: {passenger_id}")


fake = Faker()
fake.locale = 'en_US'

ride_details = {
    "passenger_id": fake.random_int(min=1, max=5),
    "pickup_address": fake.address(),
    "pickup_latitude": fake.latitude(),
    "pickup_longitude": fake.longitude(),
    "drop_address": fake.address(),
    "drop_latitude": fake.latitude(),
    "drop_longitude": fake.longitude(),
    "estimate_duration": "1:20:00",
}

driver = Drivers(ride_details, DriverModel(), Utils())
ride = BookRide(ride_details, RideModel(), driver)
ride.confirm_booking()
