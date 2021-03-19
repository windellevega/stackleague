class TransportShip:
    def __init__(self, ship_type, min_fare, max_distance, capacity):
        self.ship_type = ship_type
        self.min_fare = min_fare
        self.max_distance = max_distance  # maximum distance for paying minumum fare (unit is in lightyears)
        self.capacity = capacity
        self.group_of_passengers = []
        self.map = [
            {'from': 'Mon Cala', 'to': 'Alderaan', 'distance': 25},
            {'from': 'Alderaan', 'to': 'Coruscant', 'distance': 3.3},
            {'from': 'Coruscant', 'to': 'Ilum', 'distance': 14.7},
            {'from': 'Ilum', 'to': 'Jakku', 'distance': 18},
            {'from': 'Jakku', 'to': 'Endor', 'distance': 9.2},
            {'from': 'Endor', 'to': 'Hoth', 'distance': 7},
            {'from': 'Hoth', 'to': 'Mustafar', 'distance': 4.3},
            {'from': 'Mustafar', 'to': 'Dagobah', 'distance': 4.8},
            {'from': 'Dagobah', 'to': 'Malastre', 'distance': 8.8},
            {'from': 'Malastre', 'to': 'Naboo', 'distance': 2.9},
            {'from': 'Naboo', 'to': 'Ryloth', 'distance': 6.5},
        ]

    def add_passenger(self, group_of_passenger):
        # code here
        self.group_of_passengers.append(group_of_passenger)

    def total_passenger_in_group(self, passenger_name):
        for passanger in self.group_of_passengers:
            if passanger.name == passenger_name:
                return len(passanger.companion_name) + 1
        return  0

    def calculate_distance(origin, destination, distance=0):
        # calculate distance between planets;
        # distance refers to current distance calculated, initialized at 0
        # distance will not be 0 in cases where getDistance calls the function
        # repeatedly as planets are traversed
        pass

    def calculate_distance_reverse(origin, destination, distance=0):
        pass
        # calculate distance between planets in reverse order;
        # distance refers to current distance calculated, initialized at 0
        # distance will not be 0 in cases where getDistance calls the function
        # repeatedly as planets are traversed

    def get_distance(self, origin, destination):
        # calculate the distance in lightyears given the origin and destiation. Planet name can be case insensitive


    def calculate_fare(self, passenger_name):
        pass
        # calculate fare of given passenger name. Name can be case insensitive

    def calculate_group_fare(self, passenger_name):
        pass
        # calculate group fare of given passenger name. Name can be case insensitive


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



falcon = TransportShip('Millenium Falcon', 45, 128, 31)
falcon.add_passenger(Passenger('Luke','Endor','Naboo',['Nathan']))
falcon.add_passenger(Passenger('Porg','Jakku','Ilum',['Hoobe','Kool']))
falcon.add_passenger(Passenger('Anakin','Jakku','Naboo'))
falcon.add_passenger(Passenger('Anni','Jakku','Ilum',['Solo','Han','Mace','Windu']))
print(falcon.get_distance('Hoth', 'Naboo'))