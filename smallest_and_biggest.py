def getSmallest(l):
    if len(l) == 0:
        return None
    min = float("inf")
    for i in l:
        if i < min:
            min = i
    return min

assert getSmallest([1, 2, 3]) == 1
assert getSmallest([3, 2, 1]) == 1
assert getSmallest([28, 25, 42, 2, 28]) == 2
assert getSmallest([1]) == 1
assert getSmallest([]) == None
