"""Task 2:
В научном институте Василия работают 5 профессоров.
Помогите написать функцию Василию для расчета максимальной разницы
в зарплатах у этих профессоров.

Пример работы:
Вводит 400, 900, 300, 555, 787 - Выводит 600
Вводит 345, 346, 300, 543, 600 - Выводит 300
"""


sal_1 = int(input("Enter the salary of the first professor: ")
sal_2 = int(input("Enter the salary of the second professor: ")
sal_3 = int(input("Enter the salary of the third professor: ")
sal_4 = int(input("Enter the salary of the fourth professor: ")
sal_5 = int(input("Enter the salary of the fifth professor: ")


def all_sal(sal_1, sal_2, sal_3, sal_4, sal_5):
    """Considers the difference in salaries."""

    all_sal = [sal_1, sal_2, sal_3, sal_4, sal_5]
    return max(all_sal) - min(all_sal)


print(all_sal(sal_1, sal_2, sal_3, sal_4, sal_5))

