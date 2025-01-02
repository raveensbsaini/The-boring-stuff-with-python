def getTitleCase(string):
    return_string = ""
    check = True
    for i,u in enumerate(string):
        if u.isalpha() == False:
            check = True
            return_string += u
        else:
            if check:
                return_string += u.upper()
            else:
                return_string += u.lower()
            check = False
    return return_string

            

assert getTitleCase('Hello, world!') == 'Hello, World!'
assert getTitleCase('HELLO') == 'Hello'
assert getTitleCase('hello') == 'Hello'
assert getTitleCase('hElLo') == 'Hello'
assert getTitleCase('') == ''
assert getTitleCase('abc123xyz') == 'Abc123Xyz'
assert getTitleCase('cat dog RAT') == 'Cat Dog Rat'
assert getTitleCase('cat,dog,RAT') == 'Cat,Dog,Rat'
