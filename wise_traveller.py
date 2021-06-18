#Problem Definition
# Once a there was a traveller who is wise enough to plan his travels.
# He used his coding ability to plot every possible routes from one point to another.
# These possible routes does not only include a direct travel from point A to point B.
# It may but not necessarily include travelling to other points as well before arriving to the destination
# (e.g. Travelling from point A to point B can have routes A-B, A-C-B, A-D-C-B and so on)
# He analyzed every travel points where he came into conclusion that travelling directly from one point
# to another point does not always have the least cost (e.g. taking the route A-B costs P150.00 while taking the route A-C-B costs P120.00).
# He then created a program to calculate fares on these possible routes to minimize his travel cost.
# You were amazed by this traveller and wanted to re-create the same program but this time you want to consider the time of travel instead of fare cost.
# You need to create a function that could determine the route with the shortest possible travel time given the map/list of
# different routes, your origin and your destination. The function will then return a string which consists of
# the route from origin to destination followed by the total travel time expressed in hours. (e.g. A-C-B : 4.5 hours)
# Note:
# - Input map/list/dictionary are all in proper/title case however origin and destination are all case insensitive
# - If there is no possible route return 'No possible route'
# - If origin, destination or graph is invalid or empty input return an Error

import math
import itertools
import re
import operator
import collections

def wise_traveller(graph, origin, destination):
    graph = eval(repr(graph).lower())
    origin = origin.lower()
    destination = destination.lower()

    if origin not in graph or destination not in graph:
        return ValueError

    shortest_distance = {}
    track_predecessor = {}
    unvisited_points = graph
    INFINITY = 9999999
    track_path = []

    for point in unvisited_points:
        shortest_distance[point] = INFINITY

    shortest_distance[origin] = 0

    while len(unvisited_points) > 0:
        min_distance_point = None

        for point in unvisited_points:
            if min_distance_point == None:
                min_distance_point = point
            elif shortest_distance[point] < shortest_distance[min_distance_point]:
                min_distance_point = point

        path_options = graph[min_distance_point]

        for child_point in path_options:
            if path_options[child_point] + shortest_distance[min_distance_point] < shortest_distance[child_point]:
                shortest_distance[child_point] = path_options[child_point] + shortest_distance[min_distance_point]
                track_predecessor[child_point] = min_distance_point

        unvisited_points.pop(min_distance_point)

    current_point = destination

    if current_point not in track_predecessor:
        return 'No possible route'

    while current_point != origin:
        track_path.append(current_point)
        current_point = track_predecessor[current_point]

    track_path.append(origin)

    track_path = [path.title() for path in track_path]
    return '-'.join(track_path[::-1]) + ' : ' + str(shortest_distance[destination]) + ' hours'



######################### END OF SOLUTION #########################


import unittest

class MyTestCase(unittest.TestCase):
    # SAMPLE CASE
    def test___AL___sample_case_route_search(self):
        graph = {
            'Tuguegarao': { 'Iguig': 0.5, 'Amulung': 1.5 },
            'Iguig':{ 'Aparri': 4.5, 'Penablanca': 0.75, 'Tuguegarao': 0.5 },
            'Amulung':{ 'Penablanca': 0.6, 'Tuguegarao': 1.5, 'Enrile': 2.75 },
            'Penablanca':{ 'Iguig': 0.75, 'Amulung': 0.6, 'Enrile': 0.9 },
            'Aparri': { 'Iguig': 4.5 },
            'Enrile': { 'Piat': 0.8, 'Penablanca': 0.9, 'Amulung': 2.75 },
            'Piat': { 'Amulung': 2, 'Enrile': 0.8 },
            'Claveria': { 'Tuao': 6 },
            'Tuao': { 'Claveria': 6 },
        }

        self.assertEqual(wise_traveller(graph, 'Enrile', 'Iguig'), 'Enrile-Penablanca-Iguig : 1.65 hours')

    def test___AL___sample_case_route_search_case_insensitive(self):
        graph = {
            'Tuguegarao': { 'Iguig': 0.5, 'Amulung': 1.5 },
            'Iguig':{ 'Aparri': 4.5, 'Penablanca': 0.75, 'Tuguegarao': 0.5 },
            'Amulung':{ 'Penablanca': 0.6, 'Tuguegarao': 1.5, 'Enrile': 2.75 },
            'Penablanca':{ 'Iguig': 0.75, 'Amulung': 0.6, 'Enrile': 0.9 },
            'Aparri': { 'Iguig': 4.5 },
            'Enrile': { 'Piat': 0.8, 'Penablanca': 0.9, 'Amulung': 2.75 },
            'Piat': { 'Amulung': 2, 'Enrile': 0.8 },
            'Claveria': { 'Tuao': 6 },
            'Tuao': { 'Claveria': 6 }
        }

        self.assertEqual(wise_traveller(graph, 'IguiG', 'PIAt'), 'Iguig-Penablanca-Enrile-Piat : 2.45 hours')

    def test___AL___sample_case_only_one_possible_route(self):
        graph = {
            'Tuguegarao': {'Iguig': 0.5, 'Amulung': 1.5},
            'Iguig': {'Aparri': 4.5, 'Penablanca': 0.75, 'Tuguegarao': 0.5},
            'Amulung': {'Penablanca': 0.6, 'Tuguegarao': 1.5, 'Enrile': 2.75},
            'Penablanca': {'Iguig': 0.75, 'Amulung': 0.6, 'Enrile': 0.9},
            'Aparri': {'Iguig': 4.5},
            'Enrile': {'Piat': 0.8, 'Penablanca': 0.9, 'Amulung': 2.75},
            'Piat': {'Amulung': 2, 'Enrile': 0.8},
            'Claveria': {'Tuao': 6},
            'Tuao': {'Claveria': 6}
        }

        self.assertEqual(wise_traveller(graph, 'Claveria', 'Tuao'), 'Claveria-Tuao : 6 hours')

    def test___AL___sample_case_no_possible_route(self):
        graph = {
            'Tuguegarao': {'Iguig': 0.5, 'Amulung': 1.5},
            'Iguig': {'Aparri': 4.5, 'Penablanca': 0.75, 'Tuguegarao': 0.5},
            'Amulung': {'Penablanca': 0.6, 'Tuguegarao': 1.5, 'Enrile': 2.75},
            'Penablanca': {'Iguig': 0.75, 'Amulung': 0.6, 'Enrile': 0.9},
            'Aparri': {'Iguig': 4.5},
            'Enrile': {'Piat': 0.8, 'Penablanca': 0.9, 'Amulung': 2.75},
            'Piat': {'Amulung': 2, 'Enrile': 0.8},
            'Claveria': {'Tuao': 6},
            'Tuao': {'Claveria': 6}
        }

        self.assertEqual(wise_traveller(graph, 'Tuguegarao', 'Tuao'), 'No possible route')

    # TEST CASE
    def test___AL___case_not_direct_route(self):
        graph = {
            'Tuao': {'Claveria': 6, 'Santa Ana': 1},
            'Claveria': {'Tuao': 6, 'Santa Ana': 2},
            'Tuguegarao': {'Iguig': 0.5, 'Amulung': 1.5},
            'Iguig': {'Aparri': 4.5, 'Penablanca': 0.75, 'Tuguegarao': 0.5},
            'Amulung': {'Penablanca': 0.6, 'Tuguegarao': 1.5, 'Enrile': 2.75},
            'Penablanca': {'Iguig': 0.75, 'Amulung': 0.6, 'Enrile': 0.9},
            'Aparri': {'Iguig': 4.5},
            'Enrile': {'Piat': 0.8, 'Penablanca': 0.9, 'Amulung': 2.75},
            'Piat': {'Amulung': 2, 'Enrile': 0.8},
            'Santa Ana': {'Tuao': 1, 'Claveria': 2}
        }

        self.assertEqual(wise_traveller(graph, 'Tuao', 'Claveria'), 'Tuao-Santa Ana-Claveria : 3 hours')

    def test___EH___case_one_invalid_input(self):
        graph = {
            'Tuguegarao': {'Iguig': 0.5, 'Amulung': 1.5},
            'Iguig': {'Aparri': 4.5, 'Penablanca': 0.75, 'Tuguegarao': 0.5},
            'Amulung': {'Penablanca': 0.6, 'Tuguegarao': 1.5, 'Enrile': 2.75},
            'Penablanca': {'Iguig': 0.75, 'Amulung': 0.6, 'Enrile': 0.9},
            'Aparri': {'Iguig': 4.5},
            'Enrile': {'Piat': 0.8, 'Penablanca': 0.9, 'Amulung': 2.75},
            'Piat': {'Amulung': 2, 'Enrile': 0.8},
            'Claveria': {'Tuao': 6},
            'Tuao': {'Claveria': 6}
        }

        self.assertEqual(wise_traveller(graph, 'Tgurao', 'Tuao'), ValueError)

    def test___EH___case_two_invalid_inputs(self):
        graph = {
            'Tuguegarao': {'Iguig': 0.5, 'Amulung': 1.5},
            'Iguig': {'Aparri': 4.5, 'Penablanca': 0.75, 'Tuguegarao': 0.5},
            'Amulung': {'Penablanca': 0.6, 'Tuguegarao': 1.5, 'Enrile': 2.75},
            'Penablanca': {'Iguig': 0.75, 'Amulung': 0.6, 'Enrile': 0.9},
            'Aparri': {'Iguig': 4.5},
            'Enrile': {'Piat': 0.8, 'Penablanca': 0.9, 'Amulung': 2.75},
            'Piat': {'Amulung': 2, 'Enrile': 0.8},
            'Claveria': {'Tuao': 6},
            'Tuao': {'Claveria': 6}
        }

        self.assertEqual(wise_traveller(graph, 'Tgurao', 'Invplace'), ValueError)

    def test___EH___case_empty_string_input(self):
        graph = {
            'Tuguegarao': {'Iguig': 0.5, 'Amulung': 1.5},
            'Iguig': {'Aparri': 4.5, 'Penablanca': 0.75, 'Tuguegarao': 0.5},
            'Amulung': {'Penablanca': 0.6, 'Tuguegarao': 1.5, 'Enrile': 2.75},
            'Penablanca': {'Iguig': 0.75, 'Amulung': 0.6, 'Enrile': 0.9},
            'Aparri': {'Iguig': 4.5},
            'Enrile': {'Piat': 0.8, 'Penablanca': 0.9, 'Amulung': 2.75},
            'Piat': {'Amulung': 2, 'Enrile': 0.8},
            'Claveria': {'Tuao': 6},
            'Tuao': {'Claveria': 6}
        }

        self.assertEqual(wise_traveller(graph, '', 'Invplace'), ValueError)

    def test___EH___case_empty_string_inputs(self):
        graph = {
            'Tuguegarao': {'Iguig': 0.5, 'Amulung': 1.5},
            'Iguig': {'Aparri': 4.5, 'Penablanca': 0.75, 'Tuguegarao': 0.5},
            'Amulung': {'Penablanca': 0.6, 'Tuguegarao': 1.5, 'Enrile': 2.75},
            'Penablanca': {'Iguig': 0.75, 'Amulung': 0.6, 'Enrile': 0.9},
            'Aparri': {'Iguig': 4.5},
            'Enrile': {'Piat': 0.8, 'Penablanca': 0.9, 'Amulung': 2.75},
            'Piat': {'Amulung': 2, 'Enrile': 0.8},
            'Claveria': {'Tuao': 6},
            'Tuao': {'Claveria': 6}
        }

        self.assertEqual(wise_traveller(graph, '', ''), ValueError)

    def test___EH___case_empty_graph(self):
        graph = {}

        self.assertEqual(wise_traveller(graph, 'Tugue', 'Manila'), ValueError)

    def test___AL___case_route_search(self):
        graph = {
            'Tuguegarao': { 'Iguig': 0.5, 'Amulung': 1.5 },
            'Iguig':{ 'Aparri': 4.5, 'Penablanca': 0.75, 'Tuguegarao': 0.5 },
            'Amulung':{ 'Penablanca': 0.6, 'Tuguegarao': 1.5, 'Enrile': 2.75 },
            'Penablanca':{ 'Iguig': 0.75, 'Amulung': 0.6, 'Enrile': 0.9 },
            'Aparri': { 'Iguig': 4.5 },
            'Enrile': { 'Piat': 0.8, 'Penablanca': 0.9, 'Amulung': 2.75 },
            'Piat': { 'Amulung': 2, 'Enrile': 0.8 },
            'Claveria': { 'Tuao': 6 },
            'Tuao': { 'Claveria': 6 },
        }

        self.assertEqual(wise_traveller(graph, 'Piat', 'Aparri'), 'Piat-Enrile-Penablanca-Iguig-Aparri : 6.95 hours')

    def test___AL___case_route_search_case_insensitive(self):
        graph = {
            'Tuguegarao': { 'Iguig': 0.5, 'Amulung': 1.5 },
            'Iguig':{ 'Aparri': 4.5, 'Penablanca': 0.75, 'Tuguegarao': 0.5 },
            'Amulung':{ 'Penablanca': 0.6, 'Tuguegarao': 1.5, 'Enrile': 2.75 },
            'Penablanca':{ 'Iguig': 0.75, 'Amulung': 0.6, 'Enrile': 0.9 },
            'Aparri': { 'Iguig': 4.5 },
            'Enrile': { 'Piat': 0.8, 'Penablanca': 0.9, 'Amulung': 2.75 },
            'Piat': { 'Amulung': 2, 'Enrile': 0.8 },
            'Claveria': { 'Tuao': 6 },
            'Tuao': { 'Claveria': 6 },
        }

        self.assertEqual(wise_traveller(graph, 'PeNABlancA', 'EnRiLE'), 'Penablanca-Enrile : 0.9 hours')

    def test___AL___case_only_one_possible_route(self):
        graph = {
            'Ugac Sur': {'Buntun': 0.2, 'Ugac Norte': 0.1},
            'Buntun': {'Ugac Sur': 0.2},
            'Ugac Norte': {'Ugac Sur': 0.1}
        }

        self.assertEqual(wise_traveller(graph, 'Ugac Sur', 'Buntun'), 'Ugac Sur-Buntun : 0.2 hours')

if __name__ == '__main__':
    unittest.main()