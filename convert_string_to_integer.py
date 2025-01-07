def convertStrToInt(string):
    isneg = False
    if string[0] == "-":
        isneg = True
        string = string[1:]
    return_int = 0
    leng = len(string)
    a = None
    for i,u in enumerate(string):
        if u == "0":
           a = 0
        elif u == "1":
           a = 1
        elif u == "2":
           a = 2
        elif u == "3":
           a = 3
        elif u == "4":
           a = 4
        elif u == "5":
           a = 5
        elif u == "6":
           a = 6
        elif u == "7":
           a = 7
        elif u == "8":
           a = 8
        elif u == "9":
           a = 9
        return_int += a * (10**(leng-1))
        leng -= 1
    if isneg:
        return_int *= -1

    return return_int

for i in range(-10000, 10000):
    assert convertStrToInt(str(i)) == i
