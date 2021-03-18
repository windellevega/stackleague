def get_total_combination(money, coins):
    combinations = [0] * (money + 1)
    combinations[0] = 1
    for coin in coins:
        for j in range(coin, money + 1):
            combinations[j] += combinations[j - coin]
    return combinations[money]


print(get_total_combination(100, [1, 5, 10, 25]))
