

def order_agnostic_bs(arr, target):
    # checking the arr is acceding order or deciding order
    start = 0
    end = len(arr) - 1
    isAsc = arr[start] < arr[end]

    while start <= end:
        # finding the middle element
        mid = (start + end) // 2

        if target == arr[mid]:
            return mid

        if isAsc:
            if target > arr[mid]:
                start = mid + 1
            else:
                end = mid - 1
        else:
            if target < arr[mid]:
                start = mid + 1
            else:
                end = mid - 1

    return -1


arr = [91, 82, 71, 61, 43, 22, 11, -11]
target = -11

ans = order_agnostic_bs(arr, target)
print("Ans The Index is : ", ans)
