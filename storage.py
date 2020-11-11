import argparse
import json
import tempfile
import os


STORAGE_PATH = os.path.join(tempfile.gettempdir(), 'storage.data')


def get_data():
    if not os.path.exists(STORAGE_PATH):
        return {}

    with open(STORAGE_PATH, 'r') as f:
        data = f.read()
        if data:
            return json.loads(data)

        return {}


def plus(key, value):
    data = get_data()

    if key in data:
        data[key].append(value)
    else:
        data[key] = [value]

    with open(STORAGE_PATH, 'w') as f:
        f.write(json.dumps(data))


def gat(key):
    data = get_data()

    return data.get(key)


parser = argparse.ArgumentParser()
parser.add_argument('--key', help='Key')
parser.add_argument('--val', help='Value')


args = parser.parse_args()

if args.key and args.val:
    plus(args.key, args.val)
elif args.key:
    print(str(gat(args.key)))
else:
    print('Error')

