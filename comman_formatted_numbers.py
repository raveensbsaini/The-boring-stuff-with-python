def commaFormat(num):
    num = str(num)
    num = num.split(".")
    main_num = num[0]
    return_string = ""
    leng = 0
    for i,u in enumerate(main_num[::-1]):
        if leng < 3:
            return_string += u
            leng += 1
        elif leng == 3:
            return_string += ","
            return_string += u
            leng = 1
    return_string = return_string[::-1]
    try:
        dec_num = num[1]
    except:
        dec_num = None
    if dec_num :
        return_string =  return_string + "." + dec_num
    return return_string

    
assert commaFormat(1) == '1'
assert commaFormat(10) == '10'
assert commaFormat(100) == '100'
assert commaFormat(1000) == '1,000'
assert commaFormat(10000) == '10,000'
assert commaFormat(100000) == '100,000'
assert commaFormat(1000000) == '1,000,000'
assert commaFormat(1234567890) == '1,234,567,890'
assert commaFormat(1000.123456) == '1,000.123456'
