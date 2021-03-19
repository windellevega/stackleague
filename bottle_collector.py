def calculate_expenses(daily_expense, daily_travels):
    totalExpense = daily_expense * len(daily_travels)

    earnings = 0
    for travel in daily_travels:
        parsedTravel = travel.split(' ')
        parsedTravel[0] = int(parsedTravel[0])
        parsedTravel[2] = float(parsedTravel[2])

        ctr = 0
        while parsedTravel[0] != 0:

            if parsedTravel[1][ctr] == 'B':
                earnings += parsedTravel[2]

            if (ctr == len(parsedTravel[1]) - 1):
                ctr = 0

            ctr += 1
            parsedTravel[0] -= 1

    if earnings > totalExpense:
        extraMoney = (earnings - totalExpense) / len(daily_travels)
        return 'Good earnings. Extra money per day: {:.2f}'.format(extraMoney)

    else:
        moneyNeeded = totalExpense - earnings
        return 'Hard times. Money needed: {:.2f}'.format(moneyNeeded)


print(calculate_expenses(250, ["5 MMZBQQQQ 37", "11 ZZBBBQ 80"]))
print(calculate_expenses(180, ["8 ABMRB 24.50"]))