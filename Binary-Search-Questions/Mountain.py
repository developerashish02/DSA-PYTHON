

def mountain(arr):
    start = 0
    end = len(arr) - 1

    while (start < end):
        # finding the mid element
        mid = (start + end) // 2

        # check mid > mid + 1 then we in the decreasing part of the array
        if arr[mid] > arr[mid + 1]:
            end = mid
        # if mid < mid + 1 so we in the increasing part of the array

        else:
            start = mid + 1

    return start  # return end or start


arr = [1, 2, 3, 4, 5, 11, 4, 3, 2]
ans = mountain(arr)
print("The Peak Index in mountain array: ", ans)
