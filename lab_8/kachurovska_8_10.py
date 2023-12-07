def generate_permutations(n):
    digits = list(range(1, n + 1))
    result = []

    while True:
        # Додаємо поточну перестановку до результату
        result.append("".join(map(str, digits)))     # знайшла таку цікаву команду в чата gpt

        j = n - 2             # Знаходимо найбільший індекс j, для якого digits[j] < digits[j + 1]
        while j >= 0 and digits[j] >= digits[j + 1]:
            j -= 1
        if j == -1:         # Якщо такого індексу то всі перестановки створено
            break

        k = n - 1           # Знаходимо найбільший індекс k, для якого digits[k] > digits[j]
        while digits[k] <= digits[j]:
            k -= 1
        digits[j], digits[k] = digits[k], digits[j]
        digits[j + 1:] = reversed(digits[j + 1:])          # Перевертаємо підсписок від digits[j + 1] до кінця

    return result

n = int(input("Введіть натуральне число n: "))
permutations = generate_permutations(n)

for perm in permutations:
    print(perm)


# не зрозуміла як це зробити рекурсією навіть з підказками чату gpt. А ще спочатку прийшла ідея як це приблизно можна
# зробити за допомогою циклів, тому трішки допомоги від чата і вийшов такий код. Відповідь генерує правильну, але
# але на еолімп не проходить :(
