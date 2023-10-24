
def findMin(arr):

    if len(arr) == 0:
        return -111111111

    min = arr[0]

    for index in range(1, len(arr)):
        if arr[index] < min:
            min = arr[index]

    return min


arr = [-11, 22, 43, 21, 91]
ans = findMin(arr)
print(ans)
