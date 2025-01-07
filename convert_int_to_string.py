def convertIntToStr(num):
    return_string = ""
    if num == 0:
        return "0"
    isneg = False
    if num < 0:
        isneg = True
        num *= -1
    assert num >= 0
    list1 = []
    a =1
    while a*10 <= num:
        a *= 10
    while num >= 1:
        list1.append(num//a)
        digit = num // a
        num = num - (digit)*a
        if num == 0:
            while a  > 1:
                list1.append(0)
                a /= 10
            break
        a //= 10
    for i in list1:
        if i == 1:
            return_string += "1"
        elif i == 2:
            return_string += "2"
        elif i == 3:
            return_string += "3"
        elif i == 4:
            return_string += "4"
        elif i == 5:
            return_string += "5"
        elif i == 6:
            return_string += "6"
        elif i == 7:
            return_string += "7"
        elif i == 8:
            return_string += "8"
        elif i == 9:
            return_string += "9"
        elif i == 0:
            return_string += "0"
    if isneg:
        return_string =  "-"+ return_string
    return return_string
        
for i in range(-10000, 10000):
    assert convertIntToStr(i) == str(i)
