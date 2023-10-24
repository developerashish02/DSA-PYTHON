
# simple binary search

def binarySearch(arr, target, start, end):

    while start <= end:
        # finding the mid element
        mid = (start + end) // 2

        # check mid element is your target element
        if target == arr[mid]:
            return mid
        # target > mid element then ans is lies on the right hand side
        elif target > arr[mid]:
            start = mid + 1
        else:
            end = mid - 1

    return -1


def findingTheRange(arr, target):
    # we found the range we start with box size of 2 and increase exponentially
    start = 0
    end = 1

    # the condition the target element lies in our range

    while target > arr[end]:
        # my new start
        temp = end + 1
        # my new end
        # previous end + sizeOfTheBox * 2
        end = end + (end - start + 1) * 2
        start = temp

    # here now the target element is lies on the range
    return binarySearch(arr, target, start, end)


# giving the infinite array and we need to the find the target
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 89, 100]
target = 11

ans = findingTheRange(arr, target)
print(ans)
