import math
def harvester_rescue(data):
    distanceWorm = math.sqrt(math.pow(data['harvester'][0] - data['worm'][0][0], 2) + math.pow(data['harvester'][1] - data['worm'][0][1], 2))
    distanceCarryall = math.sqrt(math.pow(data['harvester'][0] - data['carryall'][0][0], 2) + math.pow(data['harvester'][1] - data['carryall'][0][1], 2))

    timeWorm = distanceWorm / data['worm'][1]
    timeCarryall = (distanceCarryall / data['carryall'][1]) + 1

    if timeCarryall < timeWorm:
        return 'The spice must flow! Rescue the harvester!'

    return 'Damn the spice! I\'ll rescue the miners!'

print(harvester_rescue({'harvester': [345,600], 'worm': [[200,100],25], 'carryall': [[350,200],32]}))
#sqrt(pow(345-200, 2) + pow(600-100, 2))
#sqrt(pow(145, 2) + pow(500, 2))
#sqrt(21025 + 250000)
#sqrt(271025)
#520.6/25 = 20.824

#sqrt(pow(345-350, 2) + pow(600-200, 2))
#sqrt(pow(5,2) + pow(400,2))
#sqrt(25 + 160000)
#sqrt(160025)
#400.03/32 = 12.5 + 1 = 13.5

print(harvester_rescue({'harvester': [200,400], 'worm': [[200,0],40], 'carryall': [[500,100],45]}))
#sqrt(pow(200-200, 2) + pow(400-0, 2))
#sqrt(pow(0, 2) + pow(400, 2))
#sqrt(0 + 160000)
#sqrt(160000)
#400/40 = 10

#sqrt(pow(200-500, 2) + pow(400-100, 2))
#sqrt(pow(300, 2) + pow(300, 2))
#sqrt(90000 + 90000)
#sqrt(180000)
#424.26/45 = 9.43 + 1 = 10.43