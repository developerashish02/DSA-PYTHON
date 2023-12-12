
def quick_sort(nums, low, high):
    # base case
    if low >= high:
        return

    start = low
    end = high
    mid = (start + end) // 2
    pivot = nums[mid]

    while start <= end:
        # all elements less the pivot comes in left hand side
        while nums[start] < pivot:
            start += 1

        # all elements bigger then pivot comes in right hand side of the pivot

        while nums[end] > pivot:
            end -= 1

        # when the loop is over its means volition is happened than swap it
        # before swapping check array index start and end is index not out of bound

        if start <= end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

    quick_sort(nums, low, end)
    quick_sort(nums, start, high)


nums = [5, 4, 3, 2, 1]
quick_sort(nums, 0, len(nums) - 1)
print(nums)
