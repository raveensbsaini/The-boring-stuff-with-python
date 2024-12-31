def writeToFile(filename,text):
    with open(filename,"w") as file:
        file.write(text)
def appendToFile(filename,text):
    with open(filename,"a") as file:
        file.write(text)
def readFromFile(filename):
    with open(filename,"r") as file:
        file = file.read()
    return file
writeToFile('greet.txt', 'Hello!\n')
appendToFile('greet.txt', 'Goodbye!\n')
assert readFromFile('greet.txt') == 'Hello!\nGoodbye!\n'

    
