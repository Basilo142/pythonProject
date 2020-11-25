import argparse
import json
import tempfile
import os


STORAGE_PATH = os.path.join(tempfile.gettempdir(), 'storage.data')


def get_data():
    if not os.path.exists(STORAGE_PATH):
        return {}

    with open(STORAGE_PATH, 'r') as f:
        raw_data = f.read()
        if raw_data:
            return json.loads(raw_data)

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
parser.add_argument('--clear', action='store_true', help='Clear')

args = parser.parse_args()

if args.clear:
   os.remove(STORAGE_PATH)
elif args.key and args.val:
    plus(args.key, args.val)
elif args.key:
    print(gat(args.key))
else:
    print('Wrong command')