import argparse
import os
import tempfile
import json

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
def read(storage_path):
    if not os.path.exists(storage_path):
        return {}
    with open(storage_path, 'r') as file:
        raw_data = file.read()
        if raw_data:
            result = json.loads(raw_data)
        else:
            result = {}
        return result




def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('--key', type=str)
    parser.add_argument('--value', type=str)
    args = parser.parse_args()
    if args.key and args.value:
        pass

def write(file, key, value):
    with open(file, w) as file:
        data[key] = value
        file.write(json.dump(data))


def put(storage_path, key, value):
    data = storage_path.read()
    if key in data:

parse()
read(storage_path)