def print_n_to_one(number):
    # base condition
    if number == 1:
        print(number)
        return

    # recursive call
    print_n_to_one(number - 1)

    # body
    print(number)

    ans = print_n_to_one(5)
    print(ans)
