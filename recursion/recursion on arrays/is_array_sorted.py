

def is_sorted(arr, index):
    # base condition
    if index == len(arr) - 1:
        return True

    # recusance relation
    return arr[index] < arr[index + 1] and is_sorted(arr, index+1)


arr = [1, 2, 3, 11, 7, 4, 5]
ans = is_sorted(arr, 0)
print(ans)
