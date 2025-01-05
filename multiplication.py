def fun():
    print("""  |  1  2  3  4  5  6  7  8  9  10
--+--------------------------------""")
    for i in range(1,11):
        print(f"{i}|".rjust(3),end="")
        for t in range(1,11):
            padding = 3
            if t == 10:
                padding = 4
            print(f"{i*t}".rjust(padding),end="")
        print()
            

fun()
