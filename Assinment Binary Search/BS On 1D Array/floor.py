
def floor(nums, x):
    start = 0
    end = len(nums) - 1

    while start <= end:
        mid = (start + end) // 2
        if nums[mid] == x:
            return mid

        elif x > nums[mid]:
            start = mid + 1

        else:
            end = mid - 1

    return [start, end]


nums = [3, 4, 7, 8, 8, 10]
x = 5
ans = floor(nums, x)
print("The Floor of number is : ", ans)
