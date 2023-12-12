

def printNumber(n):
    # base case
    if n == 1:
        print(n)
        return

    # body
    printNumber(n - 1)
    print(n)


num = int(input("Enter the number: "))
printNumber(num)
