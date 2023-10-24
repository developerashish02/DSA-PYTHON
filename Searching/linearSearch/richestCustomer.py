def richestPerson(nums):
    currWelth = 0
    for row in range(len(nums)):
        maxWelth = 0
        for col in range(len(nums[row])):
            maxWelth = maxWelth + nums[row][col]

        if maxWelth > currWelth:
            currWelth = maxWelth

    return currWelth


nums = [
    [1, 5],
    [7, 3],
    [3, 5],
]

ans = richestPerson(nums)
print("The Max wealth is : ", ans)
