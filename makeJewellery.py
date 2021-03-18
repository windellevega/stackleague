from math import floor

def make_jewellery(accessories_to_make, silver_for_one_item, available_silver, jewels_available, jewel_price):
    able_to_make = floor(available_silver / silver_for_one_item)
    total_grams_required = accessories_to_make * silver_for_one_item
    needed_more_grams = total_grams_required - available_silver
    total_cost_of_jewels = jewel_price * jewels_available

    price_profit = total_cost_of_jewels / accessories_to_make * 1.25
    # code here
    if able_to_make < accessories_to_make:
        return "Could only make " + str(able_to_make) + " accessories. " + "Need " + str("{:.2F}".format(needed_more_grams)) + " more silver"
    else:
        return "All accessories available. Price for one: " + str("{:.2F}".format(price_profit))

print(make_jewellery(100, 20, 1000, 130, 12))
print(make_jewellery(100, 20, 2000, 130, 12))