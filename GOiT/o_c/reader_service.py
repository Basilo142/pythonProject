from reader import YAMLEReader, JSONReader, Reader


class ReaderService:
    def __init__(self, reader: Reader):
        self.reader = reader

    def get(self, key):
        return self.reader.get_value(key)


if __name__ == "__main__":
    reader_json = ReaderService(JSONReader('data.json')).get("name")
    reader_yaml = ReaderService(YAMLEReader('data.yaml')).get('phone')
    print(reader_json, reader_yaml)
