#Note: This program doesn't work the best, but it does work.

def primeFactor(n):
    n = int(n)
    satisfied = False
    for i in range(2, n+1):
        if i is n:
            break
        if n % i == 0:
            primeFactor(n/i)
            break
    print(n)

primeFactor(600851475143)