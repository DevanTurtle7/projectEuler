#myString = str(input())

def isPalindrome(s):
    l = len(s)
    i1=i2=int()

    if l % 2 == 1:
        i1 = int((l - 1) / 2)
        i2 = int((l + 1) / 2)
    else:
        i1=i2=int(l/2)

    if s[0:i1] == s[i2:l][::-1]:
            return True
    
    return False

#print(isPalindrome(myString))

#work backwards
#find the largest palindromes and then find its factors.
#if the factors are 2 3-digit numbers than shes a go.