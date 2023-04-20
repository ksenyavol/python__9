# 1) реализовать дескрипторы для любых двух классов

class NonNegative:
    def __init__(self, name):
        self.name = name
    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

class Worker:
    name = NonNegative('name')
    surname = NonNegative('surname')
    def __init__(self, name, surname, position, salary):
        self.name = name
        self.surname = surname
        self.position = position
        self.salary = salary

    def full_name(self):
        return self.name + self.surname

OBJ = Worker('Игорь', 'Петров', 'Оператор', 30000)
print(OBJ.full_name())


OBJ.name = 'Игорь'
OBJ.surname = 'Петров'
print(OBJ.__dict__)
print(OBJ.full_name())

