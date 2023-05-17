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
