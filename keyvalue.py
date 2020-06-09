import argparse
import os
import tempfile
import json


def read(storage_path):
    if not os.path.exists(storage_path):
        return {}
    with open(storage_path, 'r') as file:
        raw_data = file.read()
        if raw_data:
            # result = json.loads(raw_data)
            result = 'da'
        else:
            result = {}
        return result




def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('--key', type=str)
    parser.add_argument('--value', type=str)
    args = parser.parse_args()
    return args

def write(file, key, value):
    with open(file, 'w') as file:


        file.write('Hello')


def put(storage_path, key, value):
    data = storage_path.read()
    data[key] = value
    print(data)



def get(storage_path, key):
    pass
if __name__ == '__main__':
    storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
    print(storage_path)
    write(storage_path,'500','599')
    print(read(storage_path))