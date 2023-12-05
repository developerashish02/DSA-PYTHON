# Q Print The Number 1 to 5

def printNumber(n):
    # base condition for the problem
    if n == 5:
        print(n)
        return

    # function calling its self we called as a recursion
    print(n)
    printNumber(n+1)


# main function
printNumber(1)
