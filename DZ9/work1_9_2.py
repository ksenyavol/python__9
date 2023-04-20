# 1.2) Реализовать дескрипторы для любых двух классов

class NumValidator:
    def set(self, instance, value):
        if not isinstance(value, int):
            raise TypeError(f"Переменная "f"{self.my_attr} должна быть числом.")
        elif value < 0:
            raise ValueError(f'{self.my_attr} не может 'f' быть отрицательным')
            instance.__dict__[self.my_attr] = value
    def __set_name__(self, owner, my_attr):
        self.my_attr = my_attr
class Road:
    _length = NumValidator()
    _width = NumValidator()
    weight = 25
    thickness = 0.5

    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width
    def asphalt(self):
        res_kg = int(self._length * self._width * self.weight *
                     self.thickness)
        res_t = int(res_kg / 1000)
        print(f'{self._length}м*{self._width}м*'
              f'{self.weight}кг*{self.thickness}м = '
              f'{res_kg}кг = {res_t}т')

        
work = Road(5000, 20)
work.asphalt()
