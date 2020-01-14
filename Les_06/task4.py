"""Task 4:
Создать массив «Список покупок».
Каждый элемент массива является объектом, который содержит название продукта,
необходимое количество и куплен или нет.

Написать несколько функций для работы с таким массивом.
1. Вывод всего списка на экран таким образом, чтобы сначала шли некупленные продукты, а потом – купленные.
2. Добавление покупки в список.
   Учтите, что при добавлении покупки с уже существующим в списке продуктом,
   необходимо увеличивать количество в существующей покупке, а не добавлять новую.
3. Покупка продукта.
   Функция принимает название продукта и отмечает его как купленный.
"""

lis = [['Мандарин', 0.374, 'Куплен'],['Апельсин', 0.545, 'Не куплен'],['Мука', 2, 'Не куплен']]


def add_p(product):
    """Добавление покупки в список"""
    product[1] = float(product[1])
    res = True
    for i in lis:
        if product[0] in i and i[2] != 'Куплен':
            i[1] = round(i[1] + product[1], 2)
            res = False
        elif product[0] in i:
            i[1] = product[1]
            i[2] = 'Не куплен'
            res = False
    if res:
        product.append('Не куплен')
        lis.append(product)

def buy_product(name):
    """Принимает название продукта и отмечает его как купленный."""
    for i in lis:
        if name in i and i[2] != 'Куплен':
            i[2] = 'Куплен'
        elif name in i and i[2] == 'Куплен':
            print('Вы уже купили данных товар')

def print_p():
    """Вывод всего списка на экран"""
    for i in lis:
        i[2] = 'b' if i[2] == 'Куплен' else 'a'
        i.reverse()
    lis.sort()
    for i in lis:
        i.reverse()
        i[2] = 'Куплен' if i[2] == 'b' else 'Не куплен'
        print(i[0].ljust(max_len_p), str(i[1]).ljust(max_len_n), '-', i[2])


name_p = [i[0] for i in lis]
max_len_p = max([len(i) for i in name_p])
len_num = [str(i[1]) for i in lis]
max_len_n = max([len(i) for i in len_num])

print_p()
product = [i for i in input('Продукт для добавление в список(через запятую и пробел): ').split(', ')]
product_name = input('Введите продукт который хотите купить: ')
add_p(product)
buy_product(product_name)
print_p()



