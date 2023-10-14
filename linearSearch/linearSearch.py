
# return the index
def linearSearch(arr, target):

    for i in range(len(arr)):
        if arr[i] == target:
            return i
        # This line execute means we dont have item in array
    return -1


#  return the element
def linearSearch2(arr, target):
    for index in range(len(arr)):
        if arr[index] == target:
            return arr[index]

    # this line is executed means we dont have element
    return -111111111


def linearSearch3(arr, index):
    for index in range(len(arr)):
        if arr[index] == target:
            return True

    # This line is executed means we dont have the element
    return False


arr = [11, 22, 33, 44, 66]
target = 11

ans = linearSearch3(arr, target)
print(ans)
