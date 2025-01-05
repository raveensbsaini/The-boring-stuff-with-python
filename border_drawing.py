def drawBorder(width,height):
    print("+"+"+".rjust(width-1,"-"))
    for i in range(height-2):
        print("|"+"|".rjust(width-1))
    print("+"+"+".rjust(width-1,"-"))

