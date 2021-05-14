class TransportShip:
    def __init__(self, ship_type, min_fare, max_distance, capacity):
        self.ship_type = ship_type
        self.min_fare = min_fare
        self.max_distance = max_distance  # maximum distance for paying minumum fare (unit is in lightyears)
        self.capacity = capacity
        self.group_of_passengers = []
        self.map = [
            {'from':'Mon Cala','to':'Alderaan','distance':25},
            {'from':'Alderaan','to':'Coruscant','distance':3.3},
            {'from':'Coruscant','to':'Ilum','distance':14.7},
            {'from':'Ilum','to':'Jakku','distance':18},
            {'from':'Jakku','to':'Endor','distance':9.2},
            {'from':'Endor','to':'Hoth','distance':7},
            {'from':'Hoth','to':'Mustafar','distance':4.3},
            {'from':'Mustafar','to':'Dagobah','distance':4.8},
            {'from':'Dagobah','to':'Malastre','distance':8.8},
            {'from':'Malastre','to':'Naboo','distance':2.9},
            {'from':'Naboo','to':'Ryloth','distance':6.5},
        ]

    def add_passenger(self, group_of_passenger):
        # code here
        self.group_of_passengers.append(group_of_passenger)

    def total_passenger_in_group(self, passenger_name):
        for passanger in self.group_of_passengers:
            if passanger.name.lower() == passenger_name.lower():
                if passanger.companion_name == None:
                    return 1
                if not isinstance(passanger.companion_name, list):
                    return 2
                return len(passanger.companion_name) + 1
        return 0

    def calculate_distance(self, origin, destination, distance=0):
        # calculate distance between planets;
        # distance refers to current distance calculated, initialized at 0
        # distance will not be 0 in cases where getDistance calls the function
        # repeatedly as planets are traversed
        distanceTemp = distance
        for dest in self.map:
            if dest['from'].lower() == origin.lower():
                distance += dest['distance']
                origin = dest['to']

            if origin.lower() == destination.lower():
                return round(distance, 1)

        # for dest in self.map:
        #     if dest['from'].lower() == origin.lower() and dest['to'].lower() == destination.lower():
        #         distance += dest['distance']

        return distanceTemp

    def calculate_distance_reverse(self, origin, destination, distance=0):
        # calculate distance between planets in reverse order;
        # distance refers to current distance calculated, initialized at 0
        # distance will not be 0 in cases where getDistance calls the function
        # repeatedly as planets are traversed
        distanceTemp = distance
        tempMap = self.map[::-1]
        for dest in tempMap:
            if dest['to'].lower() == origin.lower():
                distance += dest['distance']
                origin = dest['from']

            if origin.lower() == destination.lower():
                return round(distance, 1)

        return distanceTemp

    # origin = mon cala -> destination = illum
    # origin = ryloth -> destination = jakku
    # origin = jakku -> destination = dagobah
    # origin = dagobah -> destination = jakku
    def get_distance(self, origin, destination):
        # calculate the distance in lightyears given the origin and destiation. Planet name can be case insensitive
        for dest in self.map:
            if dest['from'].lower() == destination.lower():
                return self.calculate_distance_reverse(origin, destination)
            if dest['from'].lower() == origin.lower():
                return self.calculate_distance(origin, destination)
        return 0.0


    def calculate_fare(self, passenger_name):
        # calculate fare of given passenger name. Name can be case insensitive
        for passenger in self.group_of_passengers:
            if passenger.name.lower() == passenger_name.lower():
                travel_distance = self.get_distance(passenger.origin, passenger.destination)
                if travel_distance <= self.max_distance:
                    return self.min_fare
                else:
                    diff_distance = travel_distance - self.max_distance
                    three_percent = self.min_fare * 0.03
                    total_fare = (diff_distance * three_percent) + self.min_fare
                    return round(total_fare, 2)
        return None

    def calculate_group_fare(self, passenger_name):
        # calculate group fare of given passenger name. Name can be case insensitive
        for passenger in self.group_of_passengers:
            if passenger.name.lower() == passenger_name.lower():
                fare = self.calculate_fare(passenger_name)

                if passenger.companion_name == None:
                    companions = 0
                else:
                    companions = len(passenger.companion_name)

                group_fare = fare * (companions + 1)
                return round(group_fare, 2)
        return None

class Passenger:
    def __init__(self, name, origin, destination, companion_name=None):
        self.name = name
        self.companion_name = companion_name  # multiples names in a list; can be null
        self.origin = origin
        self.destination = destination

    def __eq__(self, other):
        ## do not delete this
        return isinstance(other, Passenger) and \
               self.name == other.name and \
               self.origin == other.origin and \
               self.destination == other.destination and \
               self.companion_name == other.companion_name

import unittest

class MyTestCase(unittest.TestCase):

    def test_ObjectOrientedProgramming_add_passenger(self):
        falcon = TransportShip('Millenium Falcon', 45, 128, 4)
        falcon.add_passenger(Passenger('Luke', 'Endor', 'Naboo', 'Nathan'))
        falcon.add_passenger(Passenger('Porg', 'Jakku', 'Ilum', 'Hoobe,Kool'))

        self.assertEqual(falcon.group_of_passengers, [
            Passenger('Luke', 'Endor', 'Naboo', 'Nathan'),
            Passenger('Porg', 'Jakku', 'Ilum', 'Hoobe,Kool')
        ])

    def test_Algorithms_total_passenger_in_group(self):
        falcon = TransportShip('Millenium Falcon', 45, 128, 31)
        falcon.add_passenger(Passenger('Luke', 'Endor', 'Naboo'))
        falcon.add_passenger(Passenger('Porg', 'Jakku', 'Ilum', ['Hoobe', 'Kool']))
        falcon.add_passenger(Passenger('Anakin', 'Jakku', 'Naboo'))
        falcon.add_passenger(Passenger('Anni', 'Jakku', 'Ilum', ['Solo', 'Han', 'Mace', 'Windu']))

        self.assertEqual(falcon.total_passenger_in_group('luke'), 1)

    def test___SL___calculate_fare(self):
        falcon = TransportShip('Millenium Falcon', 45.50, 12, 7)
        falcon.add_passenger(Passenger('Luke', 'Endor', 'Naboo', ['Nathan']))
        falcon.add_passenger(Passenger('Porg', 'Jakku', 'Ilum', ['Hoobe', 'Kool']))
        falcon.add_passenger(Passenger('Anakin', 'Jakku', 'Naboo'))
        falcon.add_passenger(Passenger('Anni', 'Jakku', 'Ilum', ['Solo', 'Han', 'Mace', 'Windu']))
        falcon.add_passenger(Passenger('Darth', 'Jakku', 'Naboo', 'Vader'))

        self.assertEqual(falcon.calculate_fare('Luke'), 67.07)

    def test___SL___calculate_group_fare(self):
        falcon = TransportShip('Millenium Falcon', 5.5, 14, 7)
        falcon.add_passenger(Passenger('Anni', 'Jakku', 'Ilum', ['Solo', 'Han', 'Mace', 'Windu']))

        self.assertEqual(falcon.calculate_group_fare('anni'), 30.8)

    def test___SL___calculate_distance_(self):
        falcon = TransportShip('Millenium Falcon', 5.5, 14, 7)

        self.assertEqual(falcon.get_distance('Mon Cala', 'Ilum'), 43)

    def test___SL___calculate_distance_reverse(self):
        falcon = TransportShip('Millenium Falcon', 5.5, 14, 7)

        self.assertEqual(falcon.get_distance('ryloth', 'Jakku'), 43.5)

    def test___SL___calculate_distance_reverse1(self):
        falcon = TransportShip('Millenium Falcon', 5.5, 14, 7)
        a = ['mon cala', 'alderaan', 'coruscant', 'ilum', 'jakku', 'endor', 'hoth', 'mustafar', 'dagobah', 'malastre', 'naboo', 'ryloth']
        b = ['mon cala', 'alderaan', 'coruscant', 'ilum', 'jakku', 'endor', 'hoth', 'mustafar', 'dagobah', 'malastre', 'naboo', 'ryloth']
        for i in range(len(a)):
            for j in range(len(a) - 1, -1, -1):
                self.assertEqual(falcon.calculate_distance(a[i], b[j]), falcon.calculate_distance_reverse(b[j], a[i]))


if __name__ == '__main__':
    unittest.main()