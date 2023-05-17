import geocoder


class Location:
    def get_current_location():
        g = geocoder.ip('me')
        latitude = g.lat
        longitude = g.lng

        return latitude, longitude
