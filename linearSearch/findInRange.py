
def searchInRange(arr, start, end, target):
    for item in range(start, end):
        if arr[item] == target:
            return True
    return False


arr = [11, 21, 3, 1, 55, 12]
start = 1
end = 4
target = 11

ans = searchInRange(arr, start, end, target)
print(ans)
