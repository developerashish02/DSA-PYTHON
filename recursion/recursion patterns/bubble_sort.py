
def bubble_sort(nums, row, col):
    if row == 0:
        return

    if col < row:
        if nums[col] > nums[col + 1]:
            nums[col], nums[col + 1] = nums[col + 1], nums[col]
        bubble_sort(nums, row, col + 1)

    else:
        bubble_sort(nums, row - 1, 0)


arr = [4, 3, 2, 1]
length = len(arr) - 1
bubble_sort(arr, length, 0)
print(arr)
