def rot13(string):
    return_string = ""
    for i,u in enumerate(string):
        if u.isalpha():
            if u.islower():
                a = "a"
                pass
            if u.isupper():
                a = "A"
            number = ord(u) - ord(a) +1
            reminder = (number + 13 ) % 26
            if reminder == 0:
                reminder = 26
            main_ascii_dec = reminder + ord(a) -1
            character = (chr(main_ascii_dec))
            return_string += character
        else:
            return_string += u
    return return_string
                       
assert rot13('Hello, world!') == 'Uryyb, jbeyq!'
assert rot13('Uryyb, jbeyq!') == 'Hello, world!'
assert rot13(rot13('Hello, world!')) == 'Hello, world!'
assert rot13('abcdefghijklmnopqrstuvwxyz') == 'nopqrstuvwxyzabcdefghijklm'
assert rot13('ABCDEFGHIJKLMNOPQRSTUVWXYZ') == 'NOPQRSTUVWXYZABCDEFGHIJKLM'
