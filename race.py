def race(v1, v2, g):
    if v1 >= v2:
        return None
    rel_speed = v2 - v1
    time_to_catchup = g/rel_speed
    hrs = time_to_catchup
    time_to_catchup = abs(time_to_catchup - int(hrs))
    mins = time_to_catchup * 60
    time_to_catchup = abs(mins - int(mins))
    secs = time_to_catchup * 60
    return [int(hrs), int(mins), int(secs)]

print(race(720, 850, 70))
print(race(80, 91, 37))

#10
#15