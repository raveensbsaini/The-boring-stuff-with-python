def isLeapYear(year):
    if year % 4 == 0:
        if year % 100  == 0 and year % 400 == 0:
            return True
        elif year % 100 == 0 and year % 400 != 0:
            return False
        else:
            return True
    else:
        return False
def isValidDate(year,month,day):
    months = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
    if 0< month <= 12 and 0<= day <= 31:
        if isLeapYear(year) :
            if month == 2:
                if 0< day <= 29:
                    return True
                else:
                    return False
        for i in months:
            if month == i:
                if 0< day <= months[i]:
                    return True
                else:
                    return False
        
    else:
        return False
        
    

assert isValidDate(1999, 12, 31) == True
assert isValidDate(2000, 2, 29) == True
assert isValidDate(2001, 2, 29) == False
assert isValidDate(2029, 13, 1) == False
assert isValidDate(1000000, 1, 1) == True
assert isValidDate(2015, 4, 31) == False
assert isValidDate(1970, 5, 99) == False
assert isValidDate(1981, 0, 3) == False
assert isValidDate(1666, 4, 0) == False
import datetime
d = datetime.date(1970, 1, 1)
oneDay = datetime.timedelta(days=1)
for i in range(1000000):
    assert isValidDate(d.year, d.month, d.day) == True
    d += oneDay
