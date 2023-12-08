def read_content_file(file_m):
    try:
        with open(file_m, 'r') as content_file:
            files = content_file.read().splitlines()
        return files
    except FileNotFoundError:
        print(f"Помилка: файл {file_m} не знайдено.")
        return None
    except IOError:
        print(f"Помилка: не вдалося прочитати файл {file_m}.")              # <== я ось таким чином прописала всі помилки, надіюсь це треба було робити
        return None

def read_numbers_in_file(file_m):
    try:
        with open(file_m, 'r') as numbers_file:
            numbers = []
            for line in numbers_file:
                try:
                    line_numbers = [float(num) for num in line.replace(',', '.').split()]
                    numbers.extend(line_numbers)                # додаю всі елементи до списку
                except ValueError:
                    print(f"Помилка: не вдалося конвертувати рядок '{line.strip()}' в дійсне число.")
                    return None
        return numbers
    except FileNotFoundError:
        print(f"Помилка: файл {file_m} не знайдено.")
        return None
    except IOError:
        print(f"Помилка: не вдалося прочитати файл {file_m}.")
        return None

def run_main():
    content_file_path = "content.txt"
    files = read_content_file(content_file_path)

    if files is not None:
        total_sum = 0
        for file_name in files:
            numbers = read_numbers_in_file(file_name)
            if numbers is not None:
                total_sum += sum(numbers)

        print(f"Загальна сума чисел з усіх файлів: {total_sum}")

run_main()

