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


# -------------------------------------------------------------------------------------

from abc import ABC, abstractmethod


class Publisher(ABC):
    @abstractmethod
    def attach(self, observer):
        pass

    @abstractmethod
    def detach(self, observer):
        pass

    @abstractmethod
    def notify(self):
        pass


class PublisherMessages(Publisher):
    _observers = []
    _indicator = 0

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update(self)

    def business_logic_execution(self):
        print(f"Application logic is being executed. Indicator: {self._indicator}")
        self._indicator += 1
        self.notify()


class Observer(ABC):
    @abstractmethod
    def update(self, publisher):
        pass


class ObserverA(Observer):
    def update(self, publisher):
        if publisher._indicator <= 3:
            print("ObserverA: reacts to the indicator less than 2")


class ObserverB(Observer):
    def update(self, publisher):
        if publisher._indicator > 2:
            print("ObserverB: reacts to the indicator greater than 2")


def client():
    publisher = PublisherMessages()

    observer_a = ObserverA()
    publisher.attach(observer_a)

    observer_b = ObserverB()
    publisher.attach(observer_b)

    publisher.business_logic_execution()
    publisher.business_logic_execution()
    publisher.detach(observer_a)
    publisher.business_logic_execution()


if __name__ == "__main__":

    client()

