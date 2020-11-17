class FileReader:
    def __init__(self, file):
        self._file=file
    def read(self):
        try:
            with open(self._file,'r') as f:
                return f.read()
        except IOError:
            return ''