def printHandshakes(list1):
    n = len(list1)
    for i,u in enumerate(list1):
        if i <= len(list1) -1-1:
            for i1,u1 in enumerate(list1[i+1:]):
                print(u,"shakes hands with ",u1)

    return (n*(n-1))/2

assert printHandshakes(['Alice', 'Bob']) == 1
assert printHandshakes(['Alice', 'Bob', 'Carol']) == 3
assert printHandshakes(['Alice', 'Bob', 'Carol', 'David']) == 6
