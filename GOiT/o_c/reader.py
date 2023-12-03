import json
import yaml


class Reader:
    def get_value(self, key):
        raise NotImplemented


class JSONReader(Reader):
    def __init__(self, filename):
        self.filename = filename

    def get_value(self, key):
        with open(self.filename, 'r') as f:
            data = json.load(f)
            return data.get(key, None)


class YAMLEReader(Reader):
    def __init__(self, filename):
        self.filename = filename

    def get_value(self, key):
        with open(self.filename, 'r') as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            return data.get(key, None)
