# DOES NOT WORK
# Issues:
#   - The current solution finds the first answer with the biggest multiples, not biggest value
#       Ex: The solution is in the low 900s. My algorithm will be satisfied before it finds this solution
#   - I don't need to be iterating through every number, just the 3 digit ones
# I should probably work backwords from the palindrome

def palindrome():
    x = 999
    while True:
        for y in range(999, x,-1):
            if str(x*y) == str(x*y)[::-1]:
                return x*y
        x -= 1

print(palindrome())