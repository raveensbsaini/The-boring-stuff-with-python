def median(list1):
    list1.sort()
    if len(list1) < 1:
        return None
    if len(list1) % 2 == 0:
        idx1 = len(list1)//2
        idx2 = idx1 -1
        return (list1[idx1] + list1[idx2]) / 2
    else:
        return list1[len(list1)//2]
    
assert median([]) == None
assert median([1, 2, 3]) == 2
assert median([3, 7, 10, 4, 1, 9, 6, 5, 2, 8]) == 5.5
assert median([3, 7, 10, 4, 1, 9, 6, 2, 8]) == 6
import random
random.seed(42)
testData = [3, 7, 10, 4, 1, 9, 6, 2, 8]
for i in range(1000):
    random.shuffle(testData)
    assert median(testData) == 6
