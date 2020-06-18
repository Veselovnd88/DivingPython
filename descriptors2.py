class Logs:

    def __set__(self, instance, value):
        with open('text.txt', 'w', encoding='utf8') as f:
            data = 'Tail length ' + str(value)
            f.write(data)

    def __get__(self, instance, owner):
        return instance.tail


class Dog:
    tail = Logs()

    def __init__(self, color):
        self.color = color


sharik = Dog('Black')
sharik.tail = 100
