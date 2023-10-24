

def sqrt(num):
    # taking the count
    count = 1

    while count <= num:
        # getting the sqrt
        sqrt = count * count

        if sqrt == num:
            return int(count)

        if sqrt > num:
            return int(count - 1)

        count = count + 1
    return -1


# sqrt 2

def sqrt_2(num):

    if num == 0:
        return 0

    start = 1
    end = num

    while start <= end:
        # finding the mid element
        mid = (start + end) // 2
        # cal sqrt
        sqrt = mid * mid

        if sqrt == num:
            return mid

        if sqrt > num:
            end = mid - 1
        else:
            start = mid + 1

    return end


x = 28
print(sqrt_2(x))
