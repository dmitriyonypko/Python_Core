"""
3. Запросить у пользователя трехзначное и число и проверить,
   есть ли в нем одинаковые цифры.
"""


num = int(input("Enter the numer (100 - 999): "))


a = num // 100
num %= 100
b = num // 10
num %= 10
c = num

if a == b or a == c:
    result = "Yes"
elif b == c:
    result = "Yes"
else:
    result = "No"

print(result)
