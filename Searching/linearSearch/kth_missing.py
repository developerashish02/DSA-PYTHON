

def missingElement(arr, k):
    num = 1
    index = 0

    while index < len(arr) and k > 0:
        # lets check
        print(arr[index] == num)
        if arr[index] == num:
            index = index + 1
        else:
            k = k - 1

        num = num + 1

    while k > 0:
        num += 1
        k -= 1

    return num - 1


my_list = [1, 2, 3, 4],
k = 2
print(missingElement(my_list, k))
