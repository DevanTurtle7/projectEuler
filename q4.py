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

#divide n by 2 and make it an int
#keep lower this until

# i have no idea what im doing :)

def factors(n):
    f = []

    print("n is: " + str(n))

    if n > 2:
        i = int(n/2)

        while n%i != 0:
            print(i)
            i-=1
        
        f.append(i)

        r = factors(i)
        for x in range(0, len(r)):
            f.append(r[x])
    
    if n%3 == 0 and int(n/3) not in f:
        f.append(int(n/3))
    
    return f

test = factors(int(input()))
print(test)
print("There are " + str(len(test)) + " factors")