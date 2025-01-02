def calculateSum(list1):
    return_ans = 0
    for i,u in enumerate(list1):
        if isinstance(u,float) or isinstance(u,int):
            return_ans += u
        else:
            assert False
    return return_ans
def calculateProduct(list1):
    return_ans = 1
    for i,u in enumerate(list1):
        if isinstance(u,float) or isinstance(u,int):
            return_ans *= u
        else:
            assert False
    return return_ans
        
assert calculateSum([]) == 0
# print(calculateSum([2, 4, 6, 8, 10]) )
assert calculateSum([2, 4, 6, 8, 10]) == 30
assert calculateProduct([]) == 1
assert calculateProduct([2, 4, 6, 8, 10]) == 3840
