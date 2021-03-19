def stock_list(listOfCode, listOfCategory) :
    qtys = []
    res = ""
    if len(listOfCode) == 0 or len(listOfCategory) == 0:
        return res
    for m in enumerate(listOfCategory) :
        qtys.append(0)
        for l in enumerate(listOfCode) :
            if m[1] == l[1][0] :
                qty_curr = l[1].partition(" ")[2]
                qtys[m[0]] += int(qty_curr)
        res += "(" + m[1] + " : " + str(qtys[m[0]])
        if m[0] == len(listOfCategory) - 1 :
            res += ")"
        else :
            res += ") - "
    return res


b = []
a = ["A", "B"]
print(stock_list(b, a))
b = ["ROXANNE 102", "RHODODE 123", "BKWRKAA 125", "BTSQZFG 239", "DRTYMKH 060"]
a = ["R", "B", "D"]
print(stock_list(b, a))