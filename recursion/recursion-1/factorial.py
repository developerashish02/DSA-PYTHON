def factorial_num(number):
    # base case
    if number == 1:
        return 1

    # recursive call
    return number + factorial_num(number - 1)


ans = factorial_num(5)
print(ans)
