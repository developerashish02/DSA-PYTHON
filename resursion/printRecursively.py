

def printNumber(num):
    # Base condition
    if num == 5:
        print(num)
        return

    print(num)

    printNumber(num + 1)


printNumber(1)
