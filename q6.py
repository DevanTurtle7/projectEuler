def sumSquares(n):
    if n == 1 or n == 0:
        return 1
    else:
        return (n ** 2) + sumSquares(n-1)

x = abs(sumSquares(100) - (sum(range(101)) ** 2))

print(x)