def drawPyramid(height):
    last_row_width = (2*(height-1)+1)
    for i in range(height):
        print(" "*(height-i-1)+"#"*(2*i + 1))
        
drawPyramid(8)


