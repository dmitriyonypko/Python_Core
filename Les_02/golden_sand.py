"""Золотой песок
Сотрудники завода по производству золотого песка из воздуха решили поправить свое финансовое положение.
Они пробрались на склад завода, где хранился золотой песок трех видов.
Один килограмм золотого песка первого вида они смогли бы продать за A1 рублей,
второго вида – за A2 рублей, а третьего вида – за A3 рублей. Так получилось,
что у сотрудников оказалось с собой только три емкости: первая была рассчитана на B1 килограмм груза,
вторая на B2 килограмм, а третья на B3 килограмм. Им надо было заполнить полностью все емкости таким образом,
чтобы получить как можно больше денег за весь песок. При заполнении емкостей нельзя смешивать песок разных видов,
то есть, в одну емкость помещать более одного вида песка, и заполнять емкости песком так,
чтобы один вид песка находился более чем в одной емкости.

Требуется написать программу, которая определяет,
за какую сумму предприимчивые сотрудники смогут продать весь песок
в случае наилучшего для себя заполнения емкостей песком.

Входные данные
Пользователь вводит с клавиатуры 6 натуральных чисел A1, A2, A3, B1, B2, B3. Все числа не превосходят 100.

Выходные данные
Вывести на экран единственное целое число – сумму в рублях,
которую смогут сотрудники заработать в случае наилучшего для себя заполнения емкостей песком.
"""


price_1 = int(input("Enter the first prise (1 - 100RUB): "))
price_2 = int(input("Enter the second item (1 - 100RUB): "))
price_3 = int(input("Enter the third item (1 - 100RUB): "))

capacity_1 = int(input("Enter the capacity of the first bucket (1 - 100kg): "))
capacity_2 = int(input("Enter the capacity of the second bucket (1 - 100kg): "))
capacity_3 = int(input("Enter the capacity of the third bucket (1 - 100kg): "))


def item_level(item_a, item_b, item_c):
    """Find and return max, middle and min item."""
    # Find max item
    if item_a > item_b and item_a > item_c:
        max_item = item_a
    elif item_b > item_a and item_b > item_c:
        max_item = item_b
    else:
        max_item = item_c
    # Find min item
    if item_a < item_b and item_a < item_c:
        min_item = item_a
    elif item_b < item_a and item_b < item_c:
        min_item = item_b
    else:
        min_item = item_c
    # Find middle item
    if item_a < max_item and item_a > min_item:
        middle_item = item_a
    elif item_b < max_item and item_b > min_item:
        middle_item = item_b
    else:
        middle_item = item_c
    return max_item, middle_item, min_item


price = item_level(price_1, price_2, price_3)
capacity = item_level(capacity_1, capacity_2, capacity_3)
result = (price[0] * capacity[0]) + (price[1] * capacity[1]) + (price[2] * capacity[2])
print(f"Maximum earnings = {result} RUB")
