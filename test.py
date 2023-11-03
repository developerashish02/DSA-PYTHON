def removeDuplicates(nums):

    i = 0
    j = 1

    while j < len(nums) - 1:
        if nums[i] == nums[j]:
            j += 1
        if nums[i] != nums[j]:
            nums[i+1] = nums[j]
            i += 1

    return i+1


nums = [1, 1, 2]
ans = removeDuplicates(nums)
print(nums, ans)
