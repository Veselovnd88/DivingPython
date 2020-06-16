import csv
import os


class CarBase:
    def __init__(self, brand, photo_file_name, carrying):
        self.brand = self.validate_input(brand)
        self.photo_file_name = self.validate_photo(photo_file_name)
        self.carrying = float(self.validate_input(carrying))

    def get_photo_file_ext(self):
        ext = os.path.splitext(self.photo_file_name)[-1]
        return ext

    def validate_photo(self, filename:str):
        available = ['.jpg', '.jpeg', '.png', '.gif']
        for i in available:
            if filename.endswith(i):
                print(filename)
                return filename

        raise ValueError

    @staticmethod
    def validate_input(value):
        if value == '':
            raise ValueError
        else:
            return value

    @classmethod
    def create(cls, data):

        params = []
        for i in data:
            params.append(i)
        return cls(*params)


class Car(CarBase):
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        self.passenger_seats_count = int(self.validate_input(passenger_seats_count))
    required = [1, 3, 5, 2]
    car_type = 'car'


class Truck(CarBase):
    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__(brand, photo_file_name, carrying)
        self.body_whl = self.validate_input(body_whl)
        try:
            self.body_length = float(self.body_whl.split('x')[2])
            self.body_width = float(self.body_whl.split('x')[0])
            self.body_height = float(self.body_whl.split('x')[1])
        except ValueError:
            self.body_height = 0.0
            self.body_length = 0.0
            self.body_width = 0.0

    car_type = 'truck'
    required = [1,3,5,4]
    def get_body_volume(self):
        volume = self.body_height * self.body_length * self.body_width
        return volume


class SpecMachine(CarBase):
    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying)
        self.extra = self.validate_input(extra)
    required = [1,3,5,6]
    car_type = 'spec_machine'






def get_car_list(csv_filename):
    car_list = []
    with open(csv_filename, encoding='utf-8') as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')

        next(reader)  # пропускаем заголовок
        car_dict = {'car': Car,
                    'truck': Truck,
                    'spec_machine': SpecMachine}
        for row in reader:
            try:
                car_class = car_dict[row[0]]
                params = []
                for i in car_class.required:
                    params.append(row[i])
                print(params)
                newitem = car_class.create(params)
                print(newitem)
                car_list.append(newitem)
            except Exception:
                pass


    return car_list







print(get_car_list('csv_cars.csv'))