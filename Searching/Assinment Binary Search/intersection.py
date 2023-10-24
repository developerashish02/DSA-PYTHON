
def intersection(num1, num2):
    ans = []
    ansIndex = 0

    for index1 in range(len(num1)):
        for index2 in range(len(num2)):
            if num1[index1] == num2[index2]:
                ans.insert(ansIndex,  num1[index1])
                ansIndex += 1
                num2[index2] = -19999999

    # return ans

    finalAns = []
    finalAnsIndex = 0

    for item in ans:
        if item not in finalAns:
            finalAns.append(item)

        return finalAns


nums1 = [1, 2, 2, 1]
nums2 = [2, 2]

print(intersection(nums1, nums2))
