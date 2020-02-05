"""
[ ] Телефонный справочник.
Добавление контакта, удаление контакта, редактирование контакта.
Поиск по имени-фамилии, поиск по номеру, поиск по частично набранному номеру
"""


class Contact:
    
    def __init__(self, file_name):
        self.file_name = file_name
        self.header = []
        self.body = []
        self.searched_list = []
        self.number_for_print = 0
    
    def __str__(self):
        if self.number_for_print:
            return f'{self.__table_for_print(self.header, self.searched_list)}'
        else:
            self.__read_file()
            return f'{self.__table_for_print(self.header, self.body)}'
    
    def __table_for_print(self, header, body):
        """Делаем из двух списков таблицу для печати."""
        
        list_lines = []
        list_lines.append(header)
        list_lines.extend(body)
        
        # Создаем словарь {индекс: max длина слова}
        len_words = {}
        for line in list_lines:
            for index, word in enumerate(line):
                len_word = len(str(word))
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
                result_table += str(word).ljust(len_words[index]) + ' | '
        result_table += count_char
        
        return result_table
    
    def __read_file(self):
        """Считывает данные из файла."""
        with open(self.file_name, 'r', encoding='utf-8') as file:
            self.header = file.readline()
            self.header = self.header.strip().split(',')
            self.body = [line.strip().split(',') for line in file]
    
    def __write_data(self):
        """Записывает данные в файл."""
        self.body = list(map(','.join ,self.body))
        with open(self.file_name, 'w', encoding='utf-8') as file:
            file.write(f"{','.join(self.header)}\n")
            file.write('\n'.join(self.body))
    
    def __edit_id(self, id_contact):
        """Пересчитываем id. """
        for item in self.body[id_contact:]:
            item[0] = str(id_contact + 1)
            id_contact += 1
    
    def search_contact(self, data_for_search, index_for_search=5):
        """Возвращает список с найденным контактом или возвращает пустой список."""
        self.number_for_print = 1
        self.searched_list = []
        self.__read_file
        
        if index_for_search == 4:
            index = 3
        elif type(data_for_search) is int:
            index = 0
        elif data_for_search.isdigit():
            index = 2
        elif index_for_search == 5:
            index = 4
        else:
            index = 1
        
        for line in self.body:
            if index == 0:
                if int(data_for_search) == int(line[index]):
                    self.searched_list.append(line)
            elif data_for_search.lower() in line[index].lower():
                self.searched_list.append(line)
        
        return self.searched_list
    
    def append_contact(self, name='-', phone_number='0', company='-', email='-'):
        """Добавляем контакт если в справочнике нет имени, телефона, email"""
        # Не работает проверка!!!!
        search_name = len(self.search_contact(name))
        search_number = len(self.search_contact(phone_number))
        search_email = len(self.search_contact(email, 5))
        self.searched_list = []
        self.new_id = len(self.body) + 1
        
        if search_name and search_number and search_email:
            return False
        else:
            with open(self.file_name, 'a', encoding='utf-8') as file:
                file.write(f'\n{self.new_id},{name},{phone_number},{company},{email}')
            return True
    
    def del_contact(self, id_contact):
        """Удаляет контакт по заданому id."""
        id_contact = int(id_contact)
        if id_contact not in range(1, len(self.body) + 1):
            return False
        
        self.__read_file()
        
        del self.body[id_contact - 1]
        self.__edit_id(id_contact - 1)
        self.__write_data()
        
        return True
    
    def edit_contact(self, id_contact, index_for_edit, data):
        """Рудактирует контакт."""
        if id_contact not in range(1, len(self.body) + 1):
            return False
        
        # Проверяем не будет ли дублирующих строк в файле. Если будут, вернуть False
        search_data = self.search_contact(data)
        if search_data:
            new_line = []
            new_line.extend(self.body[id_contact - 1])
            new_line[index_for_edit] = data
            for line in search_data:
                if line[1:] == new_line[1:]:
                    return False
        
        self.body[id_contact - 1][index_for_edit] = data
        self.__write_data()
        return True
