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
            result = json.loads(raw_data)

        else:
            result = {}
        return result


def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('--key', type=str)
    parser.add_argument('--value', type=str)
    args = parser.parse_args()
    return args


def write(file, data):
    with open(file, 'w') as file:
        file.write(json.dumps(data))


def put(key, value):
    data = read(storage_path)
    data[key] = data.get(key, list())
    data[key].append(value)
    return data


def get(key):
    data = read(storage_path)
    return data.get(key, [])


def key_value(storage_path):
    args = parse()
    if args.key and args.value:
        data = put(args.key, args.value)
        write(storage_path, data)
    elif args.key and args.value is None:
        data = get(args.key)
        print(*data, sep=', ')
    else:
        print('Invalid parameters')


if __name__ == '__main__':
    storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')

    key_value(storage_path)
