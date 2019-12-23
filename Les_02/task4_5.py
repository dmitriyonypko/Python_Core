"""
5. Запросить у пользователя пятиразрядное число и определить,
   является ли  оно палиндромом.
"""


num = int(input("Enter the numer (10000 - 99999): "))


dig_1 = num // 10000
num %= 10000
dig_2 = num // 1000
num %= 1000
dig_3 = num // 100
num %= 100
dig_4 = num // 10
num %= 10
dig_5 = num

result = "Palindrome" if dig_1 == dig_5 and dig_2 == dig_4 else "Not a palindrome"
print(result)
