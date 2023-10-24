

def floor(arr, target):
    start = 0
    end = len(arr) - 1

    while start <= end:
        # finding the mid
        mid = (start + end) // 2
        # if we found the element
        if target == arr[mid]:
            return mid

        elif target > arr[mid]:
            start = mid + 1

        else:
            end = mid - 1

    # greatest no <= target
    return end


arr = [2, 3, 5, 9, 14, 16, 18]
target = 10
ans = floor(arr, target)
print("The greatest and <= target : ",  ans)
