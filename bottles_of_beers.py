def song():
    string = """{a} bottles of beer on the wall,
{a} bottles of beer,
Take one down,
Pass it around,"""
    for i in range(99,1,-1):
        print(string.format(a=i))
    print("""1 bottle of beer on the wall,
1 bottle of beer,
Take one down,
Pass it around,"""
)
    print("No more bottles of beer on the wall!")
    return None
song()
