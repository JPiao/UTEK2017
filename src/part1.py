# Part 1: Finding a Charging Station
import urllib, json
from haversine import haversine_func

""" Class to represent a station """
class Station:

    """ Returns the max of 3 stations"""
    @staticmethod
    def getMax(station0, station1, station2):
        if station0.distance >= station1.distance and station0.distance >= station1.distance:
            return station0, 0
        if station1.distance >= station0.distance and station1.distance >= station2.distance:
            return station1, 1
        if station2.distance >= station0.distance and station2.distance >= station1.distance:
            return station2, 2

    """
    Constructor
    Arguments:
    latitude -- the latitude of the station
    longitude -- the longitude of the station
    name -- the name of the station
    distance -- the distance from a given starting point to this station calculated with Haversine formula
    """
    def __init__(self, latitude, longitude, name, distance):
        self.latitude = latitude
        self.longitude = longitude
        self.distance = distance
        self.name = name

    """ Prints the station according to competition specifications"""
    def mPrint(self):
        mString = str(self.latitude) + " " + str(self.longitude) + " " + self.name + " " + str(self.distance)
        print (mString)

"""
Part 1 of UTEK
Arguments:
coordinate -- a string of the coordinate
Output:
Prints 3 closest stations as output
"""
def part1(coordinate):
    # Parse the coordinate string into floats
    given_lat, given_lng = map(float, coordinate.split(' '))

    # Make the request and get the JSON
    # JSON parsing to get list of stations
    data = json.load(open("charging_stations.json"))

    # The total list of stations
    list_of_stations = data["fuel_stations"]

    # This list will contain the 3 minimum stations
    min_stations = []

    # Loop through the list of stations getting the appropriate data
    for station_dict in list_of_stations:

        latitude = station_dict["latitude"]
        longitude = station_dict["longitude"]
        name = station_dict["station_name"]
        distance = haversine_func(latitude, longitude, given_lat, given_lng)

        curr_station = Station(latitude, longitude, name, distance)

        # If don't have 3 stations, append station
        if len(min_stations) < 3:
            min_stations.append(curr_station)
        else:
            # Find the minimum station with the current max value and replace it if current station is closer
            max_station, index = Station.getMax(min_stations[0], min_stations[1], min_stations[2])

            if curr_station.distance < max_station.distance:
                min_stations[index] = curr_station

    # Sort the list in place by distance
    min_stations.sort(key=lambda x: x.distance, reverse=False)

    for station in min_stations:
        station.mPrint()

# Run from command line
if __name__  == "__main__":
    strCoor = input("Enter a coordinate: ")
    part1(strCoor)
