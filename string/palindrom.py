

def isPalindrome(name):

    start = 0
    end = len(name) - 1

    while start <= end:
        if name[start] != name[end]:
            return False
        else:
            start += 1
            end -= 1

    return True


name = "h"

isPal = isPalindrome(name)

print("IS Palindrome: ", isPal)
