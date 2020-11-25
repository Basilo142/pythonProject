class Planet:

    count = 0

    def __init__(self, name, population=None):
        self.name = name
        self.population = population or []
        Planet.count+=1
    def __repr__(self):
        return f"Planet {self.name}"

planet = Planet('Earth')
mars = Planet('Mars')
print(Planet.count)
print('e',planet)


class Human:
    def __del__(self):
        print("Goodbye")


print(planet.__class__)