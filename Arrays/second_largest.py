def getSecondOrderElements(a: [int]) -> [int]:
    # finding the first largest
    first_max = a[0]
    second_max = -1
    # finding the second largest
    first_min = a[0]
    second_min = -1

    length = len(a)

    for item in range(1, length):
        if a[item] > first_max:
            second_max = first_max
            first_max = a[item]

        if a[item] < first_min:
            second_min = first_min
            first_min = a[item]

    return [second_max, second_min]


nums = [4, 5, 3, 6, 1]
first_second_largest = getSecondOrderElements(nums)
print(first_second_largest)
