def F(n):
    if n % 10 > 0:
        return n % 10
    elif n == 0:
        return 0
    else:
        return F(n // 10)

def summa(p, q):
    return sum(F(n) for n in range(p, q + 1))

results = []
while True:
    p, q = [int(i) for i in input().split()]
    if p < 0 and q < 0:
        break
    results.append(summa(p, q))
for res in results:
    print(res)