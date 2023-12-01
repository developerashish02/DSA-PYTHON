

def rec_binary_search(arr, target, start, end):
    # base case
    if start > end:
        return - 1

    # body functions
    mid = (start + end) // 2

    # if we found the ans
    if arr[mid] == target:
        return mid
    # if target > mid search on the right hand side
    elif target > arr[mid]:
        return rec_binary_search(arr, target, mid + 1, end)

    # if target < mid search on the left hand side
    else:
        return rec_binary_search(arr, target, start, mid - 1)


arr = [1, 2, 3, 4, 5, 6, 7, 8]
target = 5
# main function
ans = rec_binary_search(arr, target, 0, len(arr) - 1)
print(ans)
