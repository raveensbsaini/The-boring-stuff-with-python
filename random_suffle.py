import time

def random_int(a=0,b =1000000):
    a = time.time()
    a = str(a)
    a = a.split(".")
    a = int(a[-1])
    return a % b
    
def swap(list1,idx1,idx2):
    assert idx1 < len(list1)
    assert idx2 < len(list1)
    a = list1[idx1]
    list1[idx1] = list1[idx2]
    list1[idx2] = a
    return list1

def shuffle(list1):
    if len(list1) == 0:
        return list1
    for i,u in enumerate(list1):
        check = True
        while check:
            swap_idx = random_int(0,len(list1)-1)
            if swap_idx != i:
                list1 = swap(list1,i,swap_idx)
                check = False
                break
    return list1

            
        
for i in range(10):
    testData1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    shuffle(testData1)
    # Make sure the number of values hasn't changed:
    assert len(testData1) == 10
    # Make sure the order has changed:
    assert testData1 != [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # Make sure that when re-sorted, all the original values are there:
    assert sorted(testData1) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # Make sure an empty list shuffled remains empty:
testData2 = []
shuffle(testData2)
assert testData2 == []
