def all_numbers(A, B):
    n = []
    for i in range(A, B + 1):
        if has_unique_digits(i):
            n.append(i)
    return n


def has_unique_digits(n):
    digits = set()
    for i in range(len(str(n))):
        digit = str(n)[i]
        if digit in digits:
            return False
        digits.add(digit)
    return True


A, B = [int(el) for el in input().split()]
result = all_numbers(A, B)
print(*result)