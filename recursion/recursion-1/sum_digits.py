def sum_digits(num):
    # base case
    if num == 0:
        return 0

    # body of the functions
    lastDigit = num % 10

    # recurrence relation
    return lastDigit + sum_digits(num // 10)


ans = sum_digits(1687)
print(ans)
