"""
2. Запросить у пользователя число от 0 до 9 и вывести ему спецсимвол,
   который расположен на этой клавише (1–!, 2–@, 3–# и т. д).
"""


num = int(input("Enter the numer (0 - 9): "))

if num == 1:
    result = "!"
elif num == 2:
    result ="@"
elif num == 3:
    result ="#"
elif num == 4:
    result ="$"
elif num == 5:
    result ="%"
elif num == 6:
    result ="^"
elif num == 7:
    result ="&"
elif num == 8:
    result ="*"
elif num == 9:
    result ="("
elif num == 0:
    result =")"
else:
    result = "Error"

print(result)
