def josephus(xs, k):
    if xs == []:
        return []
    k -= 1
    ctr = k
    arr = []
    while len(xs) > 1:
        arr.append(xs.pop(ctr))
        ctr = (ctr + k) % len(xs)
    arr.append(xs[0])
    return arr

print(josephus([1,2,3,4,5,6,7,8,9,10],1))
print(josephus([1,2,3,4,5,6,7,8,9,10],2))
print(josephus([],2))