

def bubble_sort(nums):

    isSwapped = False

    for i in range(len(nums)):

        for j in range(1, len(nums) - i):

            if nums[j] < nums[j - 1]:
                # then only swapped
                temp = nums[j - 1]
                nums[j - 1] = nums[j]
                nums[j] = temp
                isSwapped = True

        # when the J value is navar swapped means array is already sorted
        if not isSwapped:
            break

    return nums


nums = []

print(bubble_sort(nums))
