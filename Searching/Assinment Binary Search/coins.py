

def printCoins(num):

    for row in range(1, num + 1):
        for col in range(1, row + 1):
            sum = row + col

            if sum == num:
                break
            print("🪙 ", end="")

        print("")


num = 5
printCoins(num)
