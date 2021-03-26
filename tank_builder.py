import math
def tank_price(height, diameter, unit, quantity):
    if height == 0 or diameter == 0 or quantity == 0:
        return 0

    if unit == 'in':
        height = height / 39.370079
        diameter = diameter / 39.370079
    elif unit == 'ft':
        height = height / 3.2808399
        diameter = diameter / 3.2808399

    radius = diameter / 2

    surface_area = (2 * math.pi * math.pow(radius, 2)) + (2 * math.pi * radius * height)
    surface_area = surface_area * quantity

    return (surface_area + 1) * 100

print(tank_price(10, 2, 'in', 1))