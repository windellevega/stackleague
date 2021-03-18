def bouncingBall(h, bounce, window):
    ctrPass = 1
    #code here
    if h <=0 or bounce <= 0 or bounce >= 1 or window >=h:
        return  -1

    while True:
        h *= bounce

        if(h <= window):
            break
        else:
            ctrPass += 2

    return  ctrPass

print(bouncingBall(3, 0.66, 1.5))