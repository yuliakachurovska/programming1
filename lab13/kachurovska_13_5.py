def even_numbers(file_name):
    with open(file_name, 'r') as file:    # користувалась методом відкриття файлів який ви нам показували
        numbers = [int(num) for num in file.read().split()]
        even = [num for num in numbers if num % 2 == 0]
        return len(even)

def squares_odd(file_name):
    with open(file_name, 'r') as file:
        numbers = [int(num) for num in file.read().split()]
        odd = [num for num in numbers if num % 2 != 0]
        squares_of_odd = [num ** 2 for num in odd]      # дивне формулювання, "кі-сть квадратів непарного числа", тут можна навіть
        return len(squares_of_odd)                              # прибрати обрахунок квадратів і просто порахувати кі-сть непарних чисел

def max_even_min_odd(file_name):
    with open(file_name, 'r') as file:
        numbers = [int(num) for num in file.read().split()]
        even = [num for num in numbers if num % 2 == 0]
        odd = [num for num in numbers if num % 2 != 0]
        return (max(even))-(min(odd))

def longest_ascending_sequence(file_name):
    with open(file_name, 'r') as file:
        numbers = [int(num) for num in file.read().split()]
        if not numbers:
            return 0

        current = 1
        max_length = 1
        for i in range(1, len(numbers)):
            if numbers[i] > numbers[i - 1]:
                current += 1
            else:
                max_length = max(max_length, current)
                current = 1

        return max(max_length, current)

file_name = 'my_file4.txt'
result1 = even_numbers(file_name)
result2 = squares_odd(file_name)
result3 = max_even_min_odd(file_name)
result4 = longest_ascending_sequence(file_name)
print(f"Кількість парних чисел у файлі: {result1}")
print(f"Кількість квадратів непарних чисел у файлі: {result2}")
print(f"Різниця між найбільшим парним і найменшим непарним числами в файлі: {result3}")
print(f"Кількість компонентів у найдовшій зростаючій послідовності: {result4}")