from abc import ABC, abstractmethod


class Creature(ABC):

    @abstractmethod
    def feed(self):
        pass

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def make_noise(self):
        pass


class Animal(Creature):

    def feed(self):
        print("i eat grass")

    def move(self):
        print("I walk forward")

    def make_noise(self):
        print("WOO")


class AbstractDecorator(Creature):

    def __init__(self, base):
        self.base = base

    def move(self):
        self.base.move()

    def feed(self):
        self.base.feed()

    def make_noise(self):
        self.base.make_noise()


class Swim(AbstractDecorator):
    def move(self):
        print('i ssss')

    def make_noise(self):
        print('......')


anim = Animal()
anim.move()
anim.feed()
anim.make_noise()


aaa = Swim(anim)
aaa.move()
aaa.feed()
aaa.make_noise()
