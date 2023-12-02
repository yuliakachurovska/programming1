def power(binary_res):
    if len(binary_res) == 0:
        return ""

    last_digit = int(binary_res[-1])
    if last_digit % 2 == 1:          # Рекурсія без останньої цифри, повертає значення в залежності від парності числа
        return power(binary_res[:-1]) + "SX"
    else:
        return power(binary_res[:-1]) + "S"

def decimal_to_binary(decimal):
    binary_res = ""

    while decimal > 0:
        remainder = decimal % 2
        binary_res = str(remainder) + binary_res
        decimal = decimal // 2

    return binary_res[1:]



decimal_numb = int(input())

binary_res = decimal_to_binary(decimal_numb)     # Перетворюємо в двійкову форму
power_res = power(binary_res)      # Правило швидкого піднесення
print(power_res)
