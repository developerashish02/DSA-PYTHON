

def printLargestOptimal(nums):
    firstLargest = nums[0]
    secondLargest = -1

    for ele in nums:
        if ele > firstLargest:
            secondLargest = firstLargest
            firstLargest = ele

        elif ele > secondLargest and ele < firstLargest:
            secondLargest = ele

    return secondLargest

# Time complexity is 2 0(n) need tow passes to find out the largest
# space o(1)


def printLargestBrut(nums):
    # find out the largest
    largest = nums[0]
    secondLargest = -1

    for ele in nums:
        if ele > largest:
            largest = ele

    for i in range(len(nums)):
        if nums[i] > secondLargest and nums[i] != largest:
            secondLargest = nums[i]

    return secondLargest
# Time complexity is N ^ 2
# space complexity is o (1)


def printLargest(nums):
    nums.sort()
    length = len(nums) - 1

    if len(nums) == 0:
        return 0

    largest = nums[length]

    for i in range(len(nums) - 1, -1, -1):
        if nums[i] != largest:
            return nums[i]

    return -1


nums = [5, 5, 5, 5, 5]
ans = printLargestOptimal(nums)
print('the second largest is ', ans)
