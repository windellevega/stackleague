import math
import itertools
import re
import operator
import collections

class Portfolio:
    def __init__(self, owner):
        self.owner = owner
        self.restaurants = []

    def addRestaurant(self, restaurant):
        self.restaurants.append(restaurant)

    def removeRestaurant(self, restaurant):
        self.restaurants.remove(restaurant)

    def getRestaurants(self):
        return self.restaurants

    def getRestaurantCount(self):
        return len(self.restaurants)

    def getGrossIncome(self):
        income = 0
        for restaurant in self.restaurants:
            income += restaurant.income

        return income

    def getMostProfitableVenture(self):
        income = -99999999
        most_profit = None
        for restaurant in self.restaurants:
            if restaurant.income > income:
                income = restaurant.income
                most_profit = restaurant

        return most_profit

    def getLeastProfitableVenture(self):
        income = 999999999
        least_profit = None
        for restaurant in self.restaurants:
            if restaurant.income < income:
                income = restaurant.income
                least_profit = restaurant

        return least_profit

    def transferAssets(self, owner):
        self.owner = owner


class Restaurant:
    def __init__(self, name):
        self.name = name
        self.income = 0
        self.client = 0

    def billClient(self, amount):
        self.income += amount
        self.client += 1

    def payWages(self, amount):
        self.income -= amount

    def payTaxes(self):
        self.income -= self.income * 0.1

######################### END OF SOLUTION #########################





import unittest

class MyTestCase(unittest.TestCase):
    def test___OO___add_restaurants(self):
        portfolio = Portfolio('Sean')
        camren = Restaurant('Camren')
        racquel = Restaurant('Racquel')

        portfolio.addRestaurant(camren)
        portfolio.addRestaurant(racquel)

        self.assertListEqual(portfolio.restaurants, [camren, racquel])

        self.assertEqual(portfolio.getRestaurantCount(), 2)

    def test___OO___most_profitable_venture(self):
        portfolio = Portfolio('Sean')

        camren = Restaurant('Camren')
        camren.billClient(710)

        racquel = Restaurant('Racquel')
        racquel.billClient(701)

        demian = Restaurant('Demain')
        demian.billClient(700)

        portfolio.addRestaurant(camren)
        portfolio.addRestaurant(racquel)
        portfolio.addRestaurant(demian)

        self.assertEqual(portfolio.getMostProfitableVenture(), camren)

    def test___OO___least_profitable_venture(self):
        portfolio = Portfolio('Sean')

        camren = Restaurant('Camren')
        camren.billClient(710)

        racquel = Restaurant('Racquel')
        racquel.billClient(701)

        demian = Restaurant('Demain')
        demian.billClient(700)

        portfolio.addRestaurant(camren)
        portfolio.addRestaurant(racquel)
        portfolio.addRestaurant(demian)

        self.assertEqual(portfolio.getLeastProfitableVenture(), demian)

    def test___SE___bill_client(self):
        ko = Restaurant('Ko')
        ko.billClient(300)

        self.assertEqual(ko.income, 300)
        self.assertEqual(ko.client, 1)

    def test___SE___pay_taxes(self):
        ko = Restaurant('Ko')
        ko.billClient(300)
        ko.payTaxes()

        self.assertEqual(ko.income, 270)
        self.assertEqual(ko.client, 1)


if __name__ == '__main__':
    unittest.main()