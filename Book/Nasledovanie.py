class Pet:
    def __init__(self, name=None):
        self.name = name

class Dog(Pet):
    def __init__(self, name, breed=None):
        super().__init__(name)
        self.breed = breed

    def say(self):
        return "{0}: waw".format(self.name)


dog = Dog("Шарик", "Доберман")
print(dog.name)
print(dog.say())
print(dog.breed)


import json

class ExportJSON:
    def to_json(self):
        return json.dumps({
            "name": self.name,
            "breed": self.breed
        })
class ExDog(Dog, ExportJSON):
    def __init__(self, name, breed=None):
        super().__init__(name, breed)


class WoolenDog(Dog, ExportJSON):
    def __init__(self, name, breed=None):
        super(Dog, self).__init__(name)
        self.breed = "Якась фигня = {0}".format(breed)

dog = WoolenDog('Жучка','Такса')
print(dog.breed)


dog = ExDog('Belka', breed='Dvornjaga')
print(dog.to_json())

