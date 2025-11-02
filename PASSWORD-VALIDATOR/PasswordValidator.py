# password Validator
def password_validator(string):
    lower = 0
    upper = 0
    num = 0
    special = 0
    
    length = len(string)

    for char in string:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1
        elif char.isdigit():
            num += 1
        elif not char.islower() and not char.isupper() and not char.isdigit() and char not in ['-']:
            special += 1


    if upper > 0 and lower > 0 and num > 0 and special > 0 and length > 8:
        return True
    else:
        return False
    
    

