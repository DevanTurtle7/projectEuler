def fib(n1, n2):
    if (n1 < 4 * 10 ** 6):
        s = n1+n2 if (n1+n2) % 2 is 0 else 0
        return s + fib(n1+n2, n1)
    else:
        return 0

print(fib(1,1))