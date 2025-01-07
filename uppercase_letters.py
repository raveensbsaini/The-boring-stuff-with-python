def getUppercase(string):
    return_string = ""
    for i,u in enumerate(string):
        if u.isalpha() and u.islower():
            return_string += chr( ord(u)- ( ord("a")-ord("A") ))
        else:
            return_string += u
    return return_string
        
assert getUppercase('Hello') == 'HELLO'
assert getUppercase('hello') == 'HELLO'
assert getUppercase('HELLO') == 'HELLO'
assert getUppercase('Hello, world!') == 'HELLO, WORLD!'
assert getUppercase('goodbye 123!') == 'GOODBYE 123!'
assert getUppercase('12345') == '12345'
assert getUppercase('') == ''
