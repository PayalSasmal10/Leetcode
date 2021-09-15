strg = "MoM"

if strg == strg[::-1]:
    print("Palindrome")

def palindrome(strng):
    if len(strng)<=1:
        return True
    else:
        if strng[0] == strng[-1]:
            return palindrome(strng[1:-1])
        else:
            return False

if palindrome("MOM") == True:
    print("This is Palindrome")

else:
    print("This is not Palindrome")

