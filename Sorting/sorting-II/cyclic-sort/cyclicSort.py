

def cyclicSort(arr):
    i = 0
    while i < len(arr):
        # finding the correct position
        correct = arr[i] - 1  # 4

        # if is not its correct position then swap
        if arr[i] != arr[correct]:  # 5
            arr[i], arr[correct] = arr[correct], arr[i]

        # if its correct position then we continue
        else:
            i += 1


arr = [6, 5, 4, 3, 2, 1]
cyclicSort(arr)
print(arr)
