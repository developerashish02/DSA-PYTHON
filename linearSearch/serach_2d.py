
def searchIn2DArray(arr2D, target):
    for row in range(len(arr2D)):
        for col in range(len(arr2D[row])):
            if arr2D[row][col] == target:
                return [row, col]
    return [-1, -1]


arr2D = [
    [1, 2, 4],
    [5, 6, 7],
    [8, 9, 10]
]

target = 7
ans = searchIn2DArray(arr2D, target)
print(ans)
