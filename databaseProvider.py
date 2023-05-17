import mysql.connector


class DatabaseProvider:
    def __init__(self):
        # Connect to MySQL
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="ElifeRide"
        )

    def insert_ride(self, ride_details: dict):
        cursor = self.db.cursor()

        query = """
            INSERT INTO rides(
                    driver_id,
                    passenger_id,
                    pickup_address,
                    pickup_latitude,
                    pickup_longitude,
                    drop_address,
                    drop_latitude,
                    drop_longitude,
                    estimate_duration,
                    start_time,
                    end_time
                    )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        values = (
            ride_details["driver_id"],
            ride_details["passenger_id"],
            ride_details["pickup_address"],
            ride_details["pickup_latitude"],
            ride_details["pickup_longitude"],
            ride_details["drop_address"],
            ride_details["drop_latitude"],
            ride_details["drop_longitude"],
            ride_details["estimate_duration"],
            ride_details["start_time"],
            ride_details["end_time"]
        )

        try:
            cursor.execute(query, values)
            self.db.commit()
            print("Data inserted successfully!")
            return True
        except mysql.connector.Error as error:
            print("Error inserting data into MySQL table:", error)
        finally:
            cursor.close()
            self.db.close()

    """
    Get list of drivers available for pickup

    Args:
        ride_details(dict): The ride related details

    Returns:
        list: List of drivers available
    """

    def get_available_rides(self, ride_details: dict):
        cursor = self.db.cursor()

        query = """
            SELECT DISTINCT(dr.id) as driver_id
            FROM drivers AS dr
            LEFT JOIN rides ri
            ON dr.id = ri.driver_id
            WHERE (ri.id IS NOT NULL AND ri.end_time IS NOT NULL
                   AND ri.driver_id NOT IN
                   (SELECT driver_id FROM rides WHERE end_time IS NULL)
            )
            OR (ri.id IS NULL)
        """

        try:
            cursor.execute(query)
            rows = cursor.fetchall()
            available_drivers = []

            for row in rows:
                available_drivers.append(row[0])

            return available_drivers
        except mysql.connector.Error as error:
            print("Error while fetching data from MySQL table:", error)
        finally:
            cursor.close()
            self.db.close()
