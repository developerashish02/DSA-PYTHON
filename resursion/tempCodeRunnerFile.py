
def print_number(num):
    # base condition
    if num == 5:
        print(num)
        return

    # print number
    print(num)

    # recursion call
    print_number(num + 1)


# main function
print_number(1)
