# why here i am using recursion because this problem breaks into smaller problem
# divide and conquer

from typing import List


def binary_search(nums: List[int], target: int, start: int, end: int) -> int:
    # base case
    if start > end:
        return -1

    mid = (start + end) // 2

    if nums[mid] == target:
        return mid

    if target > nums[mid]:
        return binary_search(nums, target, mid + 1, end)

    else:
        return binary_search(nums, target, start, mid - 1)


nums = [1, 2, 4, 5, 6, 7, 8]
target = 11
ans = binary_search(nums, target, 0, len(nums) - 1)
print("The Ans IS : ", ans)
