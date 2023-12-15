from datetime import datetime


class Event:
    observers = []

    def register(self, observer):
        if observer not in self.observers:
            self.observers.append(observer)

    def unregister(self, observer):
        if observer in self.observers:
            self.observers.remove(observer)

    def notify(self, event, data=None):
        for observer in self.observers:
            observer(event, data)


class FileLoger:
    def __init__(self, filename):
        self.filename = filename

    def __call__(self, event, data):
        with open(self.filename, 'a') as fn:
            fn.write(f'{datetime.now()}: {event}, {data} \n')


def loger(event, data):
    print(event, data)


event = Event()
event.register(loger)
fn = FileLoger('loger.txt')
event.register(fn)
event.notify('ping', 60)
event.notify('ping', 34)
event.notify('ping', 43)
event.notify('ping34', 60)




