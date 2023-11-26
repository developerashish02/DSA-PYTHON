
def isPalindrome(string):
    start = 0
    end = len(string) - 1

    while start <= end:
        if string[start] != string[end]:
            return False
        start += 1
        end -= 1

    return True


# main function
string = input("Enter The String : ")
ans = isPalindrome(string)

if ans:
    print("String is palindrome: ")

else:
    print("String is not palindrome: ")
