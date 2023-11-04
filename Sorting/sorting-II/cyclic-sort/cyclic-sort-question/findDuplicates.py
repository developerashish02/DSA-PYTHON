def findDuplicates(nums):

    i = 0

    while i < len(nums):
        correct = nums[i] - 1
        if nums[i] != nums[correct]:
            nums[i], nums[correct] = nums[correct], nums[i]

        else:
            i += 1

    ans = []

    for i in range(len(nums)):
        if i+1 != nums[i]:
            ans.append(nums[i])

    return ans


nums = [4, 3, 2, 7, 8, 2, 3, 1]
ans = findDuplicates(nums)
print("All The Duplicates Elements Is : ", ans)
