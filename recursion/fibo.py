

def fibonacci(num):
    # base case
    if num < 2:
        return num

    # recurrence relation

    return fibonacci(num - 1) + fibonacci(num - 2)


num = 4
ans = fibonacci(num)
# print('''The Forth Fibb num is : {ans}''')
print("The ans is 4th fibo num : ", ans)
