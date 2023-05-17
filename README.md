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
- Ride price per mile - 2$
- Initially, take five drivers and create a database of drivers
- Three passengers who already signed up and exist in the database
- If two drivers are at the exact location, then assign the driver who has fewer rides on that day
- Design the solution for thousand rides

### Schema Design

I will use MySql as a database provider

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

### Approach

1.There is no conflict, e.g., we don't give the 2 different rides at 9 AM to the same driver

- Combining driver_id and start_time(datetime) as unique can solve this issue

2.We want to give the ride a lower priced driver if possible.

- Find out the list of available drivers for the new ride
  
  - Check list of drivers present in the driver table but not in ride table which means they are new to app and have not started any ride yet
  - Find all the drivers who already dropped the passengers in the ride table that means end_time is not empty
- Calculate the nearest ride available for cheaper price
  - The nearby location can be calculated using the distance between available driver's current location and pickup location.
- Choose the shortest distance from the above step and assign the driver to that ride
  
3.if we give a ride to pick up a passenger from New York time square and drop off the passenger at JFK airport to a driver, the next ride we give to the same driver should preferably pick up from JFK airport, this way, the driver doesn't have to drive a lot without a paying passenger on the car.
  
- The second step solution will solve the third problem as if the passenger will be near to drop off location then it will notify the driver if the drive is near to drop off location.

### What I have not considered

- If two drivers are at the exact location, then assign the ride to the driver who has fewer rides on that day.
- I have not considered the scalability rather focussed on MVP
- I have not considered the velocity of the vehicle to calculate estimate duration

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
```

### Further optimization

- Adding proper index to the table
- Proper error handling
- Query optimization
