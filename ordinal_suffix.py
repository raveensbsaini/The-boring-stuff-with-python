def ordinalSuffix(n):
    assert n//1 == n/1
    if n in [11,12,13]:
        return str(n) + "th"
    if n == 0:
        return "0th"
    if str(n)[-1] == "1":
        return str(n)+ "st"
    elif str(n)[-1] == "2":
        return str(n)+"nd"
    elif str(n)[-1] == "3":
        return str(n)+"rd"
    else:
        return str(n) + "th"
assert ordinalSuffix(0) == '0th'
assert ordinalSuffix(1) == '1st'
assert ordinalSuffix(2) == '2nd'
assert ordinalSuffix(3) == '3rd'
assert ordinalSuffix(4) == '4th'
assert ordinalSuffix(10) == '10th'
assert ordinalSuffix(11) == '11th'
assert ordinalSuffix(12) == '12th'
assert ordinalSuffix(13) == '13th'
assert ordinalSuffix(14) == '14th'
assert ordinalSuffix(101) == '101st'
