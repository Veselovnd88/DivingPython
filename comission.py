class Value:
    def __init__(self):
        self.amount = 0

    def __set__(self, instance, value):
        """при установке значения атрибут вычисляется
        value - значение которое присваивается, instanse - экз класса"""
        self.amount = value - instance.commission * value

    def __get__(self, instance, owner):
        """ Возврат при обращении к атрибуту"""
        return self.amount


class Account:
    amount = Value()

    def __init__(self, commission):
        self.commission = commission


new = Account(0.9)
new.amount = 100
print(new.amount)
