
# find smallest element greater then the target
def letters_find(arr, target):
    start = 0
    end = len(arr) - 1

    while start <= end:
        # finding the mid
        mid = (start + end) // 2
        # target > mid so we no we need to find out the element in right hand side
        if target > arr[mid]:
            start = mid + 1

        else:
            end = mid - 1

    return arr[start % len(arr)]


letters = ["c", "f", "j"]
target = 'c'

ans = letters_find(letters, target)
print("The ans is : ", ans)
