def song():
    string = """{a} bottles of beer on the wall,
{a} bottles of beer,
Take one down,
Pass it around,"""
    for i in range(99,0,-1):
        print(string.format(a=i))
    print("No more bottles of beer on the wall!")
    return None
song()
