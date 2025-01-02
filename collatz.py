def collatz(n):
    if n < 1:
        return []
    assert isinstance(n,int) 
    return_list = [n]
    while return_list[-1] != 1:
        last = return_list[-1]
        if last % 2 == 0:
            return_list.append(last/2)
        elif last % 2 == 1:
            return_list.append(3*last + 1)
    return return_list
assert collatz(0) == []
assert collatz(10) == [10, 5, 16, 8, 4, 2, 1]
assert collatz(11) == [11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
assert collatz(12) == [12, 6, 3, 10, 5, 16, 8, 4, 2, 1]
        
