def least_common_multiple(n):
    if n < 1:
        return 0

    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    def lcm(a, b):
        return a * b // gcd(a, b)

    result = 1
    for i in range(2, n + 1):
        result = lcm(result, i)
    return result

n = int(input())
result = least_common_multiple(n)
print(result)