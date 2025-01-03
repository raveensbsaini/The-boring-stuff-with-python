def mode(list1):
    d = {}
    number,frequency = None,0
    for i,u in enumerate(list1):
        if u in d:
            d[u] += 1
            if d[u] > frequency:
                number = u
                frequency = d[u]

        else:
            d[u] = 1
            if d[u] > frequency:
                            number = u
                            frequency = d[u]
    return number


assert mode([]) == None
assert mode([1, 2, 3, 4, 4]) == 4
assert mode([1, 1, 2, 3, 4]) == 1
import random
random.seed(42)
testData = [1, 2, 3, 4, 4]
for i in range(1000):
    random.shuffle(testData)
    assert mode(testData) == 4
