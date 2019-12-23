"""
8. Запросить у пользователя длину окружности и периметр квадрата.
   Определить, может ли такая окружность поместиться в указанный квадрат. 
"""


circle_L = float(input("Enter lap length: "))
square_P = float(input("Enter the perimeter of the square: "))
PI = 3.14


diameter = circle_L / PI
side_square = square_P / 4

result = "Yes" if diameter == side_square else "No"
print(result)
