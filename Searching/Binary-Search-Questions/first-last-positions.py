
def findIndex(arr, target, isFirstIndex):
    start = 0
    end = len(arr) - 1
    ans = -1

    while start <= end:
        # finding the mid element
        mid = (start + end) // 2

        # check middle element is === target element
        if target == arr[mid]:
            # possible ans
            ans = mid
            if isFirstIndex:
                # need to the search on the left hand side
                end = mid - 1
            else:
                start = mid + 1
        # target >= target element so we know the element on  right hand side
        elif target > arr[mid]:
            start = mid + 1

        else:
            end = mid - 1

    return ans


def findFirstAndLastIndex(arr, target):

    ans = [-1, -1]

    start = findIndex(arr, target, True)
    end = findIndex(arr, target, False)

    ans[0] = start
    ans[1] = end

    return ans


arr = [5, 7, 7, 7, 8, 8]
target = 7

ans = findFirstAndLastIndex(arr, target)
print("The first and last index of the target: ", ans)
