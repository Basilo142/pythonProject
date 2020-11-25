class Planet:
    pass




solar_system=[]
for i in range(8):
    planet=Planet()
    solar_system.append(planet)


print('ss', solar_system)
print('pl', planet)


class Planet:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return f"Planet {self.name}"

earth = Planet('Earth')
print('en', earth.name)
print('e',earth)

solar_system=[]
planet_name=[
    "Mercury", "Venus", "Earth", 'Mars', 'Jup', "Sate", "Uranus", "Neptune"
]

for name in planet_name:
    planet=Planet(name)
    solar_system.append(planet)

print('SS=',solar_system)


mars= Planet("Mars")
print(mars)
mars.name="Second Earth"
print(mars)






