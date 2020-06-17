import os


class FileReader:
    def __init__(self, filename):
        self.filename = filename
        self.current_pos = 0

    def read(self):
        try:
            with open(self.filename, 'r', encoding='utf8') as f:
                data = f.read()
                return data
        except FileNotFoundError:
            return ''

    def write(self,string):
        with open(self.filename, 'w', encoding='utf8') as f:
            data = f.write(string)
            return data

    def __add__(self, other):
        data1 = self.read()
        data2 = other.read()
        with open('newfile.txt','w', encoding='utf8') as newfile:
            data = newfile.write(data1+data2)
        return FileReader('newfile.txt')



    def __str__(self):
        return self.filename


    def __iter__(self):
        return self

    def __next__(self):
        with open(self.filename, 'r', encoding='utf8') as f:
            f.seek(self.current_pos)
            line = f.readline()
            if not line:
                self.current_pos = 0
                raise StopIteration
            self.current_pos = f.tell()
            return line



new = FileReader('text.txt')

for line in new:
    print(line)