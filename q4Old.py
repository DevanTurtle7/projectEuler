# DOES NOT WORK
# Issues:
#   - Doesn't account for ODD numbered palindromes

def palindrome():
    x = 0
    m = str(999**2)

    for i in range(int(m[0:int(len(m)/2)]), 99, -1):
        k = int(str(i) + str(i)[::-1])

        if k < int(m):
            for j in range(999, 99, -1):
                if k % j == 0 and len(str(k/j)) == 3:
                    print(j)
                    return k

print(palindrome())