def findDuplicate(nums):

    i = 0

    while i < len(nums):
        # find out the correct position
        correctPos = nums[i] - 1

        if nums[i] != nums[correctPos]:
            nums[correctPos], nums[i] = nums[i], nums[correctPos]

        else:
            i += 1

    for index in range(len(nums)):
        if nums[index] != index + 1:
            return nums[index]

    return -1


arr = [1, 3, 4, 2, 2]
ans = findDuplicate(arr)
print("In This List Duplicate element is : ", ans)
