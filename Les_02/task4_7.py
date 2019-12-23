"""
7. Запросить у пользователя сумму покупки и вывести сумму к оплате со скидкой:
   от 200 до 300 – скидка будет 3%, от 300 до 500 – 5%, от 500 и выше – 7%.
"""


purchase_sum = float(input("Enter purchase amount: "))


if purchase_sum >= 200 and purchase_sum < 300:
    purchase_sum = purchase_sum - (purchase_sum * 0.03)
elif purchase_sum >= 300 and purchase_sum < 500:
    purchase_sum = purchase_sum - (purchase_sum * 0.05)
elif purchase_sum >= 500:
    purchase_sum = purchase_sum - (purchase_sum * 0.07)

print("Amount to pay:", purchase_sum)
