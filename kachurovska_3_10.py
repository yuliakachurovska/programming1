n = int(input())
i = 0
b = 0
while n:
    d = n % 10
    if d & 0x01:
        d -= 1 
    else:
        d += 1
    b += d * 10**i
    n //= 10
    i+=1
print(b)