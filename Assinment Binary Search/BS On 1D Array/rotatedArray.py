

from typing import List


def findPivot(nums: List[int]) -> int:
    start = 0
    end = len(nums) - 1

    while start <= end:
        mid = (start + end) // 2
        # what is condition for the pivot
        if mid < end and nums[mid] > nums[mid + 1]:
            return mid

        # other condition for the ans
        if mid > start and nums[mid] < nums[mid - 1]:
            return mid - 1

        # if start is > then mid elements we know the start to mid element are smaller
        if nums[start] > nums[mid]:
            end = mid - 1

        else:
            start = mid + 1

    return -1


def binary_search(arr: List[int], target: int, start: int, end: int) -> int:

    while start <= end:
        # finding the mid element
        mid = (start + end) // 2
        # check that middle element == target if yes we found are ans
        if target == arr[mid]:
            return mid
        # if target is > then mid element then ans on the right hand side
        elif target > arr[mid]:
            start = mid + 1

        # if target < mid element then ans is on the hand side
        else:
            end = mid - 1

    # This Line is executed means we dont have element in the array to return -1
    return -1


def rbs(nums: List[int], target: int) -> int:
    pivot = findPivot(nums)

    if pivot == -1:
        return binary_search(nums, target, 0, len(nums) - 1)

    if nums[pivot] == target:
        return pivot

    if target >= nums[0]:
        return binary_search(nums, target, 0, pivot - 1)

    return binary_search(nums, target, pivot + 1, len(nums) - 1)


nums = [3, 4, 5, 6, 7, 0, 1, 2]
target = 10
ans = rbs(nums, target)
print(ans)
