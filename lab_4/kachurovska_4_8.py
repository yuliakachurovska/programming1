n = int(input())
m = []
for i in range(1, n):
    k = i ** 3
    if k < n:
        m.append(k)
    else:
        break
print(*m)
