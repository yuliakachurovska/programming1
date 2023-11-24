def convert_to_decimal(number, base, alphabet):
    decimal_number = 0
    power = 0

    while number > 0:
        digit = number % 10
        decimal_number += digit * (base ** power)
        number //= 10
        power += 1

    return decimal_number

def convert_to_base_n(decimal_number, base_n, alphabet):
    if decimal_number == 0:
        return alphabet[0]

    result = ''
    while decimal_number > 0:
        digit = decimal_number % base_n
        result = alphabet[digit] + result
        decimal_number //= base_n

    return result


m, n = [int(el) for el in input().split()]
number_m_base = int(input())


alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

decimal_number = convert_to_decimal(number_m_base, m, alphabet) # десяткова система
result = convert_to_base_n(decimal_number, n, alphabet) # n-та систему числення
print(result)