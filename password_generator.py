import random
def generatePassword(length):
    if length < 12:
        length = 12
    special_characters =list("~!@#$%^&*()_+")
    characters = "".join(special_characters)
    for i in range(ord("a"),ord("z")+1):
        characters += chr(i)
    for i in range(ord("A"),ord("Z")+1):
            characters += chr(i)
    for i in range(ord("0"),ord("9")+1):
            characters += (chr(i))
    assert len(special_characters) == 13
    return_string = ""
    return_string += chr(random.randint(ord("a"),ord("z")))
    return_string += chr(random.randint(ord("A"),ord("Z")))
    return_string += chr(random.randint(ord("0"),ord("9")))
    return_string += special_characters[random.randint(0,12)]

    while len(return_string ) < length:
        return_string += characters[random.randint(0,len(characters)-1)]
    return return_string
    

pw = generatePassword(14)

assert len(pw) == 14
hasLowercase = False
hasUppercase = False
hasNumber = False
hasSpecial = False
for character in pw:
    if ord(character) in range(ord("a"),ord("z")+1) :
        hasLowercase = True
    if ord(character) in range(ord("A"),ord("Z")+1) :
            hasUppercase = True
    if ord(character) in range(ord("0"),ord("9")+1) :
            hasNumber = True
    if character in "~!@#$%^&*()_+" :
            hasSpecial = True
assert hasLowercase and hasUppercase and hasNumber and hasSpecial
