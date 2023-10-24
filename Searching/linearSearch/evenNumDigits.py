

# first way to find out number of digits
def evenNumDigits(number):
    digits = len(str(number))
    return isPrime(digits)


# checking the number is prime no not
def isPrime(digits):
    if digits % 2 == 0:
        return True
    else:
        return False


# second way to count the number of digits
def evenNumberOfDigits2(number):

    # for the negative number
    if number < 0:
        number = number * -1

    # for the number is zero
    if number == 0:
        return 1

    count = 0
    while number != 0:
        count = count + 1
        number = number / 10

    return isPrime(count)


# find the even numbers of digits
nums = [11, 345, 2, 6, 7896]
count = 0
for index in range(len(nums)):
    if evenNumberOfDigits2(nums[index]):
        count = count + 1

print("The Count of Even number is : ", count)
