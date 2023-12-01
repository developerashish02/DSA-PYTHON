

def fib_number(num):
    # base condition
    if num <= 1:
        return num

    # recurrence relation
    return fib_number(num - 1) + fib_number(num - 2)


# main function
ans = fib_number(4)
print(ans)
