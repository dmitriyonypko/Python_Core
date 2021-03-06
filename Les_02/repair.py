"""
Ваш любимый дядя – директор фирмы, которая делает евроремонты в офисах.
В связи с финансово-экономическим кризисом, дядюшка решил оптимизировать свое предприятие.
Давно ходят слухи, что бригадир в дядюшкиной фирме покупает лишнее количество стройматериалов,
а остатки использует для отделки своей новой дачи. Ваш дядя заинтересовался,
сколько в действительности банок краски необходимо для покраски стен в офисе длиной L метров,
шириной – W и высотой – H, если одной банки хватает на 16м2, а размерами дверей и окон можно пренебречь?
Заказов много, поэтому дядя попросил написать программу, которая будет все это считать.

Входные данные
Пользователь вводит с клавиатуры три натуральных числа L, W, H – длину, ширину и высоту офиса в метрах соответственно,
каждое из которых не превышает 1000.

Выходные данные
Вывести на экран одно целое число – минимальное количество банок краски, необходимых для покраски стен в офисе.
"""


length = float(input("Enter the length of the room (1 - 1000m): "))
width = float(input("Enter the width of the room (1 - 1000m): "))
height = float(input("Enter the height of the room (1 - 1000m): "))
countMeters = 16


area = height * (length * 2 + width * 2)
if area < countMeters:
    result = 1
else:
    result = int((area / countMeters) + 0.5)
print("The number of cans of paint needed to paint the walls in the office is", result)
