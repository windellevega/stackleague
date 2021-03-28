def format_duration(seconds):
    MIN = 60
    HOUR = 3600
    DAY = 86400
    YEAR = 31536000
    times = []

    if seconds == 0:
        return 'now'
    if seconds >= YEAR:
        temp_time = int(seconds/YEAR)
        if temp_time > 1:
            times.append(str(temp_time) + ' years')
        else:
            times.append(str(temp_time) + ' year')
        seconds = seconds - (temp_time * YEAR)
    if seconds >= DAY:
        temp_time = int(seconds/DAY)
        if temp_time > 1:
            times.append(str(temp_time) + ' days')
        else:
            times.append(str(temp_time) + ' day')
        seconds = seconds - (temp_time * DAY)
    if seconds >= HOUR:
        temp_time = int(seconds/HOUR)
        if temp_time > 1:
            times.append(str(temp_time) + ' hours')
        else:
            times.append(str(temp_time) + ' hour')
        seconds = seconds - (temp_time * HOUR)
    if seconds >= MIN:
        temp_time = int(seconds/MIN)
        if temp_time > 1:
            times.append(str(temp_time) + ' minutes')
        else:
            times.append(str(temp_time) + ' minute')
        seconds = seconds - (temp_time * MIN)

    if seconds > 1:
        times.append(str(seconds) + ' seconds')
    elif seconds == 1:
        times.append(str(seconds) + ' second')

    times_txt = times[0]
    for x in range(1, len(times)):
        if x == len(times) - 1:
            times_txt += ' and ' + times[x]
        else:
            times_txt += ', ' + times[x]
    return times_txt

print(format_duration(0))
print(format_duration(62))
print(format_duration(65))
#mins = 60
#hours = 3600
#day = 86400
#year = 31536000