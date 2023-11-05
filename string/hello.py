
def singleNumber(nums):
    xor2 = 0
    for index in range(1, len(nums)):
        xor2 = nums[index - 1] ^ nums[index]
        # xor2 = xor2 ^ xor2
        print(xor2)


nums = [4, 1, 2, 1, 2]
singleNumber(nums)
