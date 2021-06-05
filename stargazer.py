import math
import itertools
import re
import operator
import collections

def stargazer(sky, star):
    for s in sky:
        for st in sky[s]:
            if(st.lower() == star.lower()):
                return s

    return 'No constellation match.'

import unittest

class MyTestCase(unittest.TestCase):
    def test___AL___stargazer(self):
        sky = {
            "Andromeda": ["Mirach", "Almach", "Alpheratz", "Mirach's Ghost", "Andromeda Nebula"],
            "Aquarius": ["Huboor", "Ancha", "Albali", "Situla", "Sadalmelik"],
            "Aquila": ["Altair", "Libertas", "Tarazed", "Tseen Foo", "Tso Ke"],
            "Ara": ["Cervantes", "Stingray Nebula", "Water Lily Nebula"],
            "Aries": ["Botein", "Mesarthim", "Sheratan", "Hamal"],
            "Cassiopeia": ["Segin", "Ruchbah", "Navi", "Caph", "Achird", "Schedar"],
            "Orion": ["Betelgeuse", "Meissa", "Bellatrix", "Rigel", "Saiph", "Alnitak"],
        }
        self.assertEqual(stargazer(sky, "Mirach"), "Andromeda")

    def test___AL___stargazer_2(self):
        sky = {
            "Andromeda": ["Mirach", "Almach", "Alpheratz", "Mirach's Ghost", "Andromeda Nebula"],
            "Aquarius": ["Huboor", "Ancha", "Albali", "Situla", "Sadalmelik"],
            "Aquila": ["Altair", "Libertas", "Tarazed", "Tseen Foo", "Tso Ke"],
            "Ara": ["Cervantes", "Stingray Nebula", "Water Lily Nebula"],
            "Aries": ["Botein", "Mesarthim", "Sheratan", "Hamal"],
            "Cassiopeia": ["Segin", "Ruchbah", "Navi", "Caph", "Achird", "Schedar"],
            "Orion": ["Betelgeuse", "Meissa", "Bellatrix", "Rigel", "Saiph", "Alnitak"],
        }
        self.assertEqual(stargazer(sky, "MirAch"), "Andromeda")

    def test___SE___stargazer_3(self):
        sky = {
            "Andromeda": ["Mirach", "Almach", "Alpheratz", "Mirach's Ghost", "Andromeda Nebula"],
            "Aquarius": ["Huboor", "Ancha", "Albali", "Situla", "Sadalmelik"],
            "Aquila": ["Altair", "Libertas", "Tarazed", "Tseen Foo", "Tso Ke"],
            "Ara": ["Cervantes", "Stingray Nebula", "Water Lily Nebula"],
            "Aries": ["Botein", "Mesarthim", "Sheratan", "Hamal"],
            "Cassiopeia": ["Segin", "Ruchbah", "Navi", "Caph", "Achird", "Schedar"],
            "Orion": ["Betelgeuse", "Meissa", "Bellatrix", "Rigel", "Saiph", "Alnitak"],
        }
        self.assertEqual(stargazer(sky, "Sequins"), "No constellation match.")

if __name__ == '__main__':
    unittest.main()