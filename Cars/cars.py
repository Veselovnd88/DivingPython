import csv
import os


class CarBase:
    def __init__(self, brand, photo_file_name, carrying):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = carrying

    def get_photo_file_ext(self):
        ext = os.path.splitext(self.photo_file_name)[-1]
        return ext

    @staticmethod
    def read_csv(filename):
        with open(csv_filename) as csv_fd:
            reader = csv.reader(csv_fd, delimiter=';')
            next(reader)  # пропускаем заголовок
            for row in reader:
                print(row)


class Car(CarBase):
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        self.passenger_seats_count = passenger_seats_count


class Truck(CarBase):
    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__(brand, photo_file_name, carrying)
        self.body_whl = body_whl
        try:
            self.body_length = float(self.body_whl.split('x')[2])
            self.body_width = float(self.body_whl.split('x')[0])
            self.body_height = float(self.body_whl.split('x')[1])
        except ValueError:
            self.body_height = 0
            self.body_length = 0
            self.body_width = 0

    def get_body_volume(self):
        volume = self.body_height * self.body_length * self.body_width
        return volume


class SpecMachine(CarBase):
    def __init__(self, brand, photo_file_name, carrying, extra):
        pass


def get_car_list(csv_filename):
    car_list = []

    return car_list


new = Truck('Nissan', 'car.jpeg', 500, '4x1xjo')

print(new.brand, new.carrying, new.body_height)
print(new.get_body_volume())
