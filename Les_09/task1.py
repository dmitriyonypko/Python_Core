

book = input('Введите данные в формате(Название*Автор*Жанр*Год издания*Издательство*Цена): ')
nameFile = 'DB.txt'


def table_DB(nameDB):
    """Cчитывать файл и возвращать пользователю в строку таблицу со всем содержимым файла."""
    with open(nameDB, encoding='utf-8') as fileDB:
        list_lines = [line.strip().split('*') for line in fileDB]
    # Создаем словарь {индекс: max длина слова}
    len_words = {}
    for line in list_lines:
        for index, word in enumerate(line):
            len_word = len(word)
            if index not in len_words:
                len_words[index] = len_word
            if len_words[index] < len_word:
                len_words[index] = len_word
    # Записываем таблицу в строку
    count_char = '\n' + '-' * (sum(len_words.values()) + len(list_lines[0]) * 3 - 1) + '\n'
    result_table = ''
    for line in list_lines:
        result_table += count_char
        for index, word in enumerate(line):
            result_table += word.ljust(len_words[index]) + ' | '
    result_table += count_char
    return result_table

def add_data(nameFile, data):
    """Добавляет в файл данные о новых книгах."""
    with open(nameFile, 'r', encoding='utf-8') as file:
        lis = [line.strip().split("*") for line in file]
    
    for i in lis:
        del i[0]
        del i[-1]
    
    list_data = data.split("*")
    del list_data[-1]
    
    if list_data in lis:
        print('Данная книга есть в списке!')
    else:
        with open(nameFile, 'a', encoding='utf-8') as file: 
            file.write('\n' + str(len(lis) - 1) + "*" + data)


print(table_DB(nameFile))
add_data(nameFile, book1)
print(table_DB(nameFile))
