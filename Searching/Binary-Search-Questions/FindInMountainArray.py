

def mountain(arr):
    start = 0
    end = len(arr) - 1

    while start < end:
        mid = (start + end) // 2

        # mid < mid + 1 then you are in the acceding order part so need to find the peak element in the array so you need to check on the right hand side because array is sorted on acceding order
        if arr[mid] < arr[mid + 1]:
            start = mid + 1
        # you are in the descending order part
        else:
            end = mid

    return start  # or end


def orderAgnosticBS(arr, target, start, end):
    # check array is acceding order or decreeing order
    isAes = False
    if arr[start] < arr[end]:
        isAes = True

    # binary search
    while start <= end:
        # finding the mid element
        mid = (start + end) // 2
        # check mid === target
        if arr[mid] == target:
            return mid
        if isAes:
            # target > mid element search on the right hand side
            if target > arr[mid]:
                start = mid + 1
            # target < mid element the search on the left hand side
            else:
                end = mid - 1
        else:
            if target < arr[mid]:
                start = mid + 1
            else:
                end = mid - 1

    return -1


arr = [1, 2, 3, 4, 5, 6, 4, 3, 2]
target = 3
peakIndex = mountain(arr)

firstPart = orderAgnosticBS(arr, target, 0, peakIndex)


if firstPart == -1:
    print(orderAgnosticBS(arr, target, peakIndex + 1, len(arr) - 1))


# print("Ans Is : ", firstPart)
# ans = orderAgnosticBS(arr, target, 0, 5)
# print(ans)
