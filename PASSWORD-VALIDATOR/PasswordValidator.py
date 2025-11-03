# password Validator
# password must be > greater than 8 characters in length
# must contain atleast 1 lowercase
# atleast on uppercase
# atleast on digit
# and atleast one special character excluding -, will not be counted as special character
# password must not have - and spaces

def password_validator(string):
    lower = 0
    upper = 0
    num = 0
    special = 0
    exclusion = 0

    length = len(string)

    for char in string:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1
        elif char.isdigit():
            num += 1
        elif not char.islower() and not char.isupper() and not char.isdigit():
            special += 1
        elif char.equal('-') or char ==" ":
            exclusion += 1


    print("this is lower", lower)
    print("this is upper", upper)
    print("this is num", num)
    print("this is special", special)
    print("this is exclustion", exclusion)



    if upper > 0 and lower > 0 and num > 0 and special > 0 and length > 8 and exclusion < 1:
        return True
    else:
        return False
    
print(password_validator("SYL5@-viatn"))
    
    

