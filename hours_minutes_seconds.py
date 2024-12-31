def getHoursMinutesSeconds(time:int):
    if time == 0:
        return "0s"
    return_string = ""
    h = time//3600
    reminder = time - (h*3600)
    m = reminder // 60
    reminder = reminder - (m * 60)
    if h > 0:
        return_string = f"{h}h"
    if m > 0:
        if len(return_string) > 0:
            return_string += f" {m}m"
        else:
            return_string = f"{m}m"
    if reminder > 0:
        if len(return_string) > 0:
            return_string += f" {reminder}s"
        else:
            return_string += f"{reminder}s"
    return return_string
assert getHoursMinutesSeconds(60) == '1m'
assert getHoursMinutesSeconds(90) == '1m 30s'
assert getHoursMinutesSeconds(3600) == '1h'
assert getHoursMinutesSeconds(3601) == '1h 1s'
assert getHoursMinutesSeconds(3661) == '1h 1m 1s'
assert getHoursMinutesSeconds(90042) == '25h 42s'
assert getHoursMinutesSeconds(0) == '0s'
