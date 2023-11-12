
def fibonacciNumber(num):
    # Base case
    if num < 2:
        return num

    # recursive functions
    return fibonacciNumber(num - 1) + fibonacciNumber(num - 2)


n = 4
ans = fibonacciNumber(n)
print("The Fibonacci number is",  ans)
