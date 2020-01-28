"""
Реализовать класс Employee, описывающий работника, и создать массив работников банка. 
Реализовать класс EmpTable для генерации кода таблицы со списком работников банка. 
Массив работников необходимо передавать через конструктор, а получать код с помощью метода getCodel(). 
Создать объект класса EmpTable и вывести в консоль результат работы метода getCode()
"""


class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary
    
    def __str__(self):
        return f'{self.name.ljust(15)} Position: {self.position.ljust(15)} Salary: {self.salary}'

class EmpTable:
    def __init__(self, *args):
        self.all_emp = args
    
    def getCode(self):
        for item in self.all_emp:
            print(item)


empl1 = Employee('John', 'Manager', 2500)
empl2 = Employee('Dean', 'Developer', 1500)
empl3 = Employee('Sam', 'Consultant', 700)

empl_table = EmpTable(empl1, empl2, empl3)
empl_table.getCode()
