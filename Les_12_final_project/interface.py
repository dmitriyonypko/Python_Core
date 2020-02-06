"""
[ ] Телефонный справочник.
Добавление контакта, удаление контакта, редактирование контакта.
Поиск по имени-фамилии, поиск по номеру, поиск по частично набранному номеру
"""


from class_contacts import *


cont = Contact('contacts.txt')


while True:
    option = int(input('\nВыберите действие:\n1 - Поиск\n2 - Добавить контакт\n3 - Удалить контакт\n4 - Редактировать контакт\n5 - Показать справочник\n6 - Выход\n----> '))
    if option not in range(1, 7):
        print('\nНекорректный ввод')
    elif option == 1:
        index_for_search = int(input('\nЧто ищем ?\n1 - id\n2 - Имя/Фамилию\n3 - Номер телефона\n4 - Компанию\n5 - E-mail\n----> '))
        if index_for_search not in range(1, 6):
            print('\nНекорректный ввод')
        else:
            data_for_search = input('\nВведите данные для поиска: ')
            if cont.search_contact(data_for_search, index_for_search-1):
                print(cont)
            else:
                print('\nПо Вашему запросу ничего не найдено.')
    elif option == 2:
        name = input('Введите имя и фамилию: ')
        number = input('Введите номер телефона: ')
        company = input('Введите название компании: ')
        email = input('Введите E-mail: ')
        if not number.isdigit():
            print('\nНекорректный ввод. Номер должен состоять только из цифр!\n')
        else:
            if cont.append_contact(name, number, company, email):
                print('\nДанные успешно добавлены')
            else:
                print('\nКонтакт уже есть в справочнике')
    elif option == 3:
        id_contact = int(input('Введите id контакта: '))
        if cont.del_contact(id_contact):
            print('\nКонтакт успешно удален')
        else:
            print('\nНекорректно введен id')
    elif option == 4:
        index_for_edit = int(input('Что редактируем ?\n1 - Имя/Фамилию\n2 - Номер телефона\n3 - Компанию\n4 - E-mail\n----> '))
        if index_for_edit not in range(1, 5):
            print('\nНекорректный ввод\n')
        else:
            id_contact = int(input('Введите id контакта: '))
            if cont.search_contact(str(id_contact), 0):
                data = input('Введите данные: ')
                if cont.edit_contact(id_contact, index_for_edit, data):
                    print('\nДанные успешно обновлены')
                else:
                    print('\nКонтакт уже есть в справочнике')
            else:
                print('\nНекорректно введен id')
    elif option == 5:
        cont.number_for_print = 0
        print(cont)
    elif option == 6:
        break
