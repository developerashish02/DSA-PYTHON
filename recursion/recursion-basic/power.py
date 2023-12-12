def power(x, n):
    # Bace case
    if n == 0:
        return 1

    # recursive call
    ans = power(x, n - 1)

    return x * ans


a = 5
b = 5
ans = power(a, b)
