"""
10. Запросить дату (день, месяц, год) и вывести следующую за ней дату.
    Учтите возможность перехода на следующий месяц, год, а также високосный год
"""


day = int(input("Enter day: "))
month = int(input("Enter month: "))
year = int(input("Enter year: "))


def leap_year(year):
    """leap year"""
    if year % 400 == 0:
        result = 1
    elif year % 4 == 0 and year % 100 != 0:
        result = 1
    else:
        result = 0
    return result
    

if leap_year(year) and (day == 28 and month == 2):
    day = 29
elif not leap_year(year) and (day == 28 and month == 2):
    day = 1
    month = 3
elif day == 31 and month == 12:
    day = 1
    month = 1
    year += 1
elif day == 31 and month == 1 or month == 3 or month == 5 \
    or month == 7 or month == 8 or month == 10:
    day = 1
    month += 1
elif day == 30 and month == 4 or month == 6 or month == 9 \
    or month == 11:
    day = 1
    month += 1
elif day >= 1 and day <= 31 and month == 1 or month == 3 \
     or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    day += 1
elif day >= 1 and day <= 30 and month == 4 or month == 6 \
     or month == 9 or month == 11:
    day += 1
elif day >= 1 and day < 28 and month == 2:
    day += 1
elif year >= 0 and month > 0 and month <= 12:
    pass
else:
    print("Error! Enter a valid date!")

print(f"{day}.{month}.{year}")
