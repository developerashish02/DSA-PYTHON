

def binary_search(arr, target):
    # Iterate on array using two pointer start and end
    start = 0
    end = len(arr) - 1

    while start <= end:
        # finding the mid element
        mid = (start + end) // 2
        # check that middle element == target if yes we found are ans
        if target == arr[mid]:
            return mid
        # if target is > then mid element then ans on the right hand side
        elif target > arr[mid]:
            start = mid + 1

        # if target < mid element then ans is on the hand side
        else:
            end = mid - 1

    # This Line is executed means we dont have element in the array to return -1
    return -1


def rotatedBinarySearch(arr):
    # find the pivot element in the array
    start = 0
    end = len(arr) - 1

    while start <= end:
        # finding the mid
        mid = (start + end) // 2

        if mid < end and arr[mid] > arr[mid + 1]:
            return mid
        if mid > start and arr[mid] < arr[mid - 1]:
            return mid - 1

        if arr[start] >= arr[mid]:
            end = mid - 1
        else:
            start = mid + 1

    return -1


arr = [1, 2, 3, 4, 5, 6, 7]
target = 5
# 1 2 3 4 5 6 7  rotated = 0
# 7 2 3 4 5 6 1  rotated = 1
# 6 7 2 3 4 5 1 2   rotated = 2


pivot = rotatedBinarySearch(arr)

# if pivot is -1 then array is not rotated then do simple binary search
if pivot == -1:
    print(binary_search(arr, target, 0, len(arr) - 1))

if arr[pivot] == target:
    print(pivot)

# search on the first half
firstHalf = binary_search(arr, target, 0, pivot)

if firstHalf != -1:
    print(firstHalf)
