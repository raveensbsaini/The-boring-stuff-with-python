def mergeTwoLists(list1,list2):
    return_list = []
    idx1,idx2 = 0,0
    while (len(list1) + len(list2)) != 0:        
        if len(list1) > 0 and len(list2) > 0:
            if list1[-1] > list2[-1]:
                return_list.append(list1.pop())
            else:
                return_list.append(list2.pop())
        else:
            if len(list1) == 0 and len(list2) == 0:
                return return_list
            if len(list1) == 0 and len(list2) > 0:
                return_list.append(list2.pop())
            elif len(list2) == 0 and len(list1) > 0:
                return_list.append(list1.pop())
    return return_list[::-1]

assert mergeTwoLists([1, 3, 6], [5, 7, 8, 9]) == [1, 3, 5, 6, 7, 8, 9]
assert mergeTwoLists([1, 2, 3], [4, 5]) == [1, 2, 3, 4, 5]
assert mergeTwoLists([4, 5], [1, 2, 3]) == [1, 2, 3, 4, 5]
assert mergeTwoLists([2, 2, 2], [2, 2, 2]) == [2, 2, 2, 2, 2, 2]
assert mergeTwoLists([1, 2, 3], []) == [1, 2, 3]
assert mergeTwoLists([], [1, 2, 3]) == [1, 2, 3]
