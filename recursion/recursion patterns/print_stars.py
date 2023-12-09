

def print_star_iterative(num):

    for row in range(num):
        for col in range(0, (num - row)):
            print("*", end=" ")

        print("")


def print_stars(row, col):
    if row == 0:
        return

    if col < row:
        print("*", end=" ")
        print_stars(row, col+1)
    else:
        print("")
        print_stars(row - 1, 0)


# print_star_iterative(5)
print_stars(5, 0)
