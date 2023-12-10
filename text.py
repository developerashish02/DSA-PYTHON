from typing import List


def maximumProduct(self, nums: List[int]) -> int:
    # first three max
    firstMax = float("-inf")
    secondMax = float("-inf")
    thirdMax = float("-inf")
    # first two min
    firstMin = float("inf")
    secondMin = float("inf")

    for item in nums:
        # Find out the first max
        if item >= firstMax:
            thirdMax = secondMax
            secondMax = firstMax
            firstMax = item

        # Find out the second max
        elif item >= secondMax and item < firstMax:
            thirdMax = secondMax
            secondMax = item

        elif item >= thirdMax and item < secondMax and item < firstMax:
            thirdMax = item

        # Find out the first min
        if item <= firstMin:
            secondMin = firstMin
            firstMin = item

        # Find out the second min
        elif item <= secondMin and item < firstMin:
            secondMin = item

    return max((firstMax * secondMax * thirdMax), (firstMin * secondMin * firstMax))
