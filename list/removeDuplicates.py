def removeDuplicates(nums) -> int:

    i = 0
    j = 0
    uniqueElements = 1
    length = len(nums) - 1

    while i <= length and j <= length:
        if nums[i] == nums[j]:
            j += 1

        elif nums[i] != nums[j]:
            nums[i+1] = nums[j]
            i += 1
            uniqueElements += 1

    return uniqueElements


nums = [1, 2]
ans = removeDuplicates(nums)
print(ans)
