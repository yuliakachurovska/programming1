def find_gcd(m, n):
    while n != 0:
        m, n = n, m % n
    return m
def find_pairs(A, B):
    gcd_lcm_PQ = A * B
    pairs = set()
    for P in range(1, int(gcd_lcm_PQ**0.5) + 1):
        if gcd_lcm_PQ % P == 0:
            Q = gcd_lcm_PQ // P
            if find_gcd(P, Q) == A:
                pairs.add((P,Q))
                pairs.add((Q, P))
    return len(pairs)

A, B = [int(el) for el in input().split()]
print(find_pairs(A, B))