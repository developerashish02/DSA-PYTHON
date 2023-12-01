

def count_numbers(s):
    # dictionary
    num = {}
    for char in s:
        if char in num:
            num[char] += 1

        else:
            num[char] = 1

    print(num)


s = '1234112456435'
count_numbers(s)
