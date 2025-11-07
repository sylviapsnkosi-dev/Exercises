# given a string check if a -- b, b is two spaces away from a
def char_cheker(mystring):

    text = mystring.lower()
    count = 0
    check_index = 0

    for x in range(0, len(text)):
        char = text[x]
        check_index = x + 3

        if char == 'a' and check_index <= len(text)-1:

            # check if we have b at check_index
            check_b = text[check_index]
            if check_b == 'b':
                count += 1
                check_index = 0
    return count

#test method
string = "ANNBAABKBLANTB"
print(char_cheker(string))

# notes: why are we subtracting 1 from the length of the whole string : if char == 'a' and check_index <= len(text)-1: