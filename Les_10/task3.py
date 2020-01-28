"""
Реализовать класс, описывающий окружность.
В классе должны быть следующие компоненты: 
■ поле, хранящее радиус окружности; 
■ get-свойство, возвращающее радиус окружности; 
■ set-свойство, устанавливающее радиус окружности; 
■ get-свойство, возвращающее диаметр окружности; 
■ метод, вычисляющий площадь окружности; 
■ метод, вычисляющий длину окружности. 
Продемонстрировать работу свойств и методов.
"""


import math


class Circle:
    
    def __init__(self, radius=0):
        self.set_radius(radius)
    
    def set_radius(self, radius):
        assert radius > 0, "Радиус должен быть положительным!"
        self._radius = radius
    
    def get_radius(self):
        return self._radius

    def get_diam(self):
        return self._radius * 2

    def square(self):
        return math.pi * self._radius**2

    def length(self):
        return 2 * math.pi * self._radius


c = Circle(3)
print(f"Радиус окружности = {c.get_radius()}")
print(f"Диаметр окружности = {c.get_diam()}")
print(f"Площадь окружности = {c.square()}")
print(f"Длина окружности = {c.length()}")
