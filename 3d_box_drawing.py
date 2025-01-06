def drawBorder(width,height):
    print("+"+"+".rjust(width-1,"-"))
    for i in range(height-2):
        print("|"+"|".rjust(width-1))
    print("+"+"+".rjust(width-1,"-"))
def drawBox(size):
    if size < 1:
        return 
    a = "+"+"-"*(size*2)+"+"
    max_width = (size*2 -1) + len(a)
    print(" "*(size+1)+a)
    for i in range(size):
        print(" "*(size-i)+"/"+" "*(size*2)+"/"+" "*i + "|")
    print(a+" "*size + "+")
    for i in range(size):
        print("|"+" "*(size*2)+"|"+" "*(size-i-1)+"/")
    print(a)
drawBox(10)
