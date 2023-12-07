alphabet = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def convert_to_13(number):
    if number == 0:
        return '0'

    str_base_13 = ""

    while number > 0:
        remainder = number % 13
        str_base_13 = alphabet[remainder] + str_base_13
        number //= 13

    return str_base_13

number = int(input())
result_13 = convert_to_13(number)
print(result_13)