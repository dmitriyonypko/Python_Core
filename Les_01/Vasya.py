"""Task 1: Вася
Вася работает программистом и получает 50$ за каждые 100 строк кода.
За каждое третье опоздание Васю штрафуют на 20$.

Реализовать меню :
1. Пользователь вводит желаемый доход Васи и количество опозданий, посчитать,
   сколько строк кода ему надо написать.
2. Пользователь вводит количество строк кода, написанное Васей и желаемый объем зарплаты.
   Посчитать, сколько раз Вася может опоздать.
3. Пользователь вводит количество строк кода и количество опозданий,
   определить, сколько денег заплатят Васе и заплатят ли вообще.
"""


action = int(input("Выберите действие(1 - 3): "))


def action_1():
    """
    1. Пользователь вводит желаемый доход Васи и количество опозданий, посчитать,
       сколько строк кода ему нужно написать.
    """
    salary = int(input("Введите желаемый доход: "))
    delays = int(input("Введите кол-во опозданий: "))
    penalty = (delays // 3) * 20
    sum_money = salary + penalty
    mod = sum_money % 50
    if mod != 0:
        sum_money += 50 - mod
    result = sum_money // 50 * 100
    print("Васе нужно написать:", result, "строк кода")

def action_2():
    """
    2. Пользователь вводит количество строк кода, написанное Васей и желаемый объем зарплаты.
       Посчитать, сколько раз Вася может опоздать.
    """
    count_lines = int(input("Введите кол-во строк кода: "))
    salary = int(input("Введите желаемый объем зарплаты: "))
    max_salary = (count_lines // 100) * 50
    if count_lines < 0:
        print("Ошибка")
    else:
        if max_salary < salary:
            result = 0
            print("За введенное кол-во строк кода, "\
                  "Вася не может получить больше", max_salary, "$!")
        else:
            result = max_salary - salary
            result = (result // 20) * 3
        print("Допустимое кол-во опозданий:", result)

def action_3():
    """
    3. Пользователь вводит количество строк кода и количество опозданий,
       определить, сколько денег заплатят Васе и заплатят ли вообще.
    """
    count_lines = int(input("Введите кол-во строк кода: "))
    delays = int(input("Введите кол-во опозданий: "))
    penalty = delays // 3 * 20
    max_salary = count_lines // 100 * 50
    salary = max_salary - penalty
    if salary < 0:
        print("Зарплата Васи: 0 $")
    else:
        print("Зарплата Васи:", salary, "$")


if action == 1:
    action_1()
elif action == 2:
    action_2()
elif action == 3:
    action_3()
else:
    print("Введите только один из трёх вариантов!")
