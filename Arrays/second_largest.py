
def brut_force_second_largest(nums):
    # sort the array
    nums.sort()
    # print(nums)
    # lets checking for the largest element
    length = len(nums) - 1
    second_largest = nums[length]

    # checking for the second largest
    for i in range(length - 1, -1, -1):
        if nums[i] != second_largest:
            second_largest = nums[i]
            break

    # return second largest
    return second_largest

    # Time Complexity - N LOG N
    # Space Complexly - o (1)


def better_second_largest(nums):
    length = len(nums)

    if length < 0:
        return "Nums is empty"

    # assume first element in largest
    largest = nums[0]

    # finding the largest
    for item in nums:
        if item > largest:
            largest = item

    # second pass find out second largest
    second_largest = -1  # assume array do not have negative values
    for item in nums:
        if item > second_largest and item < largest:
            second_largest = item
    # return ans
    return second_largest

    # Time Complexity - O(2N) because Its taking two pass
    # Space Complexity - O(1)


def optimal_second_largest(nums):
    largest = nums[0]
    second_largest = -1

    for item in nums:
        if item > largest:
            second_largest = largest
            largest = item

        if item > second_largest and item < largest:
            second_largest = item

    return second_largest

    # Time complexity - O(N)
    # Space complexity - O (1)


nums = [1, 2, 3, 4, 5]
# ans = brut_force_second_largest(nums)
# ans = better_second_largest(nums)
ans = optimal_second_largest(nums)
print(ans)
