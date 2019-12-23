"""
Task 2: игра "Камень", "Ножницы", "Бумага"
"""


import random


user = input('Введите один из трёх вариантов "Камень", "Ножницы" или "Бумага": ')
computer = random.randint(1, 3)


if computer == 1:
    computer = "Камень"
elif computer == 2:
    computer = "Ножницы"
elif computer == 3:
    computer = "Бумага"

if user == computer:
    result = "Ничья"
elif user == "Камень" and computer == "Ножницы":
    result = "Вы победили"
elif user == "Ножницы" and computer == "Бумага":
    result = "Вы победили"
elif user == "Бумага" and computer == "Камень":
    result = "Вы победили"
else:
    result = "Победил компьютер"

if user != "Камень" and user != "Ножницы" and user != "Бумага":
    print("Введите один из трёх вариантов!")
else:
    print("Выбор компьютера:", computer)
    print(result)
