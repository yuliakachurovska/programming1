n = int(input())
m = 1

for d in range(2, n // 2 + 1):
    if n % d == 0:
        m = d

print(m)