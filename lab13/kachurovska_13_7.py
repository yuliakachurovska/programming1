def find_longest_word(file_k):
    with open(file_k, 'r', encoding='utf-8') as file:
        words = file.read().split()
        longest_word = max(words, key=len)
        return longest_word

def count_words(file_k):
    with open(file_k, 'r', encoding='utf-8') as file:
        words = file.read().split()
        return len(words)

def clearing_the_list(file_k):
    with open(file_k, 'r', encoding='utf-8') as file:
        content = file.read()

    words = content.split()
    cleaned_words = [word for word in words if len(word) > 1]           # знайшла в інтернеті, що можна зробити ось
    cleaned_content = ' '.join(cleaned_words)                           # таким чином і так виходить швидше і компактніше
    with open('H.txt', 'w', encoding='utf-8') as output_file:     # переписуємо це в новий файл Н
        output_file.write(cleaned_content)

def delete_spaces(file_k):
    with open(file_k, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    cleaned_lines = [' '.join(line.split()) + '\n' for line in lines]

    with open('H.txt', 'a', encoding='utf-8') as output_file:
        output_file.write('\n')
        output_file.writelines(cleaned_lines)

#def
file_k = 'file.txt'
result_1 = find_longest_word(file_k)
result_2 = count_words(file_k)
clearing_the_list(file_k)
delete_spaces(file_k)
print(f"Найдовше слово у файлі: {result_1}")
print(f"Кількість слів в файлі: {result_2}")


# єдине, не зробила пункт е, дуже заплуталась з ним