def input_sequence():
    runtime_error_count = 0
    type_error_count = 0
    value_error_count = 0

    while True:
        try:
            user_input = input("Введіть число або слово 'досить': ")    # Користувач може в будь якому вигляді ввести слово і воно буде зараховане
            if user_input.lower() == 'досить':
                break

            number = int(user_input)
            if number > 9:
                raise RuntimeError("Число більше за 9")
            elif number < 0:
                raise TypeError("Число менше за 0")

            if number != int(user_input):
                raise ValueError("Введено не ціле число")

        except RuntimeError as run_er:
            print(run_er)
            runtime_error_count += 1
        except TypeError as type_er:
            print(type_er)
            type_error_count += 1
        except ValueError as value_er:
            print(value_er)
            value_error_count += 1

    print("\nКількість виключень типу RuntimeError:", runtime_error_count)
    print("Кількість виключень типу TypeError:", type_error_count)
    print("Кількість виключень типу ValueError:", value_error_count)


input_sequence()
