#x interval = 1/n
#y = x^2
import math
def len_curve(n):
    interval = 1 / n;
    len = 0.0
    tempX = 0
    tempY = 0
    prevH = 0
    #print(interval)

    for ctr in range(n):
        tempX =  tempX + interval
        tempY = (tempX * tempX) - prevH
        prevH = tempX * tempX
        #print(tempX, tempY)
        len += math.sqrt(pow(interval, 2) + pow(tempY, 2))

    return float('%0.9f' % len)
print(len_curve(1000))

#x=0.1, y=0.01
#x=0.2, y=0.04
#x=0.3, y=0.09
#x=0.4, y=0.16