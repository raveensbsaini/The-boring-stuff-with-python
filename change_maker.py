def makeChange(amount):
    return_dict = {}
    # d = {
    #     'quarters': 0,
    #      'dimes': 0,
    #      'nickels': 0, 
    #      'pennies': 0
    #  }
    quarters = amount// 25
    r = amount - (quarters*25)
    if quarters > 0:
        return_dict['quarters'] = quarters
    dimes = r //10
    r = r - (dimes*10)
    if dimes > 0:
        return_dict['dimes'] = dimes
    nickles = r// 5
    r = r - (nickles*5)
    if nickles > 0:
        return_dict['nickels'] = nickles
    if r > 0:
        return_dict['pennies'] = r
    return return_dict
         
assert makeChange(30) == {'quarters': 1, 'nickels': 1}
assert makeChange(10) == {'dimes': 1}
assert makeChange(57) == {'quarters': 2, 'nickels': 1, 'pennies': 2}
assert makeChange(100) == {'quarters': 4}
assert makeChange(125) == {'quarters': 5}
