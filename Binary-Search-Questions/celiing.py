

def celling(arr, target):
    start = 0
    end = len(arr) - 1

    if target > arr[end]:
        return -1

    while start <= end:
        # finding the mid
        mid = (start + end) // 2
        # check that target element == arr[mid]
        if target == arr[mid]:
            return mid
        # target > element then search on the right hand side
        elif target > arr[mid]:
            start = mid + 1
        # target < element then search on left hand side
        else:
            end = mid - 1

    # smallest no >= target

    return start


arr = [2, 3, 5, 9, 14, 16, 18]
target = 10
ans = celling(arr, target)
print("The smallest and >= target : ",  ans)
