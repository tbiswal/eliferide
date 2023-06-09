# ElifeRide

## Challenge

We have a lot of rides in New York for tomorrow, and we have a lot drivers in New York. We need to do a backend algorithm to figure out which ride to give to which driver so that

- there is no conflict, e.g., we don't give the 2 different rides at 9 AM to the same driver
- we want to give the ride a lower priced driver if possible.
- if we give a ride to pick up a passenger from New York time square and drop off the passenger at JFK airport to a driver, the next ride we give to the same driver should preferably pick up from JFK airport, this way, the driver doesn't have to drive a lot without a paying passenger on the car.

You may assume as input a collection of rides. Each ride consists of pickup time, pickup location (latitude/longitude), pickup address, drop off location/address and estimated ride duration.

## Solution

### Assumptions

- Input - a collection of rides.
- Distance unit is measured in kilometer
- Initially, take five drivers and create a database of drivers
- Three passengers who already signed up and existed in the database
- Design the solution for thousand rides
- I will use random location(latitude and longitude) to simulate driver's location
- The driver is closest to passenger's location will be considered as cheapest driver

### Schema Design

I will use MySql as a database provider.

#### Driver

- id(primary) primary, auto increment
- name(varchar 100)
- phone_number(varchar 50)

#### Passenger

- id(int) primary, auto increment
- name(varchar 100)
- phone_number(varchar 50)

#### Ride

- id(int) primary, auto increment
- driver_id(int)
- passenger_id(int)
- pickup_address(varchar 200)
- pickup_latitude(float)
- pickup_longitude(float)
- drop_address(varchar 200)
- drop_location(point)
- start_time(timestamp)
- end_time(timestamp)

unique(driver_id, start_time)

FOREIGN KEY - driver_id(drivers table id column)

FOREIGN KEY - passenger_id(passengers table id column)

### Algorithm

1. There is no conflict, e.g., we don't give two different rides at 9 AM to the same driver

- Using accurate driver status:

  - Driver status can be true or false at one time. true means it can be assigned else not.
  
  - ride_assigned(ride is assigned to driver but driver not accepted) - status false
  - ride_confirmed(pickup done) - status false
  - ride_declined(ride declined by driver or cancelled by passenger) - status true
  - ride_ended(drop done) - status true

> If the driver status is false then search for another driver having status true

- Another basic approach: Combining driver_id and start_time(DateTime) as unique can solve this issue at primary stage

2. We want to give the ride to a lower-priced driver if possible.

- Find out the list of available drivers for the new ride
  
  - Checklist of drivers present in the driver table but not in the ride table, which means they are new to the app and have not started any rides yet
  - Find all the drivers who already dropped the passengers in the ride table, which means end_time is not empty
- Calculate the nearest ride available for a lower price
  - The nearby location can be calculated using the distance between the available driver's current location and the pickup location.
- Choose the shortest distance from the above step and assign the driver to that ride
- Confirm booking
  
3. if we give a ride to pick up a passenger from New York Time Square and drop off the passenger at JFK airport to a driver, the next ride we give to the same driver should preferably pick up from JFK airport; this way, the driver doesn't have to drive a lot without a paying passenger on the car.
  
- The second step solution will solve the third problem if the passenger is near the drop-off location, then it will notify the driver if the driver is near the drop-off location.

### What I have not considered

- If two drivers are at the exact location, assign the ride to the driver with fewer rides on that day.
- I have not considered the scalability; rather focussed on MVP
- I have not considered the velocity of the vehicle to calculate the estimated duration and price

### MySql Query

```
  create database ElifeRide;

  create table drivers(
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    phone_number VARCHAR(50) NOT NULL
  );

  create table passengers(
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    phone_number VARCHAR(50) NOT NULL
  );

  create table rides(
    id INT AUTO_INCREMENT PRIMARY KEY,
    driver_id INT NOT NULL,
    passenger_id INT NOT NULL,
    pickup_address VARCHAR(200),
    pickup_latitude FLOAT NOT NULL,
    pickup_longitude FLOAT NOT NULL,
    drop_address VARCHAR(200),
    drop_latitude FLOAT NOT NULL,
    drop_longitude FLOAT NOT NULL,
    estimate_duration TIME,
    start_time DATETIME DEFAULT CURRENT_TIMESTAMP,
    end_time DATETIME
  );
  
  ALTER TABLE rides ADD CONSTRAINT uk_ride_driver_assign UNIQUE (driver_id, start_time);
```

### Seeds

Drivers

```
  INSERT INTO drivers (name, phone_number) VALUES ('Leslie Juarez', '374-154-5760');
  INSERT INTO drivers (name, phone_number) VALUES ('Chloe Edwards', '0257975722');
  INSERT INTO drivers (name, phone_number) VALUES ('Alexis Jones', '971-303-9565');
  INSERT INTO drivers (name, phone_number) VALUES ('Harold Dillon', '001-676-468-5997x2768');
  INSERT INTO drivers (name, phone_number) VALUES ('Ronald Ross', '775-550-3127x6903');
```

Passengers

```
  INSERT INTO passengers (name, phone_number) VALUES ('Victoria Reed', '+1-282-827-5488x71560');
  INSERT INTO passengers (name, phone_number) VALUES ('Michael Allen', '+1-133-919-5943x1888');
  INSERT INTO passengers (name, phone_number) VALUES ('Madison Huang', '272.872.4072');
```

### Installed package

```
  pip install faker
  pip install mysql-connector-python
  pip install geopy
```

### Further optimization

- Adding a proper index to the table
- Proper error handling
- SubQuery optimization using join
- Validation
