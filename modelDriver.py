import mysql.connector


class DriverModel:
    def __init__(self):
        # Connect to MySQL
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="ElifeRide"
        )

    """
    Get list of drivers available for pickup

    Args:
        ride_details(dict): The ride related details

    Returns:
        list: List of drivers available
    """

    def get_available_drivers(self, ride_details: dict):
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
