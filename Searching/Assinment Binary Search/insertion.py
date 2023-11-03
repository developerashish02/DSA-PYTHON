def intersection(nums1, nums2):

    # sorted array
    nums1.sort()
    nums2.sort()

    i = 0
    j = 0
    ans = []

    while i < len(nums1) and j < len(nums2):

        # if intersection found
        if nums1[i] == nums2[j]:
            ans.append(nums1[i])
            i += 1
            j += 1
        # when nums[i] < nums[j] and we khow array is sorted then where is possible intersections of nums[i] is found on the right hand side

        elif nums1[i] < nums2[j]:
            i += 1

        else:
            j += 1

    # remove duplicate elements
    finalAns = []

    for index in range(len(ans)):

        if ans[index] not in finalAns:
            finalAns.append(ans[index])

    return finalAns


nums1 = [4, 9, 5],
nums2 = [9, 4, 9, 8, 4]

print(intersection(nums1, nums2))
