"""Task 5:

Создать массив, описывающий чек в магазине.
Каждый элемент массива состоит из названия товара,
количества и цены за единицу товара. Написать следующие функции. 

1. Распечатка чека на экран. 
2. Подсчет общей суммы покупки. 
3. Получение самой дорогой покупки в чеке. 
4. Подсчет средней стоимости одного товара в чеке. 
"""


check = [['Мандарин', 0.374, 28.90],['Апельсин', 0.545, 27.90],['Мука', 2, 21]]


all_buy = [round(i[1] * i[2], 2) for i in check]
name_p = [i[0] for i in check]
max_len_p = max([len(i) for i in name_p])


def all_sum(all_buy):
    """Подсчет общей суммы покупки."""
    return round(sum(all_buy), 2)

def more_expensive(all_buy):
    """Получение самой дорогой покупки в чеке."""
    for i in check:
        if i[1] * i[2] == max(all_buy):
            exp = i[0]
    return exp

def avg_cost(all_buy):
    """Подсчет средней стоимости одного товара в чеке."""
    return round(sum(all_buy) / len(all_buy), 2)

def print_p():
    res = zip(name_p, all_buy)
    for i in res:
        print(i[0].ljust(max_len_p), '-', i[1])
    print('Сумма покупки:', all_sum(all_buy))
    print('Самый дорогой товар -', more_expensive(all_buy))
    print('Средняя стоимость:', avg_cost(all_buy))

print_p()
