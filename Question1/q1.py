n = 1
s = 0

while n*5 < 1000 or n*3 < 1000:
    if n*3 < 1000:
        s += n*3
    
    if n*5 < 1000 and (n*5) % 3 is not 0: #make sure theres no repeats
        s += n*5
    
    n += 1

print(s)