# Реализовать метакласс. позволяющий создавать всегда один и
# тот же объект класса (см. урок)

class SingletonMeta(type):
    instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls.instances:
            cls.instances[cls] = super().__call__(*args, **kwargs)
        return cls.instances[cls]
class MyClass(metaclass = SingletonMeta):
    def method_1(self):
        pass
    def method_2(self):
        pass

obj_1 = MyClass()
obj_2 = MyClass()
print(obj_1 is obj_2)

