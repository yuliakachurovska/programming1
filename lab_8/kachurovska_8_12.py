def fast_power(x, y, mod):
    if y == 0:
        return 1
    if y % 2 == 1:
        return (x * fast_power(x * x % mod, y // 2, mod)) % mod
    return fast_power(x * x % mod, y // 2, mod)

case_number = 1
while True:
    k, n, t = map(int, input().split())
    if k + n + t == 0:
        break
    mod_value = 10 ** t
    result = fast_power(k % mod_value, n, mod_value)
    print(f"Case #{case_number}: {result}")
    case_number += 1

# трішки чат допоміг, зовсім трішечки :)