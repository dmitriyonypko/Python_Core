"""
1. Запросить у пользователя его возраст и определить,
   кем он является: ребенком (0–2), подростком (12–18),
   взрослым (18_60) или пенсионером (60– ...).
"""


age = int(input("Enter your age: "))

if age >= 0 and age < 12:
    result = "Вы ребенок"
elif age >= 12 and age < 18:
    result = "Вы подросток"
elif age >= 18 and age < 60:
    result = "Вы взрослый"
elif age >= 60:
    result = "Вы пенсионер"
else:
    result = "Введите корректный возраст"

print(result)

