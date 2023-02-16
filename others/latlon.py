# Python 3 program to calculate Distance Between Two Points on Earth
from math import asin, cos, radians, sin, sqrt


def distance(lat1, lat2, lon1, lon2):
    # The math module contains a function named
    # radians which converts from degrees to radians.
    lon1 = radians(lon1)
    lon2 = radians(lon2)
    lat1 = radians(lat1)
    lat2 = radians(lat2)

    # Haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2

    c = 2 * asin(sqrt(a))

    # Radius of earth in kilometers. Use 3956 for miles
    r = 6371

    # calculate the result
    return (c * r)


# driver code
lat1 = 11.1360
lon1 = 75.8272

lat2 = 33.2778
lon2 = 75.3412

dist = round(float(distance(lat1, lat2, lon1, lon2)), 2)
print(dist, "KM")
