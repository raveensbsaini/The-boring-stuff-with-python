def getChessSquareColor(row,col):
    row = row -1
    col = col -1
    if row > 7 or row < 0 or col > 7 or col < 0 :
        return ""
    if row%2 == 0:
        if col %2 == 0:
            return 'white'
        elif col % 2 == 1:
            return "black"
    elif row % 2 == 1:
        if col %2 == 0:
            return "black"
        elif col % 2 == 1:
            return  "white"
assert getChessSquareColor(1, 1) == 'white'
assert getChessSquareColor(2, 1) == 'black'
assert getChessSquareColor(1, 2) == 'black'
assert getChessSquareColor(8, 8) == 'white'
assert getChessSquareColor(0, 8) == ''
assert getChessSquareColor(2, 9) == ''
        
