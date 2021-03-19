import math
class Recipe:
    def __init__(self, name, min_servings, max_servings):
        self.name = name
        self.min_servings = min_servings
        self.max_servings = max_servings
        self.ingredients = []

    def add_ingredient(self, ingredient):
        # code here
        self.ingredients.append(ingredient)

    def find_ingredient(self, ingredient_name):
        # return the Ingredient object, or None if ingredient_name can't be found in recipe
        # search is case-insensitive
        for ingredient in self.ingredients:
            if ingredient.name.lower() == ingredient_name.lower():
                return ingredient

        raise ValueError(ingredient_name + ' not part of recipe')

    def adjust_numbers(self, basis_ingredient_name, quantity_in_fridge, unit):
        ingredient = self.find_ingredient(basis_ingredient_name)
        ratio = ingredient.get_ratio(quantity_in_fridge, unit)
        self.min_servings = math.floor(self.min_servings * ratio)
        self.max_servings = math.ceil(self.max_servings * ratio)

        print(self.min_servings, self.max_servings)

        for ing in self.ingredients:
            ing.adjust(ratio)
        pass

class Ingredient:
    def __init__(self, name, quantity, unit):
        self.name = name
        self.quantity = quantity  # quantity prescribed by the recipe
        self.unit = unit

    def get_ratio(self, quantity_in_fridge, unit):
        selfQty = self.quantity
        if unit == 'g' and self.unit == 'kg':
            selfQty = self.quantity * 1000
        if unit == 'kg' and self.unit == 'g':
            quantity_in_fridge *= 1000

        return quantity_in_fridge / selfQty


    def adjust(self, ratio):
        if self.unit in ['kg', 'g']:
            self.quantity = self.quantity * ratio

            if self.unit == 'g' and self.quantity >= 1000:
                self.unit = 'kg'
                self.quantity = self.quantity / 1000
            elif self.unit == 'kg' and self.quantity < 1:
                self.unit = 'g'
                self.quantity = int(self.quantity * 1000)

        elif self.unit in ['cloves', 'pcs']:
            self.quantity = math.ceil(self.quantity * ratio)
        else:
            self.quantity = self.quantity * ratio

        if self.unit in ['cloves', 'pcs', 'g']:
            self.quantity = int(self.quantity)

        print(self.quantity, self.unit)

    def __eq__(self, other):
        # don't remove, needed by the test cases
        return isinstance(other, Ingredient) and \
               self.name == other.name and \
               abs(self.quantity - other.quantity) <= 0.001 and \
               self.unit == other.unit

recipe = Recipe('Chicken with Mushroom and Brocolli', 3, 4)
recipe.add_ingredient(Ingredient('Chicken', 1, 'kg'))
recipe.add_ingredient(Ingredient('Brocolli', 400, 'g'))
recipe.add_ingredient(Ingredient('Water', 4, 'cups'))
recipe.add_ingredient(Ingredient('Mushroom', 300, 'g'))
recipe.add_ingredient(Ingredient('Garlic', 6, 'cloves'))
recipe.adjust_numbers('chicken', 400, 'g')

# chicken = Ingredient('chicken', 500, 'g')
# chicken.adjust(3)
# print(chicken.quantity, chicken.unit)
# for ingredient in recipe.ingredients:
#     print(ingredient.name, ingredient.quantity, ingredient.unit)

# chicken = Ingredient('chicken', 2, 'kg')
# print(chicken.quantity, chicken.unit)
# chicken.adjust(0.3)
# print(chicken.quantity, chicken.unit)