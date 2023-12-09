
def selection_sort(arr, row, col, maxIndex):
    # base case
    if row == 0:
        return

    # body
    if col < row:
        # finding the maximum
        if arr[col] > arr[maxIndex]:
            selection_sort(arr, row, col + 1, col)
        else:
            selection_sort(arr, row, col + 1, maxIndex)

    else:
        arr[row - 1], arr[maxIndex] = arr[maxIndex], arr[row - 1]

        selection_sort(arr, row - 1, 0, 0)


# main function
arr = [4, 3, 2, 1]
length = len(arr)
selection_sort(arr, length, 0, 0)
print(arr)
