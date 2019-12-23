"""
6. Написать конвертор валют. Пользователь вводит количество USD, выбирает,
   в какую валюту хочет перевести: EUR, UAH или AZN, и получает в ответ соответствующую сумму.
"""

currency_EUR = 0.9
currency_UAH = 23.32
currency_AZN = 1.7
currency_first = float(input("Enter the amount in USD: "))
currency_second = input("Choose currency EUR, UAH or AZN: ")


if currency_second == "EUR":
    result = currency_first * currency_EUR
elif currency_second == "UAH":
    result = currency_first * currency_UAH
elif currency_second == "AZN":
    result = currency_first * currency_AZN
else:
    result = "Error"

print(result)
