

def count_zeros_iterative(num):
    count = 0

    while num != 0:
        lastDigit = num % 10
        if lastDigit == 0:
            count += 1
        num //= 10

    return count


def count_zeros_recursively(num, count=0):
    # base case
    if num == 0:
        return count

    lastDigit = num % 10

    if lastDigit == 0:
        count += 1

    return count_zeros_recursively(num // 10, count)


# ans = count_zeros_iterative(1001230)
ans = count_zeros_recursively(100123)
print("The Count of zeros is : ", ans)
