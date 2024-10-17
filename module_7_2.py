def custom_write(file_name, strings):
    file = open(file_name, 'w', encoding='utf-8')
    strings_positions = {}
    num_str = 0
    str_start_byte = file.seek(0)
    for i in strings:
        file.write(i + '\n')
        num_str += 1
        key = (num_str, str_start_byte)
        strings_positions[key] = i
        str_start_byte = file.tell()
    file.close()
    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
