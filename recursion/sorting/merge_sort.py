
def merge(nums1, nums2):
    ans = []
    i = 0
    j = 0

    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            ans.append(nums1[i])
            i += 1

        else:
            ans.append(nums2[j])
            j += 1

    while i < len(nums1):
        ans.append(nums1[i])
        i += 1

    while j < len(nums2):
        ans.append(nums2[j])
        j += 1

    return ans


def merge_sort(nums):
    # base case
    if len(nums) == 1:
        return nums

    # divide array into two parts
    mid = len(nums) // 2

    # recursion call
    firstHalf = merge_sort(nums[:mid])
    secondHalf = merge_sort(nums[mid:])

    return merge(firstHalf, secondHalf)


arr = [6, 5, 4, 3, 2, 1]
ans = merge_sort(arr)
print(arr)
print(ans)
