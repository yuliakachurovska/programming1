def create_txt_file(sequence, file_name, num_lines):
        with open(file_name, 'w', encoding='utf-8') as file:
            lines = [sequence for k in range(num_lines)]
            file.write('\n'.join(lines))
        print(f"Файл '{file_name}' створено успішно.")

sequence = "привіт світ! :)"
file_name = 'output.txt'
num_lines = 40
create_txt_file(sequence, file_name, num_lines)
