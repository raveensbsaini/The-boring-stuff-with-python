def bubbleSort(li):
    def swap(li,idx1,idx2):
        new = li[idx1]
        li[idx1] = li[idx2]
        li[idx2] = new
        return li
    for x in range(0,len(li)):
        for y in range(x+1,len(li)):
            if li[x] > li[y]:
                li = swap(li,x,y)
    return li
assert bubbleSort([2, 0, 4, 1, 3]) == [0, 1, 2, 3, 4]
assert bubbleSort([2, 2, 2, 2]) == [2, 2, 2, 2]
