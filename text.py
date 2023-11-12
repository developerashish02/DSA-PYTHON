

def search(nums, target, isLeft):
    start = 0
    end = len(nums) - 1
    count = 0

    while start <= end:
        mid = (start + end) // 2
        if nums[mid] == target:
            count += 1
            if isLeft:
                end = mid - 1

            else:
                start = mid + 1

        elif target > nums[mid]:
            start = mid + 1

        else:
            end = mid - 1

    return count


def countNumbers(nums, target):
    searchInLeft = search(nums, target, True)
    searchInRight = search(nums, target, False)
    ans = (searchInLeft + searchInRight) - 1

    if ans == - 1:
        ans += 1

    return ans


nums = [2, 4, 10, 10, 10, 10, 10, 10, 11, 12, 14, 14, 17, 19, 19]
target = 10


ans = countNumbers(nums, target)
print("The Count of numbers is ", ans)
