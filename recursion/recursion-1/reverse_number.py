def reverse_number_iterative(num):
    ans = 0

    while num != 0:
        lastDigit = num % 10
        ans = (ans * 10) + lastDigit
        num //= 10

    return ans


def reverse_number_recursive(num, rev=0):
    if num == 0:
        return rev

    last_digit = num % 10
    rev = (rev * 10) + last_digit
    return reverse_number_recursive(num // 10, rev)


# res = reverse_number_iterative(1234)
# print(res)
    
# recursive
ans = reverse_number_recursive(12345)
print(ans)
