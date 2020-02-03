"""
[ ] Телефонный справочник.
Добавление контакта, удаление контакта, редактирование контакта.
Поиск по имени-фамилии, поиск по номеру, поиск по частично набранному номеру
"""
# TODO: После поиска не выводится вся таблица
# Из за метода __str__, там стоит фильтр. Если поиск проводился, то выводим результаты поиска.

from class_contacts import *


cont = Contact('contacts.txt')
print(cont)


while True:
    option = int(input('\nВыберите действие:\n1 - Поиск\n2 - Добавить контакт\n3 - Удалить контакт\n4 - Редактировать контакт\n5 - Показать справочник\n6 - Выход\n----> '))
    if option not in range(1, 7):
        print('\nНекорректный ввод')
    
    if option == 1:
        index_for_search = int(input('Что ищем ?\n1 - id\n2 - Имя/Фамилию\n3 - Номер телефона\n4 - Компанию\n5 - E-mail\n----> '))
        if index_for_search not in range(1, 6):
            print('Некорректный ввод\n')
        else:
            data_for_search = input('Введите данные для поиска: ')
            if index_for_search == 1:
                data_for_search = int(data_for_search)
            if len(cont.search_contact(data_for_search, index_for_search)) != 0:
                print(cont)
            else:
                print('По Вашему запросу ничего не найдено.')
    elif option == 2:
        name = input('Введите имя и фамилию: ')
        number = input('Введите номер телефона: ')
        company = input('Введите название компании: ')
        email = input('Введите E-mail: ')
        if not number.isdigit():
            print('Некорректный ввод. Номер должен состоять только из цифр!\n')
        else:
            if cont.append_contact(name, number, company, email):
                print('Данные успешно добавлены')
            else:
                print('Контакт уже есть в справочнике')
    elif option == 3:
        id_contact = int(input('Введите id контакта: '))
        if cont.del_contact(id_contact):
            print('Контакт успешно удален')
        else:
            print('Некорректно введен id')
    elif option == 4:
        index_for_edit = int(input('Что редактируем ?\n1 - Имя/Фамилию\n2 - Номер телефона\n3 - Компанию\n4 - E-mail\n----> '))
        if index_for_edit not in range(1, 5):
            print('Некорректный ввод\n')
        else:
            id_contact = int(input('Введите id контакта: '))
            data = input('Введите данные: ')
            if cont.edit_contact(id_contact, index_for_edit, data):
                print('Данные успешно обновлены')
            else:
                print('Некорректно введен id')
    elif option == 5:
        print(cont)
    elif option == 6:
        break
